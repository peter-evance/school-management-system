from django.db import models
from users.models import CustomUser


class Admin(models.Model):
    """
    Django Model: Admin

    Represents an administrator linked to a CustomUser with 'role' set to "Admin".

    Attributes:
        user (CustomUser): One-to-one link to the associated user.
        created (DateTimeField): Timestamp for record creation.

    Example Usage:
        admin_instance = Admin.objects.create(user=admin_user)
        print(admin_instance.user)
        print(admin_instance.created)"""

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, limit_choices_to={"role": "Admin"}
    )
    created = models.DateTimeField(auto_now_add=True)
