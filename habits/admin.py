from django.contrib import admin

from habits.models import HealthyHabit, PleasantHabit


# Register your models here.
@admin.register(HealthyHabit)
class AdminHealthyHabit(admin.ModelAdmin):
    list_display = ('user', 'action', 'related_habit', 'reward')


@admin.register(PleasantHabit)
class AdminPleasantHabit(admin.ModelAdmin):
    list_display = ('user', 'action')
