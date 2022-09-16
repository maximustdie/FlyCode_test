from django.contrib import admin
from .models import Author, Book, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'get_count_books', 'get_count_comments')

    @admin.display(description='Имя автора')
    def full_name(self, obj):
        return f'{obj.last_name} {obj.first_name}'

    @admin.display(description='Кол-во книг')
    def get_count_books(self, obj):
        return Book.objects.filter(author__id=obj.id).count()

    @admin.display(description='Кол-во комментариев')
    def get_count_comments(self, obj):
        return Comment.objects.filter(author__id=obj.id).count()


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'get_count_comments', )
    filter_horizontal = ['author']

    @admin.display(description='Автор')
    def get_authors(self, obj):
        return ", ".join([f'{a.first_name} {a.last_name}' for a in obj.author.all()])

    @admin.display(description='Кол-во комментариев')
    def get_count_comments(self, obj):
        return Comment.objects.filter(book__id=obj.id).count()


class CommentAdmin(admin.ModelAdmin):
    list_display = ('create_time', 'update_time', 'author', 'book')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
