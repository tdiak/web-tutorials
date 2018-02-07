# coding=utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from courses.models import Course


class Lesson(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(verbose_name="Nazwa", max_length=100),
        short_description=models.TextField(verbose_name="Opis", max_length=250),
        slug=models.SlugField(verbose_name="Adres url"),
        content=RichTextField(verbose_name="Treść")
    )
    course = models.ForeignKey(Course, verbose_name="Kurs")
    number_of = models.PositiveIntegerField(verbose_name="Numer lekcji")
    created_at = models.DateTimeField(verbose_name="Data utworzenia", auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Aktywny", default=False)

    class Meta:
        verbose_name = "Lekcja"
        verbose_name_plural = "Lekcje"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_lesson', args=[self.course.slug, self.slug])