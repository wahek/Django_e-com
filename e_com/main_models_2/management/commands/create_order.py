import random

from django.core.management.base import BaseCommand
from random import randint
from main_models_2.models import Order, Item, Client


class Command(BaseCommand):
    help = 'Create orders random'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.get(id=pk)
        items = Item.objects.all()
        count = randint(1, 3)
        current = random.choices(items, k=count)
        order = Order(id_client=client)
        order.save()
        order.id_item.set(current)
        cur_sum = 0
        for cur in current:
            cur_sum += cur.price
        order.total_sum = cur_sum
        order.save()
        return 'OK'
