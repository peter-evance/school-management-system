from core.models.subject import Subject
from core.models.student import Student
from django_filters import rest_framework as filters


class StudentFilter(filters.FilterSet):
    name = filters.CharFilter(method="filter_by_name", lookup_expr="iexact")

    class Meta:
        model = Student
        fields = ["classroom"]

    def filter_by_name(self, queryset, name, value):
        # To filter by first_name and last_name
        return queryset.filter(user__first_name__icontains=value) | queryset.filter(
            user__last_name__icontains=value
        )


class SubjectFilter(filters.FilterSet):
    class Meta:
        model = Subject
        fields = ["class_room"]
