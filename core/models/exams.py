from django.db import models
from datetime import timedelta
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.choices import ExamType
from core.models.subject import Subject


class Exam(models.Model):

    """
    Django Model: Exam

    Represents an exam with specific attributes.

    Attributes:
        exam_type (CharField): Type of the exam, chosen from predefined choices.
        subject (ForeignKey): Reference to the Subject model, indicating the subject of the exam.
        scheduled_date (DateTimeField): Date and time when the exam is scheduled, automatically set to the current time on creation.
        duration (DurationField): Duration of the exam, limited to a maximum of 3 hours.
        max_marks (PositiveIntegerField): Maximum marks achievable in the exam, capped at 100.
        instructions (TextField): Additional instructions for the exam, can be null.

    Notes:
        - 'choices' module is imported from 'core.choices'.
        - 'Subject' model is imported from 'core.models.subject'.
        - Validators are used to enforce constraints on 'duration' and 'max_marks'.

    Example Usage:
        exam_instance = Exam.objects.create(exam_type='...', subject=subject_instance, duration=timedelta(hours=2), max_marks=80)
        print(exam_instance.exam_type)
        print(exam_instance.subject)
        print(exam_instance.scheduled_date)
        print(exam_instance.duration)
        print(exam_instance.max_marks)
        print(exam_instance.instructions)
    """

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
