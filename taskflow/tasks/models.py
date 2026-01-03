from django.db import models
from django.conf import settings
from teams.models import Team, TeamMember

# Create your models here.

User = settings.AUTH_USER_MODEL

class Task(models.Model):
    TASK_STATUS = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=255, blank=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name= 'assigned_tasks',
    )
    status = models.CharField(
        max_length=20,
        choices= TASK_STATUS,
        default= 'pending'
    )
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

