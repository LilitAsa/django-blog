from django.contrib import admin
from django.urls import path, re_path,register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")


urlpatterns = [
    path("", views.index),
    path("categories/", views.categories),
    path("categories/<int:cat_id>/", views.categories_by_id),
    path("categories/<slug:cat_slug>/", views.categories_by_slug),
    path("archive/<yyyy:year>/", views.archive)
]
