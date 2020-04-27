from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.answer_text


class CorrectAnswer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='correct_answer')
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer.answer_text
