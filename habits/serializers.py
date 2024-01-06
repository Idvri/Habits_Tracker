from rest_framework import serializers

from habits.models import HealthyHabit, PleasantHabit, Habit
from habits.validators import ValidateReward, ValidateTimeRequired, ValidateRewardForUpdate


class HealthyHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyHabit
        fields = "__all__"


class CreateHealthyHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyHabit
        exclude = ('user',)
        validators = [
            ValidateTimeRequired(time_required='time_required'),
            ValidateReward(reward='reward', related_habit='related_habit'),
        ]


class UpdateHealthyHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyHabit
        fields = "__all__"
        validators = [
            ValidateTimeRequired(
                time_required='time_required'
            ),
            ValidateRewardForUpdate(
                reward='reward',
                related_habit='related_habit'
            ),
        ]

    def validate(self, data):
        if 'related_habit' in dict(data) and data['related_habit'] and self.instance.reward:
            data['reward'] = None
            return data
        elif 'reward' in dict(data) and data['reward'] and self.instance.related_habit:
            data['related_habit'] = None
            return data
        else:
            return data


class PleasantHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PleasantHabit
        fields = "__all__"
        validators = [
            ValidateTimeRequired(
                time_required='time_required'
            ),
        ]


class CreatePleasantHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PleasantHabit
        exclude = ('user',)
        validators = [
            ValidateTimeRequired(
                time_required='time_required'
            ),
        ]


class PublicHabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
