from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Subject(models.Model):
	sub_name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add = True)	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.sub_name

class Homework(models.Model):
	sub_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
	topic = models.CharField(max_length=200, default='')
	text = RichTextField(config_name='my_config')
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.topic

class Project(models.Model):
	pro_name = models.CharField(max_length=200)
	text = RichTextField(config_name='my_config')
	date_added= models.DateTimeField(auto_now_add = True)	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.pro_name
