from django.db import models
from core.models.classroom import ClassRoom
from users.models import CustomUser
from core.choices import *
from core.models.subject import Subject

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,limit_choices_to={'role': 'Student'})
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    enrolled_subjects = models.ManyToManyField(Subject, related_name='enrolled_students')
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def registration_number(self):
        registration_number = self.created_at.strftime("%m%d-%Y-%H%M%S") + str(self.id)
        return registration_number[::-1]