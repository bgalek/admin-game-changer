from django.db import models
from django.urls import reverse


class Event(models.Model):

    # Fields
    name = models.CharField(max_length=100, verbose_name="Kampania")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    end_date = models.DateTimeField()
    start_date = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("game_Event_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("game_Event_update", args=(self.pk,))



class Mission(models.Model):

    # Relationships
    event = models.ForeignKey("game.Event", on_delete=models.CASCADE, verbose_name="Kampania")

    # Fields
    wrong_answer = models.TextField(max_length=200, verbose_name="Niepoprawna odpowiedź")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    right_answer = models.TextField(max_length=200, verbose_name="Poprawna odpowiedź")
    question = models.TextField(max_length=200, verbose_name="Pytanie")
    response = models.TextField(max_length=200, verbose_name="Komentarz mędrca")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    score = models.IntegerField(verbose_name="Punktacja")
    name = models.CharField(max_length=50, verbose_name="Nazwa")
    did_you_know = models.TextField(max_length=200, verbose_name="Ciekawostka")

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("game_Mission_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("game_Mission_update", args=(self.pk,))

