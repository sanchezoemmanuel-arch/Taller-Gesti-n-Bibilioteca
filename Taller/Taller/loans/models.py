from django.conf import settings
from django.db import models, transaction
from django.utils import timezone
from catalog.models import Book


class Loan(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="loans"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="loans",
    )
    start_date = models.DateField(default=timezone.localdate)
    due_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"Préstamo de {self.book} a {self.user}"

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.is_active:
            existe_activo = Loan.objects.filter(
                book=self.book, is_active=True
            ).exclude(pk=self.pk).exists()
            if existe_activo:
                raise ValidationError("Este libro ya está prestado.")

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        if self.is_active:
            if self.book.is_available:
                self.book.is_available = False
                self.book.save()
        else:
            if not self.book.is_available:
                self.book.is_available = True
                self.book.save()

    @transaction.atomic
    def mark_returned(self, return_date=None):
        if return_date is None:
            return_date = timezone.localdate()
        self.end_date = return_date
        self.is_active = False
        self.save()
        if self.end_date and self.end_date > self.due_date:
            late_days = (self.end_date - self.due_date).days
            Fine.objects.create(
                loan=self,
                late_days=late_days,
                fine_amount=late_days * 1000,
            )


class Fine(models.Model):
    loan = models.OneToOneField(
        Loan, on_delete=models.CASCADE, related_name="fine"
    )
    late_days = models.PositiveIntegerField()
    fine_amount = models.PositiveIntegerField()

    def __str__(self):
        return f"Multa {self.fine_amount} por {self.late_days} días de retraso"
