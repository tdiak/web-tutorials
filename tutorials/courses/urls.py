from django.conf.urls import url

from .views import categories, lessons

urlpatterns = [
    url(r'course/(?P<slug>[-\w]+)/$', lessons, name="lessons"),
    url(r'(?P<slug>[-\w]+)/$', categories, name="categories"),
]