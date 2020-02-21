from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pzz.models import Pizza
from .basket import Basket
from .forms import BasketAddPizzaForm


@require_POST
def basket_add(request, pizza_id):
    basket = Basket(request)
    pizza = get_object_or_404(Pizza, id=pizza_id)
    form = BasketAddPizzaForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        basket.add(pizza=pizza, quantity=cd['quantity'], update_quantity=cd['update'])

    return redirect('basket:basket_detail')


def basket_remove(request, pizza_id):
    basket = Basket(request)
    pizza = get_object_or_404(Pizza, id=pizza_id)
    basket.remove(pizza)
    return redirect('basket:basket_detail')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})
