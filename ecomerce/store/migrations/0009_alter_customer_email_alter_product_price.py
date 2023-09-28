# Generated by Django 4.2.5 on 2023-09-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_shipping_address_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, default='noreply@example.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]