from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import get_language

from courses.models import Course, CourseCategory
from lessons.models import Lesson


def categories(request, slug):
    courses = Course.objects.filter(is_active=True, translations__language_code=get_language())
    categories = CourseCategory.objects.filter(is_active=True, translations__language_code=get_language())
    try:
        current_category = CourseCategory.objects.get(translations__slug=slug, translations__language_code=get_language())
    except Exception:
        try:
            current_category = CourseCategory.objects.get(translations__slug=slug)
            return redirect(current_category.get_absolute_url())
        except Exception:
            raise Http404("Category does not exists")

    return render(request, 'courses.html', {
        'nav_items': categories,
        'current_category': current_category,
        'current_courses': courses.filter(category__translations__slug=slug)
    })


def lessons(request, slug):
    try:
        course = Course.objects.get(translations__slug=slug, translations__language_code=get_language())
    except Exception:
        try:
            course = Course.objects.get(translations__slug=slug)
            return redirect(course.get_absolute_url())
        except Exception:
            raise Http404("Course does not exists")

    lessons_list = Lesson.objects.filter(course=course,
                                         translations__language_code=get_language()).order_by('number_of')
    return render(request, 'course.html', {
        'nav_items': lessons_list,
        'course': course
    })
