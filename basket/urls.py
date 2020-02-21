from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.basket_detail, name='basket_detail'),
    re_path(r'^add/(?P<pizza_id>\d+)/$', views.basket_add, name='basket_add'),
    re_path(r'^remove/(?P<pizza_id>\d+)/$', views.basket_remove, name='basket_remove'),
]