from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg
# Create your views here.


def index(request):

    books = Book.objects.all().order_by("-title")

    number_of_books = books.count()

    average_rating = books.aggregate(Avg("rating"))


    return render(request, "book_outlet/index.html", {
        "books": books,
        "number_of_books": number_of_books,
        "average_rating": average_rating
    })


def book(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, "book_outlet/book_details.html", {
        "title": book.title,
        "author": book.author,
        "description": book.rating,
        "is_bestseller": book.is_bestselling,

    })
