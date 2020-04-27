from django.db import models
from datetime import datetime

# Create your models here.

# Store the Question
class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

# Store the Answers
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.answer_text

# Store the Correct answer
class Correct(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_text = models.CharField(max_length=200)

    def __str__(self):
        return self.correct_text
