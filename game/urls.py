from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Event", api.EventViewSet)
router.register("Mission", api.MissionViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("game/Event/", views.EventListView.as_view(), name="game_Event_list"),
    path("game/Event/create/", views.EventCreateView.as_view(), name="game_Event_create"),
    path("game/Event/detail/<int:pk>/", views.EventDetailView.as_view(), name="game_Event_detail"),
    path("game/Event/update/<int:pk>/", views.EventUpdateView.as_view(), name="game_Event_update"),
    path("game/Event/delete/<int:pk>/", views.EventDeleteView.as_view(), name="game_Event_delete"),
    path("game/Mission/", views.MissionListView.as_view(), name="game_Mission_list"),
    path("game/Mission/create/", views.MissionCreateView.as_view(), name="game_Mission_create"),
    path("game/Mission/detail/<int:pk>/", views.MissionDetailView.as_view(), name="game_Mission_detail"),
    path("game/Mission/update/<int:pk>/", views.MissionUpdateView.as_view(), name="game_Mission_update"),
    path("game/Mission/delete/<int:pk>/", views.MissionDeleteView.as_view(), name="game_Mission_delete"),

)
