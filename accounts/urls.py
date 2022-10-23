from django.urls import path
from .views import UserCreateAPIView, UserListAPIView, UserDetailAPIView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name = "accounts"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    path("login/", obtain_jwt_token, name="user_login"),
    path("refresh-token/", refresh_jwt_token, name="refresh_token"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="user_detail"),
]