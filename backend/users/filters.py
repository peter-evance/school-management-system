from users.models import CustomUser
from django_filters import rest_framework as filters


class CustomUserFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = CustomUser
        fields = ["role", "first_name"]
