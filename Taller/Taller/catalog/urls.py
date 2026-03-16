from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.book_list, name="book_list"),
]

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("books/create/", views.book_create, name="book_create"),
    path("books/<int:pk>/edit/", views.book_update, name="book_update"),
    path("books/<int:pk>/delete/", views.book_delete, name="book_delete"),
]
