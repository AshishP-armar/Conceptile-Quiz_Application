from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, QuizSession
from django.utils.timezone import now
import random

def start_quiz(request):
    session = QuizSession.objects.create()
    request.session['session_id'] = session.id
    return render(request, 'quiz/start_quiz.html')

# def get_question(request):
#     session_id = request.session.get('session_id')
#     if not session_id:
#         return redirect('start_quiz')

#     question = random.choice(Question.objects.all())
#     context = {
#         'question': question,
#         'options': question.options,
#         'question_id': question.id,
#     }
#     return render(request, 'quiz/question.html', context)

def get_question(request):
    # Ensure a quiz session exists
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('start_quiz')
    # Get the list of already-asked question IDs and count of displayed questions
    asked_questions = request.session.get('asked_questions', [])
    questions_shown = len(asked_questions)
    print(questions_shown)
    # Check if the user has already seen 10 questions
    if questions_shown == 10:
        return redirect('quiz_result')  # Replace with the appropriate result URL name

    # Filter out already-asked questions
    available_questions = Question.objects.exclude(id__in=asked_questions)

    # If no more questions are available but less than 10 were shown, handle gracefully
    if not available_questions.exists():
        return redirect('quiz_result')  # All questions are exhausted

    # Select a random question from the remaining pool
    question = random.choice(available_questions)

    # Add the question ID to the list of asked questions
    asked_questions.append(question.id)
    request.session['asked_questions'] = asked_questions

    # Pass the question and its options to the template
    context = {
        'question': question,
        'options': question.options,
        'question_id': question.id,
    }
    return render(request, 'quiz/question.html', context)





def submit_answer(request):
    if request.method == 'POST':
        session_id = request.session.get('session_id')
        if not session_id:
            return redirect('start_quiz')

        question_id = int(request.POST['question_id'])
        selected_option = int(request.POST['selected_option'])
        question = Question.objects.get(id=question_id)
        session = QuizSession.objects.get(id=session_id)

        session.total_questions += 1
        if question.correct_option == selected_option:
            session.correct_answers += 1
        else:
            session.incorrect_answers += 1
        session.save()

        if Question.objects.count() == session.total_questions:
            return redirect('quiz_result')

        return redirect('get_question')

def quiz_result(request):
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('start_quiz')

    session = QuizSession.objects.get(id=session_id)
    context = {
        'total': session.total_questions,
        'correct': session.correct_answers,
        'incorrect': session.incorrect_answers,
    }
    request.session.flush()
    return render(request, 'quiz/result.html', context)
