# Generated by Django 4.2.5 on 2023-09-23 00:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_rename_customer_costomer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costomer',
            new_name='Customer',
        ),
    ]
