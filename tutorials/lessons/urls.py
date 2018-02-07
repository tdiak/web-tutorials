from django.conf.urls import url

from .views import search, get_lesson

urlpatterns = [
    url(r'search/$', search, name="search"),
    url(r'(?P<course_slug>[-\w]+)/(?P<lesson_slug>[-\w]+)/$', get_lesson, name="get_lesson"),
]