from rest_framework import permissions


class IsDealerManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Dealer_Manager').exists())


class IsSellerDealer(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Dealer_Seller').exists())


class IsMechanicDealer(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Dealer_Mechanic').exists())


class IsDealerAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Dealer_Admin').exists())
