from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('book/create/', views.BookCreate.as_view(), name='book_create_url'),
    path('book/<str:slug>/', views.BookDetail.as_view(), name='book_detail_url'),
    path('book/<str:slug>/update/', views.BookUpdate.as_view(), name='book_update_url'),
    path('book/<str:slug>/delete/', views.BookDelete.as_view(), name='book_delete_url'),
    path('book/<str:slug>/comment/', views.CommentCreate.as_view(), name='add_comment_url'),
    path('book/<str:slug>/comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='update_comment_url'),
    path('book/<str:slug>/comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='delete_comment_url'),
    path('author/<str:slug>/', views.AuthorDetail.as_view(), name='author_detail_url'),
]
