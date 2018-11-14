from django.urls import path

from . import views

urlpatterns = [
    path(r'test/', views.test, name='test'),
]