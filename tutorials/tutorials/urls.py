from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static

from tutorials import settings
from .views import index, lang

urlpatterns =  [
    url(r'^$', index, name="home"),
    url(r'lang/(?P<lang>\w+)/', lang, name="lang"),
    url(r'^course/', include('courses.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('lessons.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)