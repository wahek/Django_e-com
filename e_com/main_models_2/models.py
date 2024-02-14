from django.db import models

"""
Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа
"""


class Client(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=128)
    date_of_registration = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    date_of_edit = models.DateField(auto_now_add=True)


class Order(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    total_sum = models.IntegerField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
