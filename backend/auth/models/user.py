# CustomUser Model Definition
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom User Model

    Attributes:
        - `username` (CharField): User's unique username.
        - `first_name` (CharField): User's first name.
        - `last_name` (CharField): User's last name.
        - `sex` (CharField): User's gender with choices 'Male' or 'Female'.
        - `is_a_teacher` (BooleanField): Indicates if the user is a teacher.
        - `is_a_student` (BooleanField): Indicates if the user is a student.
        - `is_admin` (BooleanField): Indicates if the user is an admin.

    Additional Attributes:
        - REQUIRED_FIELDS (list): List of fields required for user creation.

    Methods:
        - assign_a_student(): Assigns the user as a student.
        - assign_a_teacher(): Assigns the user as a teacher.
        - assign_an_admin(): Assigns the user as an admin.
        - dismiss_a_student(): Dismisses the user as a student.
        - dismiss_a_teacher(): Dismisses the user as a teacher.
        - dismiss_an_admin(): Dismisses the user as an admin.
    """

    class SexChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"

    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=6, choices=SexChoices.choices)
    is_a_teacher = models.BooleanField(default=False)
    is_a_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'sex', 'is_a_teacher', 'is_a_student', 'is_admin']

    def assign_a_student(self):
        """
        Assign the user as a student.
        """
        self.is_a_student = True
        self.is_admin = False
        self.is_a_teacher = False
        self.save()

    def assign_a_teacher(self):
        """
        Assign the user as a teacher.
        """
        self.is_a_student = False
        self.is_admin = False
        self.is_a_teacher = True
        self.save()

    def assign_an_admin(self):
        """
        Assign the user as an admin.
        """
        self.is_a_student = False
        self.is_admin = True
        self.is_a_teacher = False
        self.save()

    def dismiss_a_student(self):
        """
        Dismiss the user as a student.
        """
        self.is_a_student = False
        self.save()

    def dismiss_a_teacher(self):
        """
        Dismiss the user as a teacher.
        """
        self.is_a_teacher = False
        self.save()

    def dismiss_an_admin(self):
        """
        Dismiss the user as an admin.
        """
        self.is_admin = True
        self.save()
