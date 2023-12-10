from core.models.student import Student
from django_filters import rest_framework as filters


class StudentFilter(filters.FilterSet):
    class Meta:
        model = Student
        fields = ["classroom"]

    def filter_by_name(self, queryset, value):
        # To filter by first_name and last_name
        return queryset.filter(user__first_name__iexact=value) | queryset.filter(
            user__last_name__iexact=value
        )
