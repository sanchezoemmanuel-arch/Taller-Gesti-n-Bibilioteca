from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "isbn", "is_available"]

    def clean_isbn(self):
        isbn = self.cleaned_data["isbn"]
        if not isbn.isdigit() or len(isbn) != 13:
            raise forms.ValidationError(
                "El ISBN debe tener exactamente 13 dígitos numéricos."
            )
        return isbn
