from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostPermissions(BasePermission):
    """Only allow staff to interact with the db"""
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated and \
                   request.user.is_staff and \
                   request.user.is_active
