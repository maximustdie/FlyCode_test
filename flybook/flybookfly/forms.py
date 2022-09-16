from django.forms import ModelForm
from .models import Book, Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'annotation', 'author', 'archived', 'slug']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
