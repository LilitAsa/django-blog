from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("categories/", views.categories),
    path("categories/<int:cat_id>/", views.categories_by_id)
]
