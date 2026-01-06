from rest_framework.permissions import BasePermission
from .models import TeamMember

class IsTeamAdmin(BasePermission):
    def has_permission(self, request, view):
        team_id = request.data('team')
        if not team_id:
            return False
        return TeamMember.objects.filter(
            id = team_id,
            user = request.user,
            role = 'admin'
        ).exists()