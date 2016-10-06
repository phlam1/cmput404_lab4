from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

# Create your models here.

@python_2_unicode_compatible
class Question(models.Model): # this is going to be a table
	question_text = models.CharField(max_length=200) # this going to be column/ field in the Question table
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		# want this to return true if the question was published in the last day
		return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
@python_2_unicode_compatible
class Choice(models.Model): # this is going to be a table
	queston = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
