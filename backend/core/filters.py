from core.models.subject import Subject
from core.models.student import Student
from django_filters import rest_framework as filters


class StudentFilter(filters.FilterSet):
    user = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Student
        fields = ["user"]


class SubjectFilter(filters.FilterSet):
    class Meta:
        model = Subject
        fields = ["class_room"]
