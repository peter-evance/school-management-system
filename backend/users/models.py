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
    date_of_birth = models.DateField()
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
    
    
    # def save(self, *args, **kwargs):
    #     from core.models import Student
    #     print("HEY I AM TRIGGERED FROM THE SAVE METHOD")
    #     if not self.pk and self.role == self.RoleChoices.STUDENT:
    #         student: Student = Student.objects.create(user=self)
            
    #         print(student.get_reg_no)
            
    #     super().save(*args, **kwargs)
        

    
    
    
