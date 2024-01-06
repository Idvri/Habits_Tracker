import requests

from datetime import datetime

from celery import shared_task

from config.settings import BOT_API, BOT_API_KEY

from habits.models import Habit

from users.models import User


@shared_task
def check_user():
    res = requests.post(f'{BOT_API}{BOT_API_KEY}/getUpdates')
    users = User.objects.all()
    for member in res.json()['result']:
        if 'my_chat_member' in member:
            chat_id = member['my_chat_member']['chat']['id']
            telegram_username = member['my_chat_member']['chat']['username']
            if telegram_username in [user.telegram for user in users]:
                user = users.filter(telegram=telegram_username).first()
                if user and not user.chat:
                    user.chat = chat_id
                    user.save()
                    print(f'{user.telegram} - чат добавлен!')


@shared_task
def check_time():
    current_time = datetime.now().time().replace(second=0, microsecond=0)
    habits = Habit.objects.all()
    for habit in habits:
        if habit.time.replace(second=0, microsecond=0) == current_time:
            params = {
                'chat_id': habit.user.chat,
                'text': f'Пора выполнить привычку: "{habit.action}".'}
            response = requests.post(f'{BOT_API}{BOT_API_KEY}/sendMessage', params)

            if response.status_code == 200:
                print("Сообщение успешно отправлено.")
            else:
                print(f"HTTP request failed with status code: {response.status_code}")
