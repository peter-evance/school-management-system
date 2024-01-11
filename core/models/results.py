from django.db import models
from core.models.exams import Exam
from core.models.student import Student
from django.core.validators import MaxValueValidator


class SubjectResult(models.Model):
    """
    Django Model: SubjectResult

    Represents the result of a student in a specific exam for a particular subject.

    Attributes:
        student (ForeignKey): Reference to the Student model, indicating the student whose result is recorded.
        exam (ForeignKey): Reference to the Exam model, indicating the exam for which the result is recorded.
        marks_obtained (PositiveIntegerField): Marks obtained by the student in the exam, capped at 100.
        remarks (TextField): Additional remarks or comments regarding the student's performance, can be null.

    Example Usage:
        result_instance = SubjectResult.objects.create(student=student_instance, exam=exam_instance, marks_obtained=75, remarks='Well done!')
        print(result_instance.student)
        print(result_instance.exam)
        print(result_instance.marks_obtained)
        print(result_instance.remarks)
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    remarks = models.TextField(null=True)
