from django.db import models
from django.contrib.auth.models import User


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
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		if len(self.text) > 50:
			return self.text[:50] + ' ...'
		else:
			return self.text

class Project(models.Model):
	pro_name = models.CharField(max_length=200)
	text = models.TextField()
	date_added= models.DateTimeField(auto_now_add = True)	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		if len(self.text) > 50:
			return self.text[:50] + ' ...'
		else:
			return self.text
