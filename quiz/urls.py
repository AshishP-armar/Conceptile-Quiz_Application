from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('question/', views.get_question, name='get_question'),
    path('submit/', views.submit_answer, name='submit_answer'),
    path('result/', views.quiz_result, name='quiz_result'),
]
