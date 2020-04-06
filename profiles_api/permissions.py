from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to update own profile"""

    def has_object_permission(self, request, view, obj):
        """Method to overide for permission """
        if request.method in permissions.SAFE_METHOD:
            return True

        return obj.id == request.user.id
