# Generated by Django 5.1.4 on 2025-03-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subtitle', '0004_remove_subtitle_image_subtitle_image_folder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtitle',
            name='image_folder',
        ),
        migrations.AddField(
            model_name='subtitle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
