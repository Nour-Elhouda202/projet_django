from django.contrib import admin
from .models import SubTitle, Image

class ImageInline(admin.TabularInline):  # أو admin.StackedInline
    model = SubTitle.images.through  # استخدام through للتعامل مع العلاقة ManyToMany
    extra = 1  # عدد الحقول الإضافية التي تظهر في واجهة الإدارة

@admin.register(SubTitle)
class SubTitleAdmin(admin.ModelAdmin):
    list_display = ('subtitle_title', 'main_title')
    inlines = [ImageInline]  # إضافة Inline لإدارة الصور

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'uploaded_at')