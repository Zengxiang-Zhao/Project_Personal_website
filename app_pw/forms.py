from django import forms
from .models import Subject, Homework, Project

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = ['sub_name']
		labels = {'sub_name':''}

class HomeworkForm(forms.ModelForm):
	class Meta:
		model = Homework
		fields = ['topic', 'text']

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['pro_name', 'text']
		labels = {'pro_name':'Project name'}


