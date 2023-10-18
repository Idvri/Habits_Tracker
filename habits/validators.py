from rest_framework import serializers


class ValidateReward:
    def __init__(self, reward, related_habit):
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        reward = dict(value).get(self.reward)
        related_habit = dict(value).get(self.related_habit)
        if reward is None and related_habit is None:
            raise serializers.ValidationError('Нужно указать награду или приятную привычку')
        elif reward and related_habit:
            raise serializers.ValidationError('Нужно указать только награду или только приятную привычку,'
                                              ' но не оба варианта.')


class ValidateRewardForUpdate(ValidateReward):

    def __call__(self, value):
        if 'reward' in dict(value) and 'related_habit' in dict(value):
            raise serializers.ValidationError('Нужно указать только награду или только приятную привычку,'
                                              ' но не оба варианта.')


class ValidateTimeRequired:

    def __init__(self, time_required):
        self.time_required = time_required

    def __call__(self, value):
        if 'time_required' in dict(value):
            time_required = dict(value).get(self.time_required)
            if time_required > 120:
                raise serializers.ValidationError('Время для выполнения привычки не может быть больше 120 секунд')
