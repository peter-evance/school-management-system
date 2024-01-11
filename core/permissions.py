from core.models.admin import Admin
from core.models.teacher import Teacher
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Django Permission Class: IsAdmin

    Custom permission class to restrict access to views for non-admin users.

    Attributes:
        - Inherits from Django's BasePermission class.

    Methods:
        - has_permission(self, request, view): Checks if the requesting user is authenticated and is an admin.
          - If authenticated, it queries the Admin model to verify admin status.
          - Raises PermissionDenied if the user is not an admin.
          - Raises PermissionDenied if the Admin model does not exist for the user.
          - Raises AuthenticationFailed if the user is not authenticated.

    Example Usage:
        # Include this permission class in the 'permission_classes' attribute of a Django view.
        class YourAdminRestrictedView(APIView):
            permission_classes = [IsAdmin]

            def get(self, request, *args, **kwargs):
                # Your view logic here
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                admin = Admin.objects.filter(user=request.user).exists()
                if admin:
                    return True
                raise PermissionDenied("You are not allowed to perform this action")
            except Admin.DoesNotExist:
                raise PermissionDenied("You are not allowed to perform this action")
        raise AuthenticationFailed("Authentication required for this action")


class IsTeacher(BasePermission):
    """
    Django Permission Class: IsTeacher

    Custom permission class to restrict access to views for non-teacher users.

    Attributes:
        - Inherits from Django's BasePermission class.

    Methods:
        - has_permission(self, request, view): Checks if the requesting user is authenticated and is a teacher.
          - If authenticated, it queries the Teacher model to verify teacher status.
          - Raises PermissionDenied if the user is not a teacher.
          - Raises PermissionDenied if the Teacher model does not exist for the user.
          - Raises AuthenticationFailed if the user is not authenticated.

    Example Usage:
        # Include this permission class in the 'permission_classes' attribute of a Django view.
        class YourTeacherRestrictedView(APIView):
            permission_classes = [IsTeacher]

            def get(self, request, *args, **kwargs):
                # Your view logic here
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                teacher = Teacher.objects.filter(user=request.user).exists()
                if teacher:
                    return True
                raise PermissionDenied(
                    "Only Teachers are allowed to perform this action"
                )
            except Teacher.DoesNotExist:
                raise PermissionDenied(
                    "You are not allowed to perform this action please"
                )
        raise AuthenticationFailed("Authentication required for this action")


class IsTeacherOrAdmin(BasePermission):
    """
    Django Permission Class: IsTeacherOrAdmin

    Custom permission class to restrict access to views for non-teacher and non-admin users.

    Attributes:
        - Inherits from Django's BasePermission class.

    Methods:
        - has_permission(self, request, view): Checks if the requesting user is authenticated and is either a teacher or an admin.
          - If authenticated, it checks whether the user has the 'teacher' or 'admin' attribute.
          - Raises PermissionDenied if the user is neither a teacher nor an admin.
          - Returns True if the user is a teacher or an admin, allowing access.
          - Raises AuthenticationFailed if the user is not authenticated.

    Example Usage:
        # Include this permission class in the 'permission_classes' attribute of a Django view.
        class YourTeacherOrAdminRestrictedView(APIView):
            permission_classes = [IsTeacherOrAdmin]

            def get(self, request, *args, **kwargs):
                # Your view logic here
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            is_teacher = getattr(request.user, "teacher", None) is not None
            is_admin = getattr(request.user, "admin", None) is not None
            if not (is_teacher or is_admin):
                raise PermissionDenied("You are not allowed to perform this action")
            return is_teacher or is_admin
        raise AuthenticationFailed("Authentication required for this action")
