from django import forms
from django.utils import timezone
from .models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["book", "user", "start_date", "due_date"]

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        due = cleaned_data.get("due_date")

        if start and due and due <= start:
            raise forms.ValidationError(
                "La fecha de devolución debe ser posterior a la fecha de inicio."
            )
        if start and start < timezone.localdate():
            raise forms.ValidationError(
                "La fecha de inicio no puede estar en el pasado."
            )
        return cleaned_data
