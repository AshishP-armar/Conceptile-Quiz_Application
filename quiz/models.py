from django.db import models

class Question(models.Model):
    text = models.TextField()
    options = models.JSONField()  # Format: {"1": "Option A", "2": "Option B", ...}
    correct_option = models.IntegerField()

    def __str__(self):
        return self.text


class QuizSession(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"Session {self.id} - {self.start_time}"
