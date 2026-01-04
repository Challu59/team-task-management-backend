from django.shortcuts import render
from .models import Task
from rest_framework import permissions, viewsets
from .serializers import TaskSerializer
from .permissions import IsTeamAdmin, IsTaskAssignee
from teams.models import Team, TeamMember

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(team__memberships__user = self.request.user)
    
    def get_team(self):
        team_id = self.request.data.get('team')
        return (Team.objects.get(id = team_id))
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAuthenticated(), IsTeamAdmin()]
        elif self.action == 'partial_update':
            return[permissions.IsAuthenticated(), IsTaskAssignee()]
        return super().get_permissions()