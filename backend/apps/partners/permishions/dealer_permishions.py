from rest_framework.permissions import BasePermission

from apps.partners.dealer_admin.models import DealerAdminModel
from apps.partners.dealer_manager.models import DealerManager
from apps.partners.dealer_mechanic.models import DealerMechanicModel
from apps.partners.dealer_seller.models import DealerSellerModel


class IsDealerAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            dealer_admin = DealerAdminModel.objects.get(user=request.user)
            return dealer_admin.role == "DEALER_ADMIN"
        except DealerAdminModel.DoesNotExist:
            return False


class IsDealerManager(BasePermission):
    def has_permission(self, request, view):
        try:
            dealer_admin = DealerManager.objects.get(user=request.user)
            return dealer_admin.role == "DEALER_MANAGER"
        except DealerAdminModel.DoesNotExist:
            return False


class IsDealerMechanic(BasePermission):
    def has_permission(self, request, view):
        try:
            dealer_admin = DealerMechanicModel.objects.get(user=request.user)
            return dealer_admin.role == "DEALER_MECHANIC"
        except DealerAdminModel.DoesNotExist:
            return False


class IsDealersSeller(BasePermission):
    def has_permission(self, request, view):
        try:
            dealer_admin = DealerSellerModel.objects.get(user=request.user)
            return dealer_admin.role == "DEALER_SELLER"
        except DealerAdminModel.DoesNotExist:
            return False
