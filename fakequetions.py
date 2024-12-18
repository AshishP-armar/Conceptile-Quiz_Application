import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_app_project.settings')  # Replace 'quiz_app_project.settings' with your actual settings module
django.setup()

from quiz.models import Question  # Update 'quiz_app' with your app name

def add_questions():
    questions = [
        {
            "text": "What is the capital of India?",
            "options": {"1": "Mumbai", "2": "Delhi", "3": "Chennai", "4": "Kolkata"},
            "correct_option": 2
        },
        {
            "text": "What is the capital of Madhya Pradesh?",
            "options": {"1": "Bhopal", "2": "Indore", "3": "Jabalpur", "4": "Gwalior"},
            "correct_option": 1
        },
        {
            "text": "Who developed Python?",
            "options": {"1": "Guido van Rossum", "2": "Dennis Ritchie", "3": "James Gosling", "4": "Bjarne Stroustrup"},
            "correct_option": 1
        },
        {
            "text": "What is the output of `print(2**3)` in Python?",
            "options": {"1": "6", "2": "8", "3": "9", "4": "12"},
            "correct_option": 2
        },
        {
            "text": "What is the capital of Rajasthan?",
            "options": {"1": "Udaipur", "2": "Jodhpur", "3": "Jaipur", "4": "Ajmer"},
            "correct_option": 3
        },
        {
            "text": "Which keyword is used for function definition in Python?",
            "options": {"1": "function", "2": "define", "3": "def", "4": "lambda"},
            "correct_option": 3
        },
        {
            "text": "What is the national animal of India?",
            "options": {"1": "Elephant", "2": "Tiger", "3": "Lion", "4": "Peacock"},
            "correct_option": 2
        },
        {
            "text": "What does the `len()` function in Python return?",
            "options": {"1": "Length of a string or collection", "2": "Maximum value in a collection", "3": "Minimum value in a collection", "4": "Number of arguments"},
            "correct_option": 1
        },
        {
            "text": "What is the capital of Gujarat?",
            "options": {"1": "Ahmedabad", "2": "Vadodara", "3": "Gandhinagar", "4": "Surat"},
            "correct_option": 3
        },
        {
            "text": "Which Python library is used for data analysis?",
            "options": {"1": "NumPy", "2": "Pandas", "3": "Matplotlib", "4": "SciPy"},
            "correct_option": 2
        },
        {
            "text": "What is the capital of Maharashtra?",
            "options": {"1": "Mumbai", "2": "Nagpur", "3": "Pune", "4": "Nashik"},
            "correct_option": 1
        },
        {
            "text": "Which operator is used for floor division in Python?",
            "options": {"1": "/", "2": "//", "3": "%", "4": "**"},
            "correct_option": 2
        },
        {
            "text": "What is the capital of Uttar Pradesh?",
            "options": {"1": "Varanasi", "2": "Kanpur", "3": "Lucknow", "4": "Agra"},
            "correct_option": 3
        },
        {
            "text": "Which function is used to sort a list in Python?",
            "options": {"1": "sort()", "2": "sorted()", "3": "Both", "4": "None"},
            "correct_option": 3
        },
        {
            "text": "What is the capital of Karnataka?",
            "options": {"1": "Bangalore", "2": "Mysore", "3": "Mangalore", "4": "Belgaum"},
            "correct_option": 1
        },
        {
            "text": "What does the `break` keyword do in Python?",
            "options": {"1": "Terminates the loop", "2": "Skips the current iteration", "3": "Continues the loop", "4": "None of the above"},
            "correct_option": 1
        },
        {
            "text": "What is the capital of Tamil Nadu?",
            "options": {"1": "Coimbatore", "2": "Chennai", "3": "Madurai", "4": "Salem"},
            "correct_option": 2
        },
        {
            "text": "What is the capital of Kerala?",
            "options": {"1": "Kochi", "2": "Kozhikode", "3": "Thiruvananthapuram", "4": "Thrissur"},
            "correct_option": 3
        },
        {
            "text": "What does the `continue` keyword do in Python?",
            "options": {"1": "Terminates the loop", "2": "Skips the current iteration", "3": "Ends the function", "4": "None of the above"},
            "correct_option": 2
        },
        {
            "text": "What is the capital of Bihar?",
            "options": {"1": "Patna", "2": "Gaya", "3": "Muzaffarpur", "4": "Bhagalpur"},
            "correct_option": 1
        },
    ]

    # Add questions to the database
    for question in questions:
        Question.objects.create(
            text=question["text"],
            options=question["options"],
            correct_option=question["correct_option"]
        )

    print("Questions added successfully!")

# Run this function in Django shell or as a script
# python manage.py shell
add_questions()
