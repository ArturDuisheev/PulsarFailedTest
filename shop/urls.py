from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('items/', views.ProductPulsarView.as_view()),
    path('items/<int:pk>/', views.ProductPulsarRetrieveUpdateDestroyView.as_view()),
]
