from books.apps import BooksConfig
from django.urls import path
from books.views import BookCreateAPIView, BookListAPIView, \
    BookRetrieveAPIView, BookUpdateAPIView, BookDestroyAPIView

app_name = BooksConfig.name

urlpatterns = [
    path('books/create/', BookCreateAPIView.as_view(), name='book_create'),
    path('books/', BookListAPIView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookRetrieveAPIView.as_view(), name='book_get'),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDestroyAPIView.as_view(), name='book_delete'),
]
