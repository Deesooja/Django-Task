# Generated by Django 3.2.6 on 2023-02-15 12:37

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255, null=True, verbose_name='image'),
        ),
    ]
