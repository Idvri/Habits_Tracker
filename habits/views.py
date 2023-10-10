from rest_framework import generics

from habits.models import HealthyHabit, PleasantHabit
from habits.paginators import HabitPaginator
from habits.serializers import HealthyHabitSerializer, PleasantHabitSerializer, CreateHealthyHabitSerializer, \
    UpdateHealthyHabitSerializer


# Create your views here.
class CreateHealthyHabitApiView(generics.CreateAPIView):
    serializer_class = CreateHealthyHabitSerializer


class ListHealthyHabitApiView(generics.ListAPIView):
    serializer_class = HealthyHabitSerializer
    queryset = HealthyHabit.objects.all()
    pagination_class = HabitPaginator


class RetrieveHealthyHabitApiView(generics.RetrieveAPIView):
    serializer_class = HealthyHabitSerializer
    queryset = HealthyHabit.objects.all()


class UpdateHealthyHabitApiView(generics.UpdateAPIView):
    serializer_class = UpdateHealthyHabitSerializer
    queryset = HealthyHabit.objects.all()


class DestroyHealthyHabitApiView(generics.DestroyAPIView):
    queryset = HealthyHabit.objects.all()


class CreatePleasantHabitApiView(generics.CreateAPIView):
    serializer_class = PleasantHabitSerializer


class ListPleasantHabitApiView(generics.ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    pagination_class = HabitPaginator


class RetrievePleasantHabitApiView(generics.RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()


class UpdatePleasantHabitApiView(generics.UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()


class DestroyPleasantHabitApiView(generics.DestroyAPIView):
    queryset = PleasantHabit.objects.all()
