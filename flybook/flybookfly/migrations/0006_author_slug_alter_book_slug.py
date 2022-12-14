# Generated by Django 4.1.1 on 2022-09-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flybookfly', '0005_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Слаг автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Слаг книги'),
        ),
    ]
