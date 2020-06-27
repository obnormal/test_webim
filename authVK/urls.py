from django.contrib import admin
from django.urls import path, include
from .views import redirect_view, auth_page_view, get_friends_view

urlpatterns = [
    path('', get_friends_view),
    path('auth_page/', auth_page_view),
    path('vklogin/', redirect_view, name='vk-login'),
    path('accounts/profile/', get_friends_view),
]