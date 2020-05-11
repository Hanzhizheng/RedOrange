from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)


class Permission(BasePermission):
    
    def helper(self, request, party_a):
        user = request.user
        exist = user.jobcard_set.filter(
            is_verified=True,
            party_a=party_a,
            is_admin=True,
        ).exists()
        return bool(
            request.method in SAFE_METHODS or exist
        )

    def has_permission(self, request, view):
        if view.action == 'create':
            party_a = request.data['party_a']
            return self.helper(request, party_a)
        return True

    def has_object_permission(self, request, view, obj):
        return self.helper(request, obj.party_a)
