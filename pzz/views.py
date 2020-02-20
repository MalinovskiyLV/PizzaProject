from django.shortcuts import render

from .models import Pizza


def pizzas_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pzz/index.html', context={'pizzas': pizzas})


def basket(request):
    return render(request, 'pzz/basket.html')
