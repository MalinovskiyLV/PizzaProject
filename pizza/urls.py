"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

from basket import views
from pzz.views import *

urlpatterns = [
    path('pzz/', pizzas_list, name='pizzas_list_url'),
    path('admin/', admin.site.urls),
    re_path(r'^$', views.basket_detail, name='basket_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.basket_add, name='basket_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.basket_remove, name='basket_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

