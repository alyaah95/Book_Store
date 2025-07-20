from django.contrib import admin
from .models import Book,Author,Category,ISBN


class BookAdminCustom(admin.ModelAdmin):
    list_display=('title','rate','views','author')
    list_filter=['title','rate','category']

class BookInline(admin.StackedInline):
    model=Book
    extra=3

class AuthorAdminCustom(admin.ModelAdmin):
    inlines = [BookInline]



# Register your models here.
admin.site.register(Author,AuthorAdminCustom)
admin.site.register(Category)
admin.site.register(Book,BookAdminCustom)
admin.site.register(ISBN)


