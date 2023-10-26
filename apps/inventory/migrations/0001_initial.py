# Generated by Django 4.2.5 on 2023-10-26 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_option_optiongroup_optiongroupvalue_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=65, null=True, unique=True)),
                ('buy_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('sale_price', models.PositiveBigIntegerField()),
                ('num_stock', models.PositiveIntegerField()),
                ('threshold_low_stack', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockrecords', to='product.product')),
            ],
            options={
                'verbose_name': 'Stock Record',
                'verbose_name_plural': 'Stock Records',
            },
        ),
    ]
