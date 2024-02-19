from django.shortcuts import render
from django.http import HttpResponse
from main_models_2.models import Item, Order, Client


def get_orders(request, pk):
    client = Client.objects.get(id=pk)
    orders = Order.objects.filter(id_client=pk)
    orders_list = []
    for order in orders:
        print(order.__dict__)
        items = order.id_item.all()
        print(items)
        orders_list.append({order: items})
    return render(request, 'main_models_2/orders.html',
                  context={'client_name': client.name, 'client_address': client.address, 'title': 'Заказы',
                           'orders_list': orders_list})
