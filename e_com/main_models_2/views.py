import datetime

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from main_models_2.models import Item, Order, Client
from main_models_2.forms import ItemForm


def get_index(request):
    return render(request, 'main_models_2/index.html', context={'title': 'Главная'})


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


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Форма успешно заполнена!')
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'main_models_2/add_item.html', context={'title': 'Добавить новый товар',
                                                                   'form': form})


def update_item(request, pk):
    item = get_object_or_404(Item, id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Форма успешно обновлена!')
            return redirect('index')
    else:
        form = ItemForm(instance=item)
    return render(request, 'main_models_2/add_item.html', context={'title': 'Обновить товар',
                                                                   'form': form})
