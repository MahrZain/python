# Generated by Django 5.0.6 on 2024-06-27 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='rating',
            new_name='sale',
        ),
    ]
