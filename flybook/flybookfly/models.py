from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='Слаг автора')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('author_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.last_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    annotation = models.TextField(verbose_name='Аннотация')
    author = models.ManyToManyField(Author, verbose_name='Автор книги', related_name='books')
    archived = models.BooleanField(default=False, verbose_name='Отправлено в архив')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='Слаг книги')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def get_absolute_url(self):
        return reverse('book_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор комментария', related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга', related_name='comments')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Дата создания: {self.create_time}, Автор комментария:{self.author} Книга:{self.book}'
