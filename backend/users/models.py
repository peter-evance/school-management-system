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
        
    class RoleChoices(models.TextChoices):
        TEACHER = "Teacher"
        STUDENT = "Student"
        ADMIN = "Admin"
        
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=6, choices=SexChoices.choices)
    role = models.CharField(max_length=10, choices=RoleChoices.choices)


    REQUIRED_FIELDS = ['first_name', 'last_name', 'sex','role']
    
    def get_full_name(self):
        """Return the full name"""
        return f"{self.first_name} {self.last_name}"
    
    def get_role(self):
        return self.get_role_display()

    def get_users_by_role(self, role):
        return CustomUser.objects.filter(role=role)

    def __str__(self):
        return self.get_full_name()

    
    
    
