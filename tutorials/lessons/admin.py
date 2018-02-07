from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(TranslatableAdmin):
    fields = (
        'name',
        'slug',
        'course',
        'short_description',
        'content',
        'number_of',
        'is_active'
    )
    readonly_fields = ('created_at',)
    list_filter = ('course',)
    list_display = ('name', 'course', 'is_active')
    list_editable = ('is_active', )