# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_by', models.PositiveIntegerField(verbose_name='Kolejno\u015b\u0107')),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktywny')),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kursy',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_by', models.PositiveIntegerField(verbose_name='Kolejno\u015b\u0107')),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktywny')),
            ],
            options={
                'verbose_name': 'Kategoria kursu',
                'verbose_name_plural': 'Kategorie kurs\xf3w',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CourseCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('slug', models.SlugField(verbose_name='Adres url')),
                ('description', models.TextField(max_length=250, verbose_name='Opis')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='courses.CourseCategory')),
            ],
            options={
                'managed': True,
                'db_table': 'courses_coursecategory_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Kategoria kursu Translation',
            },
        ),
        migrations.CreateModel(
            name='CourseTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('slug', models.SlugField(verbose_name='Adres url')),
                ('description', models.TextField(max_length=250, verbose_name='Opis')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='courses.Course')),
            ],
            options={
                'managed': True,
                'db_table': 'courses_course_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Kurs Translation',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseCategory', verbose_name='Kategoria'),
        ),
        migrations.AlterUniqueTogether(
            name='coursetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='coursecategorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]