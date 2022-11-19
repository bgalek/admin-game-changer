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
        "start_date",
        "last_updated",
        "end_date",
    ]
    readonly_fields = [
        "created",
        "start_date",
        "last_updated",
        "end_date",
    ]


class MissionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Mission
        fields = "__all__"


class MissionAdmin(admin.ModelAdmin):
    form = MissionAdminForm
    list_display = [
        "last_updated",
        "created",
        "name",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "name",
    ]


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Mission, MissionAdmin)
