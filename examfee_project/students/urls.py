from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    path('delete-unpaid/', views.delete_unpaid, name='delete_unpaid'),
]
