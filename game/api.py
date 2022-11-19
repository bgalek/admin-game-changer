from rest_framework import viewsets, permissions

from . import serializers
from . import models


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet for the Event class"""

    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class MissionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Mission class"""

    queryset = models.Mission.objects.all()
    serializer_class = serializers.MissionSerializer
    permission_classes = [permissions.IsAuthenticated]
