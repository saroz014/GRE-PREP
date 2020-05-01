import json
import random

from django.db.models import Max
from django.http import JsonResponse
from django.views.generic import ListView
from quiz_app.models import *


class QuizListView(ListView):
    queryset = Question.objects.order_by('?')
    paginate_by = 10


def check(request):
    data = json.loads(request.body.decode('utf-8'))
    if CorrectAnswer.objects.filter(question_id=data['question_id'], answer_id=data['answer_id']).exists():
        response = {'answer_id': data['answer_id']}
    else:
        answer_id = Question.objects.get(id=data['question_id']).correct_answer.answer.id
        response = {'answer_id': answer_id}
    return JsonResponse(response)

