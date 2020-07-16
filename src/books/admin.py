from django.contrib import admin
from .models import Books




class BooksAdmin(admin.ModelAdmin):
    list_display=['pk', 'name']
    list_filter = ('available',)
    search_fields=['name']
    class Meta:
        model=Books

admin.site.register(Books, BooksAdmin)