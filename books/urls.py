from books.apps import BooksConfig
from django.urls import path
from books.views import BookCreateAPIView, BooksListAPIView, \
    BookRetrieveAPIView, BookUpdateAPIView, BookDestroyAPIView

app_name = BooksConfig.name

urlpatterns = [
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
    path('', BooksListAPIView.as_view(), name='books_list'),
    path('<int:pk>/', BookRetrieveAPIView.as_view(), name='book_get'),
    path('<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDestroyAPIView.as_view(), name='book_delete'),
]
