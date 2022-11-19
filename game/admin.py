from django.contrib import admin
from django import forms

from . import models


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = models.Event
        fields = "__all__"


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = [
        "created",
        "last_updated",
        "end_date",
        "start_date",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "end_date",
        "start_date",
    ]


class MissionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Mission
        fields = "__all__"


class MissionAdmin(admin.ModelAdmin):
    form = MissionAdminForm
    list_display = [
        "wrong_answer",
        "last_updated",
        "right_answer",
        "question",
        "response",
        "created",
        "score",
        "name",
        "did_you_know",
    ]
    readonly_fields = [
        "wrong_answer",
        "last_updated",
        "right_answer",
        "question",
        "response",
        "created",
        "score",
        "name",
        "did_you_know",
    ]


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Mission, MissionAdmin)
