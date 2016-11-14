from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        pass
    def popular(self):
        pass

class Question(models.Model):
    object = QuestionManager()
    title = models.CharField(max_length=1024)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name='user-author')
    likes = models.ManyToManyField(User, related_name='user-likes')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, related_name='question-answer')
    author = models.ForeignKey(User)