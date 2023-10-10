from rest_framework import serializers

from habits.models import HealthyHabit, PleasantHabit
from habits.validators import ValidateReward


class HealthyHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyHabit
        fields = "__all__"
        validators = [
            ValidateReward(reward='reward', related_habit='related_habit'),
        ]


class PleasantHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PleasantHabit
        fields = "__all__"
