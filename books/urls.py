from books.apps import BooksConfig
from django.urls import path
from books.views import BookCreateAPIView, BooksListAPIView, \
    BookRetrieveAPIView, BookUpdateAPIView, BookDestroyAPIView

app_name = BooksConfig.name

urlpatterns = [
    path('book/create/', BookCreateAPIView.as_view(), name='book_create'),
    path('books/', BooksListAPIView.as_view(), name='books_list'),
    path('book/<int:pk>/', BookRetrieveAPIView.as_view(), name='book_get'),
    path('book/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDestroyAPIView.as_view(), name='book_delete'),
]
