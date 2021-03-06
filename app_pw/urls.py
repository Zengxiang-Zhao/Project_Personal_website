from django.urls import path, include
from . import views
app_name = 'app_pw'

urlpatterns = [
	path('', views.index, name='index'),
	path('resume/', views.resume, name='resume'),
	path('subjects/', views.subjects, name='subjects'),
	path('subject/<int:subject_id>/', views.subject, name='subject'),
	path('new_subject/', views.new_subject, name='new_subject'),
	path('projects/', views.projects, name='projects'),
	path('new_project/', views.new_project, name='new_project'),
	path('project/<int:project_id>', views.project, name='project'),
	path('edit_project/<int:project_id>', views.edit_project, name='edit_project'),
	path('delete_project/<int:project_id>', views.delete_project, name='delete_project'),
	path('new_homework/<int:subject_id>/', views.new_homework, name='new_homework'),
	path('homework/<int:subject_id>/<int:homework_id>/', views.homework, name='homework'),
	path('edit_homework/<int:subject_id>/<int:homework_id>/',views.edit_homework,name='edit_homework'),
	path('delete_homework/<int:subject_id>/<int:homework_id>/', views.delete_homework, name='delete_homework'),
	path('deny/', views.deny, name='deny'),
	path('test/',views.test,name='test'),


]