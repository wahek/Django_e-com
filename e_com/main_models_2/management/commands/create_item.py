from django.core.management.base import BaseCommand
from random import randint
from django.utils import lorem_ipsum
from main_models_2.models import Item


class Command(BaseCommand):
    help = 'Create client random'

    def handle(self, *args, **options):
        for i in range(10):
            item = Item(name=f'Item_{i}',
                        description=''.join(lorem_ipsum.paragraphs(randint(1, 4))),
                        price=1000 + i ** randint(1, 3),
                        count=randint(0, 10), )
            item.save()
            self.stdout.write(str(item.name))

