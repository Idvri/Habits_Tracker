from rest_framework import generics

from habits.serializers import HealthyHabitSerializer, PleasantHabitSerializer


# Create your views here.
class CreateHealthyHabitApiView(generics.CreateAPIView):
    serializer_class = HealthyHabitSerializer


class CreatePleasantHabitApiView(generics.CreateAPIView):
    serializer_class = PleasantHabitSerializer
