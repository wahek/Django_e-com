import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from main_models_2.models import Item, Order, Client


def get_orders(request, pk, time=None):
    client = Client.objects.get(id=pk)
    orders = Order.objects.filter(id_client=pk)
    orders_list = []
    for order in orders:
        items = order.id_item.all()
        orders_list.append({order: items})
    return render(request, 'main_models_2/orders.html',
                  context={'client_name': client.name, 'client_address': client.address,
                           'title': 'Заказы', 'period': 'Заказы за всё время', 'orders_list': orders_list})


def get_orders_by_time(request, pk):
    if request.GET.get('time'):
        print('get')
        if request.GET.get('time') == 'week':
            time: datetime.timedelta = datetime.timedelta(days=7)
            period = 'неделю'
        elif request.GET.get('time') == 'month':
            time: datetime.timedelta = datetime.timedelta(days=30)
            period = 'месяц'
        elif request.GET.get('time') == 'year':
            time: datetime.timedelta = datetime.timedelta(days=365)
            period = 'год'
        else:

            return get_orders(request, pk)
        client = Client.objects.get(id=pk)
        orders = Order.objects.filter(id_client=pk)
        orders_list = []
        for order in orders:
            cur_time = datetime.datetime.now().replace(microsecond=0)
            try:
                order_time = order.date_of_creation.replace(microsecond=0, tzinfo=None)
                if cur_time - order_time < time:
                    items = order.id_item.all()
                    orders_list.append({order: items})
            except AttributeError:
                pass
        return render(request, 'main_models_2/orders.html',
                      context={'client_name': client.name, 'client_address': client.address,
                               'title': 'Заказы', 'period': f'Заказы за {period}', 'orders_list': orders_list})
    else:
        return get_orders(request, pk)
