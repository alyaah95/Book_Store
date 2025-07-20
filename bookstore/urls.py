from django.urls import path
from .views import  show_book, edit_book, delete_book, list_books,home,create_book

app_name="bookstore"

urlpatterns = [
    path("create-book",create_book,name="create-book"),
    path("show-book/<int:book_id>",show_book,name="show-book"),
    path("edit-book/<int:book_id>",edit_book,name="edit-book"),
    path("delete-book/<int:book_id>",delete_book,name="delete-book"),
    path("list-books",list_books,name="list-books"),
    path("",home,name="home")
]