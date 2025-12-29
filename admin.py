from django.contrib import admin
from .models import Question, Choice, Submission
from django.contrib.admin import TabularInline


class ChoiceInline(TabularInline):
    model = Choice
    extra = 4


class QuestionInline(TabularInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
