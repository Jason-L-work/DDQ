from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-survey/<int:survey_id>/', views.submit_survey, name='submit_survey'),
    path('survey-answers/', views.survey_answers_view, name='survey_answers'),
    path('success/', views.success, name='success'),
]






