from django.db import models
from core.models.classroom import ClassRoom
from users.models import CustomUser
from core.choices import *
from core.models.subject import Subject


class Student(models.Model):
    """
    Represents a student in a school or educational system.

    Attributes:
        user (CustomUser): The user associated with the student through a one-to-one relationship.
                          The user's role must be set to 'Student'.
        classroom (ClassRoom): The class to which the student is assigned, set to NULL if not assigned.
        enrolled_subjects (QuerySet): Many-to-many relationship with subjects in which the student is enrolled.
                                      Accessible through the 'enrolled_students' reverse relation in the 'Subject' model.
        created_at (datetime): The date and time when the student record was created.

    Properties:
        registration_number (str): A unique registration number generated based on the student's creation timestamp and ID.

    Usage:
        This model is part of a School Management System and is used to store information about students.
        Students are associated with a user account, assigned to a specific class, and can be enrolled in multiple subjects.
        The 'registration_number' property provides a unique identifier for each student based on creation time and ID.

    """

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, limit_choices_to={"role": "Student"},
    null=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    enrolled_subjects = models.ManyToManyField(
        Subject, related_name="student"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def registration_number(self):
        """
        Generates a unique registration number for the student.

        The registration number is a combination of the student's creation timestamp and ID.

        Returns:
            str: The unique registration number.
        """
        registration_number = self.created_at.strftime("%m%d-%Y-%H%M%S") + str(self.id)
        return registration_number[::-1]
