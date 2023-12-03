from django.db import models
from users.models import CustomUser
from core.models.choices import *
from core.models.subject import Subject

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    """
        Many-to-many relationship with subject object
        This assumes that each student can be enrolled in multiple subjects, 
        and each subject can have multiple enrolled students.
    """
    enrolled_subjects = models.ManyToManyField(Subject, related_name='enrolled_students')
    
    @property
    def generate_registration_number(self):
        registration_number = self.created.strftime("%m%d-%Y-%H%M%S") + str(self.id)
        return registration_number[::-1]
