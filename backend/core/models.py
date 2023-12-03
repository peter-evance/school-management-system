# from django.db import models
# from users.models import CustomUser
# from core.choices import *
# from datetime import datetime


# class Student(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
#     date_of_birth = models.DateField(null=True)
#     address = models.TextField(null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     """
#         Many-to-many relationship with subject object
#         This assumes that each student can be enrolled in multiple subjects, 
#         and each subject can have multiple enrolled students.
#     """
#     enrolled_subjects = models.ManyToManyField(Subject, related_name='enrolled_students')
    
#     @property
#     def generate_registration_number(self):
#         registration_number = self.created.strftime("%m%d-%Y-%H%M%S") + str(self.id)
#         return registration_number[::-1]

# class Subject(models.Model):
#     title = models.CharField(max_length=20)
#     code = models.CharField(max_length=10)
#     max_marks = models.PositiveIntegerField(default=100)
#     min_mark = models.PositiveIntegerField(default=40)
#     mark_obtained = models.PositiveIntegerField(default=0, null=True)
#     grade = models.CharField(max_length=10, null=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def grading_system(self):
#         """
#         Calculate and set the grade based on the value of mark_obtained.
#         """
#         if not self.mark_obtained:
#             return

#         if self.mark_obtained >= 90:
#             self.grade = 'A+'
#         elif 70 <= self.mark_obtained < 90:
#             self.grade = 'A'
#         elif 60 <= self.mark_obtained < 70:
#             # self.mark_obtained is between 60-69
#             self.grade = 'B'
#         elif 50 <= self.mark_obtained < 60:
#             # self.mark_obtained is between 50-59
#             self.grade = 'C'
#         elif 40 <= self.mark_obtained < 50:
#             # self.mark_obtained is between 40-59
#             self.grade = 'D'
#         else:
#             # self.mark_obtained is less than 40
#             self.grade = 'FAILED'

#     def save(self, *args, **kwargs):
#         self.grading_system()
#         super().save(*args, **kwargs)


# class Teacher(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     """
#         Many-to-many relationship with subject object
#         This assumes that a teacher can be associated with multiple subjects, 
#         and each subject can have multiple teachers.
#     """
#     assigned_subjects = models.ManyToManyField(Subject, related_name='teachers')

# class Admin(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)


# class ClassRoom(models.Model):
#     title = models.CharField(max_length=30, choices=ClassRoomTitleChoices.choices)
#     code = models.CharField(max_length=10, choices=ClassRoomCodeChoices.choices)
#     capacity = models.PositiveIntegerField(default=1)
#     stream = models.CharField(max_length=1, choices=ClassRoomStreamChoices.choices)
    
#     def __str__(self):
#         return self.title