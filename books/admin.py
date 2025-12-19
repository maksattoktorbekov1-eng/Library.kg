from django.contrib import admin
from .models import Book, Reviews

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author")
    readonly_fields = ("created_at",)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("book", "rating", "created_at", "updated_at")
    list_filter = ("rating", "book")
    search_fields = ("book__title", "text")
    readonly_fields = ("created_at", "updated_at")
    