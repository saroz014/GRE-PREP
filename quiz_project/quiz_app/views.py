from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question, Answer, Correct

# Create your views here.

def index(request):
    return render(request, 'quiz_app/index.html')

def next(request):
    latest_question_list = Question.objects.order_by('pub_date')[:]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quiz_app/next.html', context)

def check(request, question_id):
    selected_choice = request.POST['answer']
    correct_choice = Correct.objects.get(pk=question_id)
    selected_choice = str(selected_choice)
    correct_choice = str(correct_choice)

    if selected_choice == correct_choice:
        return render(request, 'quiz_app/correct.html')

    else:
        return render(request, 'quiz_app/incorrect.html')
