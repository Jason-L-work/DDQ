from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Survey, Question, SurveyResponse, Answer
from .forms import DynamicSurveyForm

def index(request):
    surveys = Survey.objects.filter(active=True)  # Only show active surveys
    return render(request, 'index.html', {'surveys': surveys})

@login_required
def submit_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id, active=True)
    questions = survey.questions.all()

    if request.method == 'POST':
        form = DynamicSurveyForm(request.POST, request.FILES, questions=questions)
        if form.is_valid():
            response = SurveyResponse.objects.create(user=request.user, survey=survey)
            for question in questions:
                field_name = f'question_{question.id}'
                answer_data = form.cleaned_data.get(field_name)

                if question.question_type == 'file':
                    Answer.objects.create(response=response, question=question, file_answer=answer_data)
                elif question.question_type == 'mcq':
                    if answer_data:
                        choice = question.choices.get(id=int(answer_data))
                        Answer.objects.create(response=response, question=question, text_answer=choice.text)
                    else:
                        Answer.objects.create(response=response, question=question, text_answer='')
                else:
                    Answer.objects.create(response=response, question=question, text_answer=answer_data)
            return redirect('success')
    else:
        form = DynamicSurveyForm(questions=questions)

    return render(request, 'submit_survey.html', {'form': form, 'survey': survey})

def success(request):
    return render(request, 'success.html')

def survey_answers_view(request):
    return render(request, 'survey_answers.html')
