from django.db import models

# Create your models here.

class CodeSnippet(models.Model):

	code = models.TextField()
	author = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')


class Code(models.Model):
	code_snippet = models.TextField()
	author = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	title = models.CharField(max_length = 100)

	def __str__(self):
		return self.title + " by " + self.author
