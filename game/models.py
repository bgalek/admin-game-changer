from django.db import models
from django.urls import reverse


class Event(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    start_date = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    end_date = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("game_Event_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("game_Event_update", args=(self.pk,))



class Mission(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=50)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("game_Mission_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("game_Mission_update", args=(self.pk,))

