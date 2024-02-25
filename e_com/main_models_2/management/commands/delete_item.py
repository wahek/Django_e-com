from django.core.management.base import BaseCommand
from main_models_2.models import Item


class Command(BaseCommand):
    help = 'Delete item by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        Item.objects.filter(id=pk).delete()
        return f'Товар с ID:{pk} удалён.'
