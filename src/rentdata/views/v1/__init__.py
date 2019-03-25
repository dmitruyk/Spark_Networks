from django.conf.urls import url
from .load_data import load_data, index
from .company import search


urlpatterns = [
    # Получаем версию куков
    url(r'^load_data/', load_data),
    url(r'^index/', index),
    url(r'^search/', search),


]
