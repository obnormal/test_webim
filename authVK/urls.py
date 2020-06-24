from django.contrib import admin
from django.urls import path, include
from .views import redirect_view, main_page_view

urlpatterns = [
    path('', main_page_view),
    path('vklogin/', redirect_view, name='vk-login'),
]