# Generated by Django 3.2.6 on 2023-02-15 13:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
