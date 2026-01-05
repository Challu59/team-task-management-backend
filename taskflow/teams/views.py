from django.shortcuts import render
from .serializers import TeamSerializer
from rest_framework import permissions,viewsets
from .models import Team, TeamMember

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = permissions.IsAuthenticated

    def get_queryset(self):
        return Team.objects.filter(memberships__user = self.request.user)
    
    def perform_create(self, serializer):
        team = serializer.save(creator = self.request.user)
        TeamMember.objects.crate(
            user = self.request.user,
            team = team,
            role = 'admin'
        )
        return super().perform_create(serializer)