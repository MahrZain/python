# Generated by Django 5.0.6 on 2024-06-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_alter_banner_banner_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='banner_image',
        ),
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.FileField(null=True, upload_to='secbanner/'),
        ),
    ]