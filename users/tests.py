from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.ru',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        self.user.set_password('0000')
        self.user.save()

    def test_create_user(self):
        """Создание пользователя"""
        data = {
            'email': 'test@example.com',
        }
        response = self.client.post('/users/register/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_user(self):
        data = {
            'email': 'test@example.com',
        }
        response = self.client.get('/users/list/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        response = self.client.delete(f'/users/{self.user.pk}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
