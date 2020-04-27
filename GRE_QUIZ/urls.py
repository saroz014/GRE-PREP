from django.contrib import admin
from django.urls import path
from quiz_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', QuizListView.as_view(), name='quiz-list'),
    path('check/', check, name='check-answer'),
]
