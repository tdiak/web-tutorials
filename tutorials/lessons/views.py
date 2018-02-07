from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import get_language

from courses.models import Course
from .models import Lesson


def search(request):
    search_word = request.GET.get('search', '')
    lessons = []
    if search_word:
        vector = SearchVector('translations__name')
        query = SearchQuery(request.GET.get('search'))
        lessons = Lesson.objects.annotate(
            rank=SearchRank(vector, query)).filter(
                rank__gte=0.01,
                translations__language_code=get_language()).order_by('-rank').distinct()
    return render(request, 'search_results.html', {
        'lessons': lessons,
        'search_word': search_word,
        'nav_items': Course.objects.filter(is_active=True, translations__language_code=get_language())
    })


def get_lesson(request, course_slug, lesson_slug):

    try:
        lesson = Lesson.objects.get(translations__language_code=get_language(), course__translations__slug=course_slug,
                                    translations__slug=lesson_slug, course__translations__language_code=get_language())
    except Exception as e:
        return redirect('/')

    lessons_list = Lesson.objects.filter(course=lesson.course,
                                         translations__language_code=get_language()).order_by('number_of')
    return render(request, 'lesson.html', {
        'nav_items': lessons_list,
        'lesson': lesson
    })


