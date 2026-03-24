from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form),
    path('lowcie/', views.low_cie_students),
]