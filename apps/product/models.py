from django.db import models
from treebeard.mp_tree import MP_Node
from django.utils.text import slugify
from apps.product.managers import CategoryQuerySet
from libs.db.db_fields import UpperCaseCharField


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


class ProductClass(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, null=True)

    track_stock = models.BooleanField(default=True)
    is_shipping = models.BooleanField(default=True)
    option = models.ManyToManyField('Option')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(ProductClass, self).save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Class'
        verbose_name_plural = 'Products Classes'


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
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE, null=True, related_name='attributes')
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

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'


class Product(models.Model):
    class ProductTypeChoice(models.TextChoices):
        standalone = 'standalone'
        parent = 'parent'
        child = 'child'

    structure = models.CharField(max_length=20, choices=ProductTypeChoice.choices, default=ProductTypeChoice.standalone)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=130, null=True, blank=True)
    upc = UpperCaseCharField(max_length=24, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, null=True)
    meta_title = models.CharField(max_length=130, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    product_class = models.ForeignKey(ProductClass, on_delete=models.PROTECT, null=True, blank=True,
                                      related_name='products')
    attributes = models.ManyToManyField(ProductAttribute, through='ProductAttributeValue')
    recommended_products = models.ManyToManyField('Product')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value_text = models.TextField(null=True, blank=True)
    value_integer = models.IntegerField(null=True, blank=True)
    value_float = models.FloatField(null=True, blank=True)
    value_option = models.ForeignKey(OptionGroupValue, on_delete=models.PROTECT)
    value_multi_option = models.ManyToManyField(OptionGroupValue, related_name='multi_valued_attribute_value')

    class Meta:
        verbose_name = 'Attribute Value'
        verbose_name_plural = 'Attribute Values'
        unique_together = ('product', 'attribute')


class ProductRecommendation(models.Model):
    primary = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='primary_recommendation')
    recommendation = models.ForeignKey(Product, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ('primary', 'recommendation')
        ordering = ('primary', '-rank')
