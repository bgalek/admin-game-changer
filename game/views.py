from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class EventListView(generic.ListView):
    model = models.Event
    form_class = forms.EventForm


class EventCreateView(generic.CreateView):
    model = models.Event
    form_class = forms.EventForm


class EventDetailView(generic.DetailView):
    model = models.Event
    form_class = forms.EventForm


class EventUpdateView(generic.UpdateView):
    model = models.Event
    form_class = forms.EventForm
    pk_url_kwarg = "pk"


class EventDeleteView(generic.DeleteView):
    model = models.Event
    success_url = reverse_lazy("game_Event_list")


class MissionListView(generic.ListView):
    model = models.Mission
    form_class = forms.MissionForm


class MissionCreateView(generic.CreateView):
    model = models.Mission
    form_class = forms.MissionForm


class MissionDetailView(generic.DetailView):
    model = models.Mission
    form_class = forms.MissionForm


class MissionUpdateView(generic.UpdateView):
    model = models.Mission
    form_class = forms.MissionForm
    pk_url_kwarg = "pk"


class MissionDeleteView(generic.DeleteView):
    model = models.Mission
    success_url = reverse_lazy("game_Mission_list")
