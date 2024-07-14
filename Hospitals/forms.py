

from django import forms
from .models import Feedback

class HospitalSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
