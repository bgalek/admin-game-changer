from rest_framework import serializers

from . import models


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = [
            "created",
            "last_updated",
            "end_date",
            "start_date",
        ]

class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Mission
        fields = [
            "wrong_answer",
            "last_updated",
            "right_answer",
            "question",
            "response",
            "created",
            "score",
            "name",
            "did_you_know",
            "event",
        ]
