# Generated by Django 5.0.6 on 2024-06-16 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0003_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='post_app/media/uploads/'),
        ),
    ]
