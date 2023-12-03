from django.db import models
from core.choices import *

class ClassRoom(models.Model):
    title = models.CharField(max_length=30, choices=ClassRoomTitleChoices.choices)
    code = models.CharField(max_length=10, choices=ClassRoomCodeChoices.choices)
    capacity = models.PositiveIntegerField(default=1)
    stream = models.CharField(max_length=1, choices=ClassRoomStreamChoices.choices)
    
    def __str__(self):
        return self.title