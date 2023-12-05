from core.models.admin import Admin
from core.models.student import Student
from core.models.teacher import Teacher
from core.models.classroom import ClassRoom
from core.models.subject import Subject
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title', 'code', 'added_at']

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['title', 'code', 'capacity', 'stream']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        depth = True
        model = Teacher
        fields = ['user', 'classroom', 'created_at', 'assigned_subjects']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = True
        model = Student
        fields = ['user', 'classroom', 'address', 'created_at','enrolled_subjects','registration_number']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['user', 'created']