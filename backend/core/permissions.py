from core.models.admin import Admin
from core.models.teacher import Teacher
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


# class IsTeacher(BasePermission):
#     def has_permission(self, request, view):
#         teacher = Teacher.objects.filter(user = request.user).first()
#         if request.user.is_authenticated and teacher:
#             return True
#         raise PermissionDenied('You are not allowed to perform this action')

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                admin = Admin.objects.filter(user = request.user).exists()
                if admin:
                    return True
                raise PermissionDenied('You are not allowed to perform this action')
            except Admin.DoesNotExist:
                raise PermissionDenied('You are not allowed to perform this action')
        raise PermissionDenied('Authentication required for this action')
    
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                teacher = Teacher.objects.filter(user = request.user).exists()
                if teacher:
                    return True
                raise PermissionDenied('Only Teachers are allowed to perform this action')
            except Teacher.DoesNotExist:
                raise PermissionDenied('You are not allowed to perform this action please')
        raise PermissionDenied('Authentication required for this action')
    
class IsTeacherOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            is_teacher = getattr(request.user, 'teacher', None) is not None
            is_admin = getattr(request.user, 'admin', None) is not None
            return is_teacher or is_admin
        return False