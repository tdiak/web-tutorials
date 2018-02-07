from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import translation
from django.utils.translation import get_language

from courses.models import Course, CourseCategory
from lessons.models import Lesson


def index(request):
    courses = Course.objects.filter(is_active=True, translations__language_code=get_language()).order_by('translations__name')
    categories = CourseCategory.objects.filter(is_active=True, translations__language_code=get_language()).order_by('translations__name')
    lessons = Lesson.objects.filter(is_active=True, translations__language_code=get_language()).order_by('-created_at')
    lessons = lessons if lessons.count() < 12 else lessons[:12]
    return render(request, 'index.html', {
        'nav_items': courses,
        'categories': categories,
        'lessons': lessons
    })


def lang(request, lang):
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    user_language = lang
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return response