from django.core.management.base import BaseCommand
from main_models_2.models import Client


class Command(BaseCommand):
    help = 'Delete client by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        Client.objects.filter(id=pk).delete()
        return f'Клиент с ID:{pk} удалён.'
