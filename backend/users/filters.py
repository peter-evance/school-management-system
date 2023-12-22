from users.models import CustomUser
from django_filters import rest_framework as filters
from django_filters import CharFilter


class CustomUserFilter(filters.FilterSet):
    first_name = CharFilter(lookup_expr='icontains')
    class Meta:
        model = CustomUser
        fields = ["role", "first_name"]
