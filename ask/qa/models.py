from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=1024)
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='user-likes')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, blank=True, null=True)