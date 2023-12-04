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