# coding=utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields


class BaseCourseModel(models.Model):
    order_by = models.PositiveIntegerField(verbose_name="Kolejność")
    is_active = models.BooleanField(verbose_name="Aktywny", default=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class CourseCategory(TranslatableModel, BaseCourseModel):
    translations = TranslatedFields(
        name=models.CharField(verbose_name="Nazwa", max_length=100),
        slug=models.SlugField(verbose_name="Adres url"),
        description=models.TextField(verbose_name="Opis", max_length=250)
    )
    image = models.ImageField(verbose_name="Zdjęcie", upload_to='categories', null=True, blank=True)

    class Meta:
        verbose_name = "Kategoria kursu"
        verbose_name_plural = "Kategorie kursów"

    def get_absolute_url(self):
        return reverse('categories', args=[self.slug])


class Course(TranslatableModel, BaseCourseModel):
    translations = TranslatedFields(
        name=models.CharField(verbose_name="Nazwa", max_length=100),
        slug=models.SlugField(verbose_name="Adres url"),
        description=RichTextField(verbose_name="Opis")
    )
    category = models.ForeignKey(CourseCategory, verbose_name="Kategoria")
    image = models.ImageField(verbose_name="Zdjęcie", upload_to='courses', null=True, blank=True)

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kursy"

    def get_absolute_url(self):
        return reverse('lessons', args=[self.slug])