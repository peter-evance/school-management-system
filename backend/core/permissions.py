from core.models.teacher import Teacher
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        teacher = Teacher.objects.filter(user = request.user).first()
        if request.user.is_authenticated and teacher:
            return True
        raise PermissionDenied('You are not allowed to perform this action')