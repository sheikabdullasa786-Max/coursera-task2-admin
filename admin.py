from django.contrib import admin

from .models import (
    Course,
    Lesson,
    Question,
    Choice,
    Submission,
    Enrollment,
    Instructor
)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'course')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'score')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name',)


