from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    
    list_display = (
        "title",
        "author",
        "price",
        "stock_count",
        "published_date",
        "is_available",
    )

    
    search_fields = ("title", "author")

    
    list_filter = ("published_date", "is_available")

    
    ordering = ("-published_date", "title")

   
    readonly_fields = ("price", "published_date")