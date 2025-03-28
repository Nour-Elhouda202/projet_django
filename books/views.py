from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator

def books(request):
    
    books = Book.objects.all().order_by('title')
    
  
    paginator = Paginator(books, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'books/books.html', context)

def book(request, book_id):
  
    book = Book.objects.get(id=book_id)
    
    context = {
        'book': book,
    }
    return render(request, 'books/book.html', context)