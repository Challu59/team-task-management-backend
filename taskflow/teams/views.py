from django.shortcuts import render
from .serializers import TeamSerializer, TeamMemberSerializer
from rest_framework import permissions,viewsets
from .models import Team, TeamMember
from .permissions import IsTeamAdmin

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Team.objects.filter(memberships__user = self.request.user)
    
    def perform_create(self, serializer):
        team = serializer.save(creator = self.request.user)
        TeamMember.objects.create(
            user = self.request.user,
            team = team,
            role = 'admin'
        )

class TeamMemberViewSet(viewsets.ModelViewSet):
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TeamMember.objects.filter(
            team__memberships__user=self.request.user
        )

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [permissions.IsAuthenticated(), IsTeamAdmin()]
        return super().get_permissions()