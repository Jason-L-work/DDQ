from django import forms
from .models import Profile  # your Profile model

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']  # whatever fields you want to edit

