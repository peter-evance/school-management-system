from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


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

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "sex",
        "role",
        "username",
        "is_approved",
        "address",
    ]
    USERNAME_FIELD = "email"

    @property
    def get_full_name(self):
        """Return the full name"""
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def get_role(self):
        return self.get_role_display()

    def get_users_by_role(self, role):
        return CustomUser.objects.filter(role=role)

    def approve_user(self):
        self.is_approved = True
        self.save()
        self.send_approval_email()

    def send_approval_email(self):
        try:
            subject = "Your account has been approved"
            template = "approval_email.html"
            context = {"recipient_name": self.first_name.capitalize()}

            html_message = render_to_string(template, context)
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [self.email]

            send_mail(
                subject, None, from_email, recipient_list, html_message=html_message
            )

            print(f"Approval email sent to {self.email}.")
        except Exception as e:
            print(f"Failed to send approval email to {self.email}: {e}")

    def notify_admins_on_registration(self):
        try:
            # Filter all admin users except the current user
            admins = CustomUser.objects.filter(
                role=self.RoleChoices.ADMIN, is_approved=True
            ).exclude(id=self.id)
            admin_emails = admins.values_list("email", flat=True)

            # Create notifications for each admin
            for admin in admins:
                Notification.objects.create(
                    user=admin,
                    subject=f"New User Registration: {self.get_full_name}",
                    message=f"A new user with username '{self.username}' has registered on the platform.",
                )

            subject = f"New User Registration: {self.username}"
            template = "registration_notification.html"
            from_email = settings.DEFAULT_FROM_EMAIL
            context = {
                "recipient_name": self.get_full_name,
                "email": self.email,
                "user_role": self.role,
            }

            html_message = render_to_string(template, context)
            # Send email to admin users
            send_mail(
                subject,
                None,
                from_email,
                admin_emails,
                html_message=html_message,
            )

            # print(f"Notification email sent to {len(admin_emails)} admins.")
        except Exception as e:
            print(f"Failed to send registration notification email: {e}")

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


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def mark_as_read(self):
        self.read = True
        self.save()
