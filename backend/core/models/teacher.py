from django.db import models
from users.models import CustomUser
from core.models.subject import Subject
from core.models.classroom import ClassRoom

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'Teacher'})
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_subjects = models.ManyToManyField(Subject, related_name='teachers')