from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Habit(models.Model):
    REGULARITY_CHOICES = (
        ('Daily', 'Eжедневно'),
        ('Monthly', 'Eжемесячно')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        **NULLABLE
    )
    place = models.CharField(max_length=255, verbose_name='место')
    time = models.TimeField(verbose_name='время, когда необходимо выполнять')
    action = models.CharField(max_length=255, verbose_name='действие')
    regularity = models.CharField(
        max_length=7,
        choices=REGULARITY_CHOICES,
        default='Daily',
        verbose_name='периодичность'
    )
    time_required = models.IntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(
        default=False,
        verbose_name='признак публичности'
    )

    def __str__(self):
        return f'{self.action}'


class PleasantHabit(Habit):
    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'


class HealthyHabit(Habit):
    related_habit = models.ForeignKey(
        PleasantHabit,
        on_delete=models.SET_NULL, **NULLABLE,
        verbose_name='связанная привычка'
    )
    reward = models.CharField(
        max_length=255,
        verbose_name='награда',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'
