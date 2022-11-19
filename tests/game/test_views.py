import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Event_list_view(client):
    instance1 = test_helpers.create_game_Event()
    instance2 = test_helpers.create_game_Event()
    url = reverse("game_Event_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Event_create_view(client):
    url = reverse("game_Event_create")
    data = {
        "start_date": datetime.now(),
        "end_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Event_detail_view(client):
    instance = test_helpers.create_game_Event()
    url = reverse("game_Event_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Event_update_view(client):
    instance = test_helpers.create_game_Event()
    url = reverse("game_Event_update", args=[instance.pk, ])
    data = {
        "start_date": datetime.now(),
        "end_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Mission_list_view(client):
    instance1 = test_helpers.create_game_Mission()
    instance2 = test_helpers.create_game_Mission()
    url = reverse("game_Mission_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Mission_create_view(client):
    url = reverse("game_Mission_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Mission_detail_view(client):
    instance = test_helpers.create_game_Mission()
    url = reverse("game_Mission_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Mission_update_view(client):
    instance = test_helpers.create_game_Mission()
    url = reverse("game_Mission_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
