from datetime import datetime
import requests

from celery import shared_task

from config.settings import BOT_API, BOT_API_KEY, CHAT_ID
from habits.models import Habit


@shared_task
def check_time():
    current_time = datetime.now().time().replace(second=0, microsecond=0)
    habits = Habit.objects.all()
    for habit in habits:
        if habit.time.replace(second=0, microsecond=0) == current_time:
            # Нужно узнать свой "chat_id" у бота @userinfobot.
            params = {'chat_id': {CHAT_ID}, 'text': f'Пользователю "{habit.user.email}" '
                                                    f'пора выполнить привычку: "{habit.action}".'}
            response = requests.post(f'{BOT_API}{BOT_API_KEY}/sendMessage', params)

            if response.status_code == 200:
                print("Сообщение успешно отправлено.")
            else:
                print(f"HTTP request failed with status code: {response.status_code}")
