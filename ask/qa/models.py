from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    object = QuestionManager()
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    answer = models.ForeignKey(User)
    likes = models.ManyToManyField(User)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

class QuestionManager(models.Manager):
    def new(self):
        pass
    def popular(self):
        pass