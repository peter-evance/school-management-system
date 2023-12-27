from core.models.exams import Exam
from core.models.results import SubjectResult
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


class ExamFilter(filters.FilterSet):
    class Meta:
        model = Exam
        fields = ("exam_type", "subject")


class SubjectResultFilter(filters.FilterSet):
    class Meta:
        model = SubjectResult
        fields = ("student", "exam")
