from users.models import CustomUser
from django_filters import rest_framework as filters


class CustomUserFilter(filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name"]
