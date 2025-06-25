from django import forms
from .models import SurveyResponse

class DynamicSurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)

        for question in questions:
            field_name = f"question_{question.id}"
            if question.question_type == 'file':
                self.fields[field_name] = forms.FileField(label=question.text, required=False)
            elif question.question_type == 'mcq':
                choices = [(choice.id, choice.text) for choice in question.choices.all()]
                self.fields[field_name] = forms.ChoiceField(
                    label=question.text,
                    choices=choices,
                    widget=forms.RadioSelect,
                    required=False
                )
            else:
                self.fields[field_name] = forms.CharField(label=question.text, required=False)
