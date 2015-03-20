from django.db import models
import datetime
# Create your models here.

class SubQuestion(models.Model):
	question_text=models.CharField(max_length=200)
	question_marks=models.IntegerField(default=0)
	subject=models.ForeignKey('Subject')
	image=models.ImageField()
	question_difficulty=models.CharField(max_length=10)
	#unit
	section=models.CharField(max_length=5)
	def __str__(self):
		return self.question_text

class Subject(models.Model):
	subject_name=models.CharField(max_length=40)
	subject_code=models.CharField(max_length=10)
	semester=models.IntegerField(default=0)
	branch=models.CharField(max_length=10)
	def __str__(self):
		return self.subject_name

class QuestionPaper(models.Model):
	subject=models.ForeignKey('Subject')
	main_question=models.ForeignKey('MainQuestion')
	max_marks=models.IntegerField(default=0)
	date_of_exam=models.DateTimeField()
	teacher_name=models.CharField(max_length=30)
	def __str__(self):
		return self.subject.subject_name

class MainQuestion(models.Model):
	sub_question=models.ForeignKey('SubQuestion')
	def __str__(self):
		return self.sub_question.question_text
