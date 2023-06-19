from django import forms
from .models import Form

class StudentForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ("firstname", "lastname")