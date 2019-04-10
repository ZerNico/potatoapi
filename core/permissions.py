from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    """Only allow staff to interact with the db"""
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated and \
                   request.user.is_staff and \
                   request.user.is_active
        else:
            return False
