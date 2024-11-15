from rest_framework.permissions import BasePermission

from apps.all_users.accounts.models import AccountType
from apps.all_users.users.choices import UserRoleType


class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role_type == UserRoleType.BUYER)


class IsSellerPrime(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role_type == UserRoleType.PREMIUM_SELLER
            and request.user.account_type == AccountType.PREMIUM
        )


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role_type == UserRoleType.MANAGER)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role_type == UserRoleType.ADMIN)


