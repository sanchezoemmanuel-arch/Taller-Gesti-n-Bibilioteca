from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoanForm
from .models import Loan


def is_staff(user):
    return user.is_staff


@login_required
def my_loans(request):
    loans = Loan.objects.select_related("book").filter(
        user=request.user, is_active=True
    )
    return render(request, "loans/my_loans.html", {"loans": loans})


@login_required
@user_passes_test(is_staff)
def loan_list(request):
    loans = Loan.objects.select_related("book", "user").all()
    return render(request, "loans/loan_list.html", {"loans": loans})


@login_required
@user_passes_test(is_staff)
def loan_create(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save()
            messages.success(request, "Préstamo creado correctamente.")
            return redirect("loans:loan_list")
    else:
        form = LoanForm()
    return render(request, "loans/loan_form.html", {"form": form})


@login_required
@user_passes_test(is_staff)
def loan_return(request, pk):
    loan = get_object_or_404(
        Loan.objects.select_related("book", "user"), pk=pk
    )
    if request.method == "POST":
        loan.mark_returned()
        messages.success(request, "Devolución registrada correctamente.")
        return redirect("loans:loan_list")
    return render(
        request,
        "loans/loan_return_confirm.html",
        {"loan": loan},
    )
