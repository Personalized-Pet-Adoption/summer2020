from rest_framework import permissions

class isSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

class isAdopter(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
        