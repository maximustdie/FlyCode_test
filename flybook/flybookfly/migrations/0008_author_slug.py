# Generated by Django 4.1.1 on 2022-09-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flybookfly', '0007_remove_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Слаг книги'),
        ),
    ]