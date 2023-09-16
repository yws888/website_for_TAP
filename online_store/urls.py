from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("items/<int:id>/", views.detail, name="detail"),
]