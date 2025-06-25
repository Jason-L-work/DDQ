from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    title = models.CharField(max_length=200, default='Anonymous')
    active = models.BooleanField(default=True)
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_file_upload = models.BooleanField(default=False, help_text="Check if this question requires a file upload.")
    
    # Add this field to distinguish question type
    MULTIPLE_CHOICE = 'mcq'
    TEXT = 'text'
    FILE = 'file'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (FILE, 'File Upload'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default=TEXT)

    def __str__(self):
        return f"{self.text} ({self.get_question_type_display()})"

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    response = models.ForeignKey(SurveyResponse, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True, null=True)
    file_answer = models.FileField(upload_to='uploads/', blank=True, null=True)
    choice_answer = models.ForeignKey(Choice, blank=True, null=True, on_delete=models.SET_NULL)
