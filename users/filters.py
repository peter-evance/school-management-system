from users.models import CustomUser, ProfileImage
from django_filters import rest_framework as filters


class CustomUserFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = CustomUser
        fields = ["role", "first_name"]

class ImageFilter(filters.FilterSet):
    # first_name = filters.CharFilter(field_name='user__first_name',lookup_expr='icontains')
    class Meta:
        model = ProfileImage
        fields = ["user"]
