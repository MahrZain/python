# Generated by Django 5.0.6 on 2024-06-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0005_alter_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.FileField(help_text='Max Resolutions (1460 × 822) Only One Image Will Be Shown at a Time! ', null=True, upload_to='secbanner/'),
        ),
    ]
