from django.urls import path
from . import views

app_name = 'category'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:num>/', views.book, name='book'),
]