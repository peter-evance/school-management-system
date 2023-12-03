from django.db import models
from users.models import CustomUser

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)