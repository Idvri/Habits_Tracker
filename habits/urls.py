from django.urls import path

from habits.apps import HabitsConfig
from habits.views import CreateHealthyHabitApiView, CreatePleasantHabitApiView

app_name = HabitsConfig.name

urlpatterns = [
    path('healthy_habit/create/', CreateHealthyHabitApiView.as_view(), name='create_healthy_habit'),
    path('pleasant_habit/create/', CreatePleasantHabitApiView.as_view(), name='create_pleasant_habit'),
]
