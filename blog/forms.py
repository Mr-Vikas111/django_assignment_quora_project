from django import forms
from .models import *
from django.core.exceptions import ValidationError


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionData
        fields = ['question']

class QuestionAnswerForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswerData
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        }