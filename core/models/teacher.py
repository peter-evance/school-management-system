from django.db import models
from users.models import CustomUser
from core.models.subject import Subject
from core.models.classroom import ClassRoom


class Teacher(models.Model):
    """
    Represents a teacher in a school or educational system.

    Attributes:
        user (CustomUser): The user associated with the teacher through a one-to-one relationship.
                          The user's role must be set to 'Teacher'.
        classroom (ClassRoom): The class to which the teacher is assigned, set to NULL if not assigned.
        assigned_subjects (QuerySet): Many-to-many relationship with subjects that the teacher is assigned to.
                                      Accessible through the 'teachers' reverse relation in the 'Subject' model.
        created_at (datetime): The date and time when the teacher record was created.

    Usage:
        This model is part of a School Management System and is used to store information about teachers.
        Teachers are associated with a user account, assigned to a specific class, and can be linked to
        multiple subjects. The 'assigned_subjects' field represents the subjects the teacher is responsible for.

    Note:
        Ensure that the user associated with the teacher has the role set to 'Teacher'.
    """

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, limit_choices_to={"role": "Teacher"},
    null=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    assigned_subjects = models.ManyToManyField(Subject, related_name="teachers")
    created_at = models.DateTimeField(auto_now_add=True)
