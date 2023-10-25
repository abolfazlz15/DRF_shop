from django.dispatch import receiver
from django.db.models.signals import pre_save

from apps.media.exceptions import DuplicateImageException
from apps.media.models import Image


@receiver(pre_save, sender=Image)
def check_duplicate_hash(sender, instance, **kwargs):
    existed = Image.objects.filter(file_hash=instance.file_hash).exclude(pk=instance.pk).exists()
    if existed:
        raise DuplicateImageException('Duplicate')
