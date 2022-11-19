from django import forms
from . import models


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = [
            "start_date",
            "end_date",
        ]


class MissionForm(forms.ModelForm):
    class Meta:
        model = models.Mission
        fields = [
            "name",
        ]
