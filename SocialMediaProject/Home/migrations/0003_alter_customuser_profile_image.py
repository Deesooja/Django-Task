# Generated by Django 3.2.6 on 2023-02-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_friend_friendrequest_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.FileField(default=None, null=True, upload_to='user_profile_image/'),
        ),
    ]
