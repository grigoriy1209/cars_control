from rest_framework.permissions import BasePermission


class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        print(f"User: {request.user}")
        print(f"Is staff: {request.user.is_staff}")
        print(f"Role: {request.user.role_type}")
        return bool(
            request.user and
            request.user.is_staff
            and request.user.role_type in ['Manager', 'Admin'])