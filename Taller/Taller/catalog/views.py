from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book


def is_staff(user):
    return user.is_staff


def book_list(request):
    query = request.GET.get("q", "")
    books = Book.objects.all()
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        ).distinct()
    paginator = Paginator(books, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "query": query}
    return render(request, "catalog/book_list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    last_loan = book.loans.filter(is_active=False).order_by("-end_date").first()
    context = {"book": book, "last_loan": last_loan}
    return render(request, "catalog/book_detail.html", context)


@login_required
@user_passes_test(is_staff)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado correctamente.")
            return redirect("catalog:book_list")
    else:
        form = BookForm()
    return render(request, "catalog/book_form.html", {"form": form})


@login_required
@user_passes_test(is_staff)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado.")
            return redirect("catalog:book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "catalog/book_form.html", {"form": form, "book": book})


@login_required
@user_passes_test(is_staff)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Libro eliminado.")
        return redirect("catalog:book_list")
    return render(
        request,
        "catalog/book_confirm_delete.html",
        {"book": book},
    )
