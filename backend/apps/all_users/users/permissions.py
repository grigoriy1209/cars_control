from rest_framework.permissions import BasePermission

from apps.all_users.users.choices import UserRoleType


class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        print(f"User: {request.user}")
        print(f"Is staff: {request.user.is_staff}")
        print(f"Role: {request.user.role_type}")
        return bool(
            request.user and
            request.user.is_staff
            and request.user.role_type in ['Manager', 'Admin'])


class IsPremiumSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.role_type == UserRoleType.PREMIUM_SELLER
        )
