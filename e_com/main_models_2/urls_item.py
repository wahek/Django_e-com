from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
]
