from django.db import models
from datetime import timedelta
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.choices import ExamType
from core.models.subject import Subject


class Exam(models.Model):
    exam_type = models.CharField(choices=ExamType.choices, max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(
        validators=[
            MaxValueValidator(
                limit_value=timedelta(hours=3),
                message="Duration should not exceed 3 hours.",
            )
        ]
    )
    max_marks = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(
                limit_value=100, message="Maximum marks should not exceed 100."
            ),
        ]
    )
    instructions = models.TextField(null=True)
