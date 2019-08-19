from django.urls import path, include
from . import views
app_name = 'app_pw'

urlpatterns = [
	path('', views.index, name='index'),
	path('resume/', views.resume, name='resume'),
	path('subjects/', views.subjects, name='subjects'),
	path('subject/<int:subject_id>/', views.subject, name='subject'),
	path('projects/', views.projects, name='projects'),
	path('new_subject/', views.new_subject, name='new_subject'),
	path('new_homework/<int:subject_id>/', views.new_homework, name='new_homework'),
	path('delete_homework/<int:subject_id>/<int:homework_id>/', views.delete_homework, name='delete_homework'),
	path('deny/', views.deny, name='deny'),
	# path('test2/', views.test2, name='test2'),


]