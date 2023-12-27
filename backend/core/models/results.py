from django.db import models
from core.models.exams import Exam
from core.models.student import Student
from django.core.validators import MaxValueValidator


class SubjectResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    remarks = models.TextField(null=True)
