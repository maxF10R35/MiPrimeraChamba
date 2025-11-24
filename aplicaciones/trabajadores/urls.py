from django.urls import path
from . import views

urlpatterns = [
    path('home_t/', views.home, name='home_t'),
]