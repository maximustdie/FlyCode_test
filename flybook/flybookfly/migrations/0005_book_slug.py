# Generated by Django 4.1.1 on 2022-09-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flybookfly', '0004_alter_book_archived_alter_book_author_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='SOME SLUG', max_length=100, unique=True),
        ),
    ]
