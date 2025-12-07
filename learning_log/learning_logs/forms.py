from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'study_date', 'study_location', 'hours_spent']
        labels = {
            'text': '',
            'study_date': 'Date studied',
            'study_location': 'Study location',
            'hours_spent': 'Hours spent studying (in hours)',
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
            # HTML date picker
            'study_date': forms.DateInput(attrs={'type': 'date'}),
        }