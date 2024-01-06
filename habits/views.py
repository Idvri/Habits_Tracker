from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema

from habits.models import HealthyHabit, PleasantHabit, Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HealthyHabitSerializer, PleasantHabitSerializer, CreateHealthyHabitSerializer, \
    UpdateHealthyHabitSerializer, PublicHabitsSerializer, CreatePleasantHabitSerializer


# Create your views here.
@extend_schema(summary="Создать полезную привычку.")
class CreateHealthyHabitApiView(generics.CreateAPIView):
    serializer_class = CreateHealthyHabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


@extend_schema(summary="Получить список полезных привычек.")
class ListHealthyHabitApiView(generics.ListAPIView):
    serializer_class = HealthyHabitSerializer
    queryset = HealthyHabit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PleasantHabit.objects.filter(user=self.request.user).order_by('pk')


@extend_schema(summary="Просмотреть полезную привычку.")
class RetrieveHealthyHabitApiView(generics.RetrieveAPIView):
    serializer_class = HealthyHabitSerializer
    queryset = HealthyHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


@extend_schema(summary="Редактировать полезную привычку.")
class UpdateHealthyHabitApiView(generics.UpdateAPIView):
    serializer_class = UpdateHealthyHabitSerializer
    queryset = HealthyHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


@extend_schema(summary="Удалить полезную привычку.")
class DestroyHealthyHabitApiView(generics.DestroyAPIView):
    queryset = HealthyHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


@extend_schema(summary="Создать приятную привычку.")
class CreatePleasantHabitApiView(generics.CreateAPIView):
    serializer_class = CreatePleasantHabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


@extend_schema(summary="Получить список приятных привычек.")
class ListPleasantHabitApiView(generics.ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PleasantHabit.objects.filter(user=self.request.user).order_by('pk')


@extend_schema(summary="Просмотреть приятную привычку.")
class RetrievePleasantHabitApiView(generics.RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]


@extend_schema(summary="Редактировать приятную привычку.")
class UpdatePleasantHabitApiView(generics.UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


@extend_schema(summary="Удалить приятную привычку.")
class DestroyPleasantHabitApiView(generics.DestroyAPIView):
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


@extend_schema(summary="Получить список публичных привычек.")
class ListPublicHabitsApiView(generics.ListAPIView):
    serializer_class = PublicHabitsSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
