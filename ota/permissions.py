from rest_framework.permissions import BasePermission, SAFE_METHODS


class BuildPermissions(BasePermission):
    """Only allow staff and maintainers to interact with the db"""
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_active:
            return request.user.is_superuser or \
                obj.user == request.user and \
                request.user.is_maintainer

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_active:
            return request.user.is_superuser or \
                request.user.is_maintainer
