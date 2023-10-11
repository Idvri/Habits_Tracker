from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            is_superuser=True,
            is_stuff=True,
        )
        user.set_password('Nodar126')
        user.save()
