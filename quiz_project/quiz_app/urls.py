from django.urls import path
from quiz_app import views

app_name = 'quiz_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('next/', views.next, name='next'),
    path('<int:question_id>/check/', views.check, name='check'),

]
