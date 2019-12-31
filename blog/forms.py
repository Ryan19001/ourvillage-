from django import forms
from .models import Quest2Check

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea
    )

class CheckIfFromForm(forms.Form):

    answer = forms.CharField(max_length=25)
