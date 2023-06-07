from rest_framework.permissions import BasePermission


class CollectionPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name="provider").exists() or request.user.is_staff:
            return True
