from users.filters import CustomUserFilter, ImageFilter
from rest_framework.viewsets import ModelViewSet
from users.serializers import (
    CustomUserCreateSerializer,
    CustomUserSerializer,
    ProfileImageSerializer,
)
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django_filters import rest_framework as filters
from users.models import CustomUser, ProfileImage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from users.permissions import IsAdmin


class CustomUserViewSet(ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomUserFilter

    def get_serializer_class(self):
        if self.action == "create":
            return CustomUserCreateSerializer
        return CustomUserSerializer

    @action(detail=False, methods=["PATCH"], permission_classes=[IsAdmin])
    def approve_new_users(self, request):
        user_ids = request.data.get("user_ids", [])
        current_user = request.user

        approved_users = []
        not_found_users = []
        invalid_users = []

        for user_id in user_ids:
            try:
                user = CustomUser.objects.get(id=int(user_id))
            except (ValueError, CustomUser.DoesNotExist):
                if user.isdigit(user_id):
                    not_found_users.append(user_id)
                else:
                    invalid_users.append(user_id)
            else:
                if user == current_user:
                    raise ValidationError("You cannot approve yourself")
                elif user.is_approved:
                    raise ValidationError(f"User {user.username} is already approved")
                else:
                    user.approve_user()
                    approved_users.append(user)

        response_data = {}
        if approved_users:
            if len(approved_users) > 1:
                response_data["message"] = (
                    f"Users {', '.join(approved_users)} has been approved"
                )
            else:
                response_data["message"] = f"User {approved_users[0]} has been approved"

        if not_found_users:
            if len(not_found_users) > 1:
                response_data["error"] = (
                    f"Users with the following IDs are not found: {', '.join(not_found_users)}"
                )
            else:
                response_data["error"] = (
                    f"User with the following ID is not found: {not_found_users[0]}"
                )

        if invalid_users:
            if len(invalid_users) > 1:
                response_data["error"] = (
                    f"Users with the following IDs are invalid: {', '.join(invalid_users)}"
                )
            else:
                response_data["error"] = (
                    f"User with the following ID is invalid: {invalid_users[0]}"
                )

        status_code = (
            status.HTTP_200_OK
            if not response_data.get("error")
            else status.HTTP_400_BAD_REQUEST
        )
        return Response(response_data, status=status_code)


class ProfileImageViewSet(ModelViewSet):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ImageFilter
