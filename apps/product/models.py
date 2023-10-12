from django.db import models
from treebeard.mp_tree import MP_Node
from django.utils.text import slugify
from managers import CategoryQuerySet


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    is_public = CategoryQuerySet

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
