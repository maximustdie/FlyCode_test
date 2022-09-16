from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from .models import Book, Author, Comment
from .forms import BookForm, CommentForm


def index(request):
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'flybookfly/index.html', context)


class BookDetail(DetailView):
    model = Book
    template_name = 'flybookfly/book_detail.html'


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'flybookfly/book_update_form.html'
    success_url = reverse_lazy('index')


class BookDelete(DeleteView):
    model = Book
    template_name = 'flybookfly/book_delete_form.html'
    success_url = reverse_lazy('index')


class AuthorDetail(DetailView):
    model = Author
    template_name = 'flybookfly/author_detail.html'


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'flybookfly/comment_create_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.book_id = Book.objects.get(slug=self.kwargs['slug']).id
        return super().form_valid(form)


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'flybookfly/comment_update_form.html'
    success_url = reverse_lazy('index')


class CommentDelete(DeleteView):
    model = Comment
    template_name = 'flybookfly/comment_delete_form.html'
    success_url = reverse_lazy('index')
