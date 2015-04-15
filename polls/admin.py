# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]



admin.site.register(Choice)
admin.site.register(Question , QuestionAdmin)

