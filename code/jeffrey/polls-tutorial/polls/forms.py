from django import forms

class QuestionForm(forms.Form):
    your_name = forms.CharField(label='Your question', max_length=100)