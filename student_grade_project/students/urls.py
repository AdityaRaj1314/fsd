from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update-grade/', views.update_grade, name='update_grade'),
]
