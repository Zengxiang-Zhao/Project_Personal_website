from django.shortcuts import render
from .models import Subject, Homework

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SubjectForm, HomeworkForm

from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	return render(request, 'app_pw/index.html')
@login_required
def resume(request):
	return render(request,'app_pw/resume.html')

def subjects(request):
	subjects = Subject.objects.order_by('date_added')

	context = {
		'subjects': subjects,
	}

	return render(request, 'app_pw/subjects.html', context)

def subject(request, subject_id):
	subject = Subject.objects.get(id = subject_id)
	homeworks = subject.homework_set.order_by('-date_added')
	context = {
		'subject' : subject,
		'homeworks' : homeworks,
	}

	return render(request, 'app_pw/subject.html', context)

def new_subject(request):
	if request.method != 'POST':
		form = SubjectForm()
	else:
		form = SubjectForm(request.POST)
		if form.is_valid():
			# new_subject = form.save(commit= Fasle)
			
			form.save()
			return HttpResponseRedirect(reverse('app_pw:subjects'))
	context = {'form':form}
	return render(request, 'app_pw/new_subject.html', context)


def new_homework(request,subject_id):
	subject = Subject.objects.get(id = subject_id)
	if request.method != 'POST':
		form = HomeworkForm()
	else:
		form = HomeworkForm(request.POST)
		if form.is_valid():
			new_homework = form.save(commit=False)
			new_homework.sub_name = subject
			new_homework.save()
			return HttpResponseRedirect(reverse('app_pw:subject', args=[subject_id]))

	context = {'subject':subject, 'form':form}
	return render(request, 'app_pw/new_homework.html', context)


def delete_homework(request,subject_id, homework_id):
	subject = Subject.objects.get(id = subject_id)
	homework = subject.homework_set.get(id=homework_id)
	homework.delete()

	return  HttpResponseRedirect(reverse('app_pw:subject', args=[subject_id]))



def project(request):
	return render(request, 'app_pw/project.html')
