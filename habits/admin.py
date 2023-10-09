from django.contrib import admin

from habits.models import HealthyHabit, PleasantHabit


# Register your models here.
@admin.register(HealthyHabit)
class HealthyHabit(admin.ModelAdmin):
    list_display = ('user', 'action', 'related_habit', 'reward')


@admin.register(PleasantHabit)
class PleasantHabit(admin.ModelAdmin):
    list_display = ('user', 'action')
