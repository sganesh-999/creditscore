from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=225)
    question_score = models.FloatField(default=180)
    def __str__(self) -> str:
        return self.text

class Choice(models.Model):
    text = models.CharField(max_length=225)
    question = models.ForeignKey(Question,related_name='choices',on_delete=models.CASCADE)
    choice_score = models.FloatField(default=45)
    def __str__(self) -> str:
        return self.text

    
