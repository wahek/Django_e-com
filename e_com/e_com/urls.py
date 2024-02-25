from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('main_models_2.urls_order')),
    path('item/', include('main_models_2.urls_item')),
]
