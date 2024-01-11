from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from core.models.student import Student
from core.models.teacher import Teacher
from core.models.admin import Admin

from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_a_profile(sender, instance, **kwargs):
    """
    Django Signal Receiver: create_a_profile

    Signal receiver triggered after a CustomUser instance is saved. Creates a corresponding profile
    (Student, Teacher, or Admin) based on the user's role.

    Parameters:
        - sender: The sender of the signal (CustomUser model in this case).
        - instance: The instance of the saved CustomUser.
        - kwargs: Additional keyword arguments.

    Logic:
        - Checks the role of the saved user instance using CustomUser.RoleChoices.
        - Creates a corresponding profile (Student, Teacher, or Admin) using get_or_create.

    Example Usage:
        - Automatically creates a Student, Teacher, or Admin profile when a CustomUser is saved
          based on the user's role."""

    if instance.role == CustomUser.RoleChoices.STUDENT:
        student, _ = Student.objects.get_or_create(user=instance)
    elif instance.role == CustomUser.RoleChoices.TEACHER:
        teacher, _ = Teacher.objects.get_or_create(user=instance)
    else:
        admin, _ = Admin.objects.get_or_create(user=instance)
