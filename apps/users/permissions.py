from rest_framework.permissions import BasePermission

from apps.users.choices import AccountType, UserRoleType


# =============================================role_type===============================================
class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role_type == UserRoleType.BUYER)


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role_type == UserRoleType.SELLER)


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role_type == UserRoleType.MANAGER)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role_type == UserRoleType.ADMIN)


# =================================================account_type====================================================
class IsSellerBasic(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.account_type == AccountType.BASIC)


class IsSellerPremium(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.account_type == AccountType.PREMIUM)
