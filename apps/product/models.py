from django.db import models
from treebeard.mp_tree import MP_Node
from django.utils.text import slugify
from apps.product.managers import CategoryQuerySet


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    is_public = CategoryQuerySet

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class OptionGroup(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Option Group'
        verbose_name_plural = 'Option Groups'


class OptionGroupValue(models.Model):
    title = models.CharField(max_length=255)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.group}'

    class Meta:
        verbose_name = 'Option Group'
        verbose_name_plural = 'Option Groups Values'


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, null=True)

    track_stock = models.BooleanField(default=True)
    is_shipping = models.BooleanField(default=True)
    option = models.ManyToManyField('Option')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Product, self).save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductAttribute(models.Model):
    class AttributeTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option = 'option'
        multi_option = 'multi_option'

    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=25, choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.text)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='attributes')
    is_required = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Attribute'
        verbose_name_plural = 'Products Attributes'


class Option(models.Model):
    class OptionTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option = 'option'
        multi_option = 'multi_option'

    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=25, choices=OptionTypeChoice.choices,
                            default=OptionTypeChoice.text)
    is_required = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
