from django.core.management.base import BaseCommand
from random import randint
from main_models_2.models import Client


class Command(BaseCommand):
    help = 'Create client random'

    def handle(self, *args, **options):
        for i in range(10):
            client = Client(name=f'Name_{i}',
                            email=f'email_{i}@mail.ru',
                            phone_number=f'+7' + random_phone(),
                            address=f'City: {i}, Street: {i ** 2}, Building: {i ** 3}', )
            client.save()
            self.stdout.write(str(client.name))


def random_phone():
    res = ''
    for _ in range(10):
        res += str(randint(0, 9))
    return res
