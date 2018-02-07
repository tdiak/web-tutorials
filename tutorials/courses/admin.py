from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import CourseCategory, Course

@admin.register(CourseCategory)
class CourseCategoryAdmin(TranslatableAdmin):
    fields = (
        'name',
        'slug',
        'description',
        'image',
        'order_by',
        'is_active'
    )


@admin.register(Course)
class CourseAdmin(TranslatableAdmin):
    fields = (
        'name',
        'slug',
        'category',
        'description',
        'order_by',
        'image',
        'is_active'
    )

    list_display = ('name', 'category', 'is_active')
    list_editable = ('is_active',)
