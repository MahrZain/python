# Generated by Django 5.0.6 on 2024-06-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=120)),
                ('price', models.IntegerField()),
                ('category', models.TextField(max_length=60)),
            ],
        ),
    ]
