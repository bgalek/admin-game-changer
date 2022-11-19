from rest_framework import serializers

from . import models


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = [
            "created",
            "start_date",
            "last_updated",
            "end_date",
        ]

class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Mission
        fields = [
            "last_updated",
            "created",
            "name",
        ]
