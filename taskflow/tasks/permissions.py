from rest_framework.permissions import BasePermission

class IsTeamAdmin(BasePermission):
    def has_permission(self, request, view):
        team = view.getTeam()
        return team.created_by == request.user

class IsTaskAssignee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assigned_to == request.user
