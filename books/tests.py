from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.ru',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        self.user.set_password('0000')
        self.user.save()

        self.book = Book.objects.create(
            title='test_course',
            author='test',
            ISBN='978-3-12732-320-7'
        )
        self.book.save()

    def test_create_book(self):
        """Создание книги"""
        data = {'title': 'test_course', 'author': 'test', 'ISBN': '978-3-12732-320-7'}
        response = self.client.post('/books/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_book(self):
        """Тестирование получения списка книг"""
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_lesson(self):
        """Получение книги"""
        response = self.client.get(f'/books/{self.book.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        """Удаление книги"""
        response = self.client.delete(f'/books/{self.book.pk}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
