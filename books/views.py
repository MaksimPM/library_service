from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer


class BooksListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
