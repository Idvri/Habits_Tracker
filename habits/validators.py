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
