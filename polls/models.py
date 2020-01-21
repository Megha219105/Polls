from django.db import models
import datetime

from django.utils import timezone

# Create models for the apps question and choice

class Question(models.Model):
	question_text = models.CharField(max_length =200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.question_text
		
	#method a customized method
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	#the foreign key will allow to use related object manager in Django!
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text
		
	
	

