from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from core.models import *

from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_a_profile(sender, instance, **kwargs):
    if instance.role == CustomUser.RoleChoices.STUDENT:
        student, _ = Student.objects.get_or_create(user=instance)
    elif instance.role == CustomUser.RoleChoices.TEACHER:
        teacher, _ = Teacher.objects.get_or_create(user=instance)
    else:
        admin, _ = Admin.objects.get_or_create(user=instance)
        