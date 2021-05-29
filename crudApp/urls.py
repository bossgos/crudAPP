from django.contrib import admin
from django.urls import path
from crudApp import views

urlpatterns = [
    path('display/', views.display, name = 'display'),
    path('new/', views.form, name = 'form'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('delete/<int:id>', views.delete, name = 'delete'),
]
