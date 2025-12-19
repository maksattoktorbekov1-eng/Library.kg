from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm, ReviewForm
import datetime

def home(request):
    return render(request, 'books/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {"books": books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.reviews.order_by("-created_at")
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.full_clean()
            review.save()
            return redirect("book_detail", id=book.id)
    else:
        form = ReviewForm()
    return render(request, "books/book_detail.html", {"book": book, "reviews": reviews, "form": form})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form})

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/book_delete.html", {"book": book})

def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<h1>Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}</h1>")