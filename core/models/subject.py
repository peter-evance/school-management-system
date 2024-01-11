from django.db import models
from core.models.classroom import ClassRoom
from core.choices import *


class Subject(models.Model):
    """
    Represents a subject in a school or educational system.

    Attributes:
        title (str): The title of the subject, chosen from predefined choices.
        code (str): The code assigned to the subject, chosen from predefined choices.
        class_room (ClassRoom): The class associated with the subject through a foreign key relationship.
        added_at (datetime): The date and time when the subject record was created.

    Meta:
        unique_together (list): Ensures uniqueness for the combination of title, code, and class_room.

    Usage:
        This model is part of a School Management System and is used to store information about
        subjects offered in different classes. The unique_together constraint ensures that within
        a specific class, each subject has a distinct title and code.

    Note:
        The choices for 'title' and 'code' should be defined in the SubjectTitleChoices and SubjectCodeChoices enums.
    """

    title = models.CharField(max_length=30, choices=SubjectTitleChoices.choices)
    code = models.CharField(max_length=10, choices=SubjectCodeChoices.choices)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["title", "code", "class_room"]

    def __str__(self):
        return f"{self.title}"
