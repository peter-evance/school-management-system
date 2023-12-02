from django.db import models
from users.models import CustomUser
from core.choices import *



class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_reg_no(self):
        creation_date = self.created.strftime('%Y')
        return f"{self.id}-##{creation_date}"

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