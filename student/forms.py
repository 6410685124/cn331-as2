from django import forms
from subject.models import Class

class QuotaRequestForm(forms.Form):
    course_code = forms.CharField(max_length=10)
