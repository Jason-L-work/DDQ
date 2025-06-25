from django.contrib import admin
from .models import Survey, Question, SurveyResponse, Answer, Choice

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2  # show 2 blank choices by default

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'survey', 'is_file_upload', 'question_type')
    list_filter = ('survey', 'is_file_upload', 'question_type')
    inlines = [ChoiceInline]  # Add inline to manage choices for MCQ questions

@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'survey', 'submitted_at')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('response', 'question', 'text_answer', 'file_answer')
