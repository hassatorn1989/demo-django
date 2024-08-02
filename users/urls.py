from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user.index'),
    path('create/', views.create, name='user.create'),
]