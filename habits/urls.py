from django.urls import path

from habits.apps import HabitsConfig
from habits.views import CreateHealthyHabitApiView, CreatePleasantHabitApiView, ListHealthyHabitApiView, \
    RetrieveHealthyHabitApiView, UpdateHealthyHabitApiView, DestroyHealthyHabitApiView, ListPleasantHabitApiView, \
    RetrievePleasantHabitApiView, UpdatePleasantHabitApiView, DestroyPleasantHabitApiView, ListPublicHabitsApiView

app_name = HabitsConfig.name

urlpatterns = [
    path('healthy_habits/create', CreateHealthyHabitApiView.as_view(), name='create_healthy_habit'),
    path('healthy_habits', ListHealthyHabitApiView.as_view(), name='healthy_habits'),
    path('healthy_habits/<int:pk>', RetrieveHealthyHabitApiView.as_view(), name='overview_healthy_habit'),
    path('healthy_habits/update/<int:pk>', UpdateHealthyHabitApiView.as_view(), name='update_healthy_habit'),
    path('healthy_habits/delete/<int:pk>', DestroyHealthyHabitApiView.as_view(), name='delete_healthy_habit'),

    path('pleasant_habits/create', CreatePleasantHabitApiView.as_view(), name='create_pleasant_habit'),
    path('pleasant_habits', ListPleasantHabitApiView.as_view(), name='pleasant_habits'),
    path('pleasant_habits/<int:pk>', RetrievePleasantHabitApiView.as_view(), name='overview_pleasant_habit'),
    path('pleasant_habits/update/<int:pk>', UpdatePleasantHabitApiView.as_view(), name='update_pleasant_habit'),
    path('pleasant_habits/delete/<int:pk>', DestroyPleasantHabitApiView.as_view(), name='delete_pleasant_habit'),

    path('public_habits', ListPublicHabitsApiView.as_view(), name='public_habits'),
]
