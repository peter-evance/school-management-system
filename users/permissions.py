from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    """
    Custom permission class that allows only students to perform an action.

    Raises:
    - `PermissionDenied`: If the user is not a student.

    Usage:
        Add the permission class to the view or viewset that requires student access:
        permission_classes = [IsStudent]
    """

    message = {"message": "Only students have permission to perform this action."}

    def has_permission(self, request, view):
        # Check if the current user is a student
        if request.user.is_authenticated and request.user.is_a_student:
            return True
        raise PermissionDenied(self.message)


class IsTeacher(BasePermission):
    """
    Custom permission class that allows only teachers to perform an action.

    Raises:
    - `PermissionDenied`: If the user is not a teacher.

    Usage:
        Add the permission class to the view or viewset that requires teacher access:
        permission_classes = [IsTeacher]
    """

    message = {"message": "Only teachers have permission to perform this action."}

    def has_permission(self, request, view):
        # Check if the current user is a teacher
        if request.user.is_authenticated and request.user.is_a_teacher:
            return True
        raise PermissionDenied(self.message)


class IsAdmin(BasePermission):
    """
    Custom permission class that allows only admins to perform an action.

    Raises:
    - `PermissionDenied`: If the user is not an admin.

    Usage:
        Add the permission class to the view or viewset that requires admin access:
        permission_classes = [IsAdmin]
    """

    message = {"message": "Only admins have permission to perform this action."}

    def has_permission(self, request, view):
        # Check if the current user is an admin
        if request.user.is_authenticated and request.user.is_admin:
            return True
        raise PermissionDenied(self.message)
