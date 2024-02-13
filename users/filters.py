from users.models import CustomUser, ProfileImage, Notification
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

class NotificationFilter(filters.FilterSet):
    class Meta:
        model = Notification
        fields = ["user"]
