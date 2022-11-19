from django import forms
from game.models import Event
from . import models


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = [
            "end_date",
            "start_date",
        ]


class MissionForm(forms.ModelForm):
    class Meta:
        model = models.Mission
        fields = [
            "wrong_answer",
            "right_answer",
            "question",
            "response",
            "score",
            "name",
            "did_you_know",
            "event",
        ]

    def __init__(self, *args, **kwargs):
        super(MissionForm, self).__init__(*args, **kwargs)
        self.fields["event"].queryset = Event.objects.all()

