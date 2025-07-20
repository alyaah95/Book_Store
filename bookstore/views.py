from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    
    return render(request, 'bookstore/home.html')

@login_required
def list_books(request):
    my_context={
        "books":Book.objects.all()
    }
    return render(request,'bookstore/list_books.html',context=my_context)

@permission_required('bookstore.delete_book', raise_exception=True)
def delete_book(request,**kwargs):
    book_id = kwargs.get("book_id")
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("bookstore:list-books")


def show_book(request,**kwargs):
    book_id = kwargs.get("book_id")
    book= Book.objects.get(id=book_id)
    my_context={
        "book":book
    }
    return render(request,"bookstore/show_book.html",context=my_context)

@permission_required('bookstore.add_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        book_form=BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect("bookstore:list-books")
    else:
        book_form=BookForm()

    return render(request,"bookstore/create_book.html",{"form":book_form})

@permission_required('bookstore.change_book', raise_exception=True)
def edit_book(request,**kwargs):
    book_id = kwargs.get("book_id")
    book_object = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book_form=BookForm(request.POST,instance=book_object)
        if book_form.is_valid():
            book_form.save()
            return redirect("bookstore:list-books")
    else:
        book_form=BookForm(instance=book_object)
    return render(request,"bookstore/edit_book.html",{"form":book_form,"book":book_object})
        
