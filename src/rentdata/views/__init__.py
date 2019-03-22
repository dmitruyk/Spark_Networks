from django.conf.urls import url, include
from . import v1

urlpatterns = [
    url(r'^v1/', include(v1.urlpatterns)),

]