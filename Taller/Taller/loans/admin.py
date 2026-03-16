from django.contrib import admin
from .models import Loan, Fine


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "start_date", "due_date", "end_date", "is_active")
    list_filter = ("is_active", "start_date", "due_date")
    search_fields = ("book__title", "user__username")


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ("loan", "late_days", "fine_amount")
