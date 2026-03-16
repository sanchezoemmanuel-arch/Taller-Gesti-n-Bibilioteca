from django.urls import path
from . import views

app_name = "loans"

urlpatterns = [
    path("", views.loan_list, name="loan_list"),
]

urlpatterns = [
    path("mis-prestamos/", views.my_loans, name="my_loans"),
    path("", views.loan_list, name="loan_list"),
    path("create/", views.loan_create, name="loan_create"),
    path("<int:pk>/return/", views.loan_return, name="loan_return"),
]
