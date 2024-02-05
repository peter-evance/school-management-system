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

    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=6, choices=SexChoices.choices)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    email = models.EmailField(max_length=40, unique=True)
    role = models.CharField(max_length=10, choices=RoleChoices.choices)
    is_approved = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["first_name", "last_name", "sex", "role", "username", "is_approved", "address"]
    USERNAME_FIELD = 'email'

    @property
    def get_full_name(self):
        """Return the full name"""
        return f"{self.first_name} {self.last_name}"

    def get_role(self):
        return self.get_role_display()

    def get_users_by_role(self, role):
        return CustomUser.objects.filter(role=role)

    def __str__(self):
        return self.get_full_name


class ProfileImage(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_images/")
    thumbnail = models.ImageField(
        upload_to="profile_thumbnails/", null=True, editable=False
    )

    def __str__(self):
        return f"Profile Image for {self.user.username}"
