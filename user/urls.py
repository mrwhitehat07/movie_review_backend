from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from user.views import GetUser, Login, Register, UpdateProfile, ChangePassword, token_validity

urlpatterns = [
    path('obtain-token/', views.obtain_auth_token),
    path('validate-token/', token_validity),
    path('login/',Login.as_view()),
    path('register/',Register.as_view()),
    path('profile-update/<int:id>/', UpdateProfile.as_view()),
    path('change-password/<int:id>/', ChangePassword.as_view()),
    path('profile/',GetUser.as_view()),
]   