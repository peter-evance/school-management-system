from django.db import models
from users.models import CustomUser
from core.choices import *
from datetime import datetime


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    @property
    def generate_registration_number(self):
        registration_number = self.created.strftime("%m%d-%Y-%H%M%S") + str(self.id)
        return registration_number[::-1]

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class ClassRoom(models.Model):
    title = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField(default=1)
    stream = models.CharField(max_length=1, choices=ClassRoomStreamChoices.choices)
    
    
    def __str__(self):
        return self.title