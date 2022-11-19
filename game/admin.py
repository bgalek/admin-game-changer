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
        "name",
        "created",
        "last_updated",
        "end_date",
        "start_date",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class MissionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Mission
        fields = "__all__"


class MissionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "question",
        "right_answer",
        "wrong_answer",
        "score",
        "did_you_know",
        "response",
        "last_updated",
        "created",
    ]
    form = MissionAdminForm
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Mission, MissionAdmin)
