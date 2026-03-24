from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
]