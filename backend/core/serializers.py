from core.models.subject import Subject
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title', 'code', 'added_at']