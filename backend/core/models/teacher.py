from django.db import models
from users.models import CustomUser

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    """
        Many-to-many relationship with subject object
        This assumes that a teacher can be associated with multiple subjects, 
        and each subject can have multiple teachers.
    """
    assigned_subjects = models.ManyToManyField(Subject, related_name='teachers')