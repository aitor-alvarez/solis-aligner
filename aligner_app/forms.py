from django import forms
from .models import Transcript

class TranscriptForm(forms.ModelForm):
    class Meta:
        model = Transcript
        fields = ('transcript_name', 'transcript_directory', 'corpus')
        widgets={
		'transcript_directory' : forms.ClearableFileInput(attrs={'multiple': True}),

		}