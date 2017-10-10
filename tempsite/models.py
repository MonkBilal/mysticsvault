from django.db import models
from django.utils import timezone


class Post(models.Model):
	"""docstring for Post"""
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length =200)
	text = models.TextField()
	created_date =models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments')
	user = models.CharField(max_length=250)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField()
	def approved(self):
		self.approved =True
		self.save()

	def __str__(self):
		return self.user


						