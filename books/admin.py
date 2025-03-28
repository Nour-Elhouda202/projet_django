from django.contrib import admin  
from .models import Book  
from django.utils.html import format_html
@admin.register(Book)
class AlgeriaBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_cover')
    
    def display_cover(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}"  />', obj.cover_image)
        return ""
    display_cover.short_description = 'Couverture'