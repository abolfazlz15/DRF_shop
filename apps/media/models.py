import hashlib

from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(width_field='width', height_field='height', upload_to='image')
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
    file_hash = models.CharField(max_length=40, db_index=True, editable=False)
    file_size = models.PositiveIntegerField(null=True, editable=False)

    def save(self, *args, **kwargs):
        self.file_size = self.image.size
        self.file_hash = self.hash_image_file()
        super().save(*args, **kwargs)

    def hash_image_file(self):
        hasher = hashlib.sha1()
        for chunk in self.image.file.chunks():
            hasher.update(chunk)
        return hasher.hexdigest()
