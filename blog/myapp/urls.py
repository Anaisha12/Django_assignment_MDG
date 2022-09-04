from django.urls import path
from . import views
urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('delete/<int:id>', views.delete, name='delete'),
]