from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import HealthyHabit, PleasantHabit, Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HealthyHabitSerializer, PleasantHabitSerializer, CreateHealthyHabitSerializer, \
    UpdateHealthyHabitSerializer, PublicHabitsSerializer, CreatePleasantHabitSerializer


# Create your views here.
class CreateHealthyHabitApiView(generics.CreateAPIView):
    serializer_class = CreateHealthyHabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class ListHealthyHabitApiView(generics.ListAPIView):
    serializer_class = HealthyHabitSerializer
    queryset = HealthyHabit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PleasantHabit.objects.filter(user=self.request.user)


class RetrieveHealthyHabitApiView(generics.RetrieveAPIView):
    serializer_class = HealthyHabitSerializer
    queryset = HealthyHabit.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PleasantHabit.objects.filter(user=self.request.user)


class UpdateHealthyHabitApiView(generics.UpdateAPIView):
    serializer_class = UpdateHealthyHabitSerializer
    queryset = HealthyHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class DestroyHealthyHabitApiView(generics.DestroyAPIView):
    queryset = HealthyHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class CreatePleasantHabitApiView(generics.CreateAPIView):
    serializer_class = CreatePleasantHabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class ListPleasantHabitApiView(generics.ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PleasantHabit.objects.filter(user=self.request.user)


class RetrievePleasantHabitApiView(generics.RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PleasantHabit.objects.filter(user=self.request.user)


class UpdatePleasantHabitApiView(generics.UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class DestroyPleasantHabitApiView(generics.DestroyAPIView):
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class ListPublicHabitsApiView(generics.ListAPIView):
    serializer_class = PublicHabitsSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
