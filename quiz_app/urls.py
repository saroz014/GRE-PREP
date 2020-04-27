from django.urls import path
from quiz_app import views

app_name = 'quiz_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('next/', views.next, name='next'),
    path('<int:question_id>/check/', views.check, name='check'),
    path('add_question', views.add_question, name='add_question'),
    path('add_answers/<int:id>/', views.add_answers, name='add_answers'),
    path('add_correct/<int:id>/', views.add_correct, name='add_correct'),
]
