from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Question, Answer, Correct
from .forms import QuestionForm, AnswerForm

# Create your views here.

# This view displays the index page
def index(request):
    return render(request, 'quiz_app/index.html')

# This view displays the main quiz page
def next(request):
    latest_question_list = Question.objects.order_by('pub_date')[:]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quiz_app/next.html', context)

# This view checks whether the selected answer is correct by comparing the
# selected answer with corresponding correct answer
def check(request, question_id):
    selected_choice = request.POST['answer']
    correct_choice = Correct.objects.get(question=question_id)
    selected_choice = str(selected_choice)
    correct_choice = str(correct_choice)

    if selected_choice == correct_choice:
        return render(request, 'quiz_app/correct.html')

    else:
        return render(request, 'quiz_app/incorrect.html')

# Generates the Question Form and stores the provided question to the database
def add_question(request):
    if request.method == "POST":
        que_form = QuestionForm(request.POST)
        if que_form.is_valid():
            que_form.save()
            question = Question.objects.order_by('-pub_date')[0]
            return HttpResponseRedirect(reverse('quiz_app:add_answers', args=(question.id,)))
    else:
        que_form = QuestionForm()
    return render(request, 'quiz_app/add_question.html', {'que_form': que_form})

# Generates the Answer Form and stores the provided answers to the database
def add_answers(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        ans_form = AnswerForm(request.POST)
        if ans_form.is_valid():
            answer = ans_form.save(commit=False)
            for k in range(4):
                answer[k].question = question
                answer[k].save()
            return render(request, 'quiz_app/add_correct.html', {'question': question})
    else:
        ans_form = AnswerForm()
    return render(request, 'quiz_app/add_answers.html', {'ans_form': ans_form, 'question': question})

# Generates Answers to select the correct answer from and stores the selected answer to the database
def add_correct(request, id):
    if request.method == "POST":
        question = get_object_or_404(Question, id=id)
        correct_choice = request.POST['correct']
        set = Correct(question=question, correct_text=correct_choice)
        set.save()
        return render(request, 'quiz_app/index.html')

    else:
        return render(request, 'quiz_app/add_correct.html', {'question': question})
