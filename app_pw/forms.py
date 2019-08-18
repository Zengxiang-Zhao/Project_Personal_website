from django import forms
from .models import Subject, Homework

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = ['sub_name']
		labels = {'sub_name':''}

class HomeworkForm(forms.ModelForm):
	class Meta:
		model = Homework
		fields = ['topic', 'text']

