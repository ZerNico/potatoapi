from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermissions(BasePermission):
    """Only allow staff to interact with the db"""
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_active:
            return request.user.is_staff
