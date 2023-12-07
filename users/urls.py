from django.urls import path
from users.apps import UsersConfig
from users.views import UserListAPIView, UserRetrieveAPIView, UserCreateAPIView, \
    UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users/list/', UserListAPIView.as_view(), name='users'),
    path('user/register/', UserCreateAPIView.as_view(), name='user_register'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user'),
    path('user/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user_delete'),
]
