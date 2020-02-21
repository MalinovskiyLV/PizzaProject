from decimal import Decimal
from django.conf import settings
from pzz.models import Pizza


class Basket(object):

    def __init__(self, request):
        self.session = request.session

        basket = self.session.get(settings.BASKET_SESSION_ID)

        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}

        self.basket = basket

    def add(self, pizza, quantity=1, update_quantity=False):
        pizza_id = str(pizza.id)

        if pizza_id not in self.basket:
            self.basket[pizza_id] = {'quantity': 0, 'price': str(pizza.price)}

        if update_quantity:
            self.basket[pizza_id]['quantity'] = quantity
        else:
            self.basket[pizza_id]['quantity'] += quantity

        self.save()

    def save(self, ):
        self.session[settings.BASKET_SESSION_ID] = self.basket

        self.session.modified = True

    def remove(self, pizza):
        pizza_id = str(pizza.id)

        if pizza_id in self.basket:
            del self.basket[pizza_id]
            self.save()

    def __iter__(self):
        pizza_ids = self.basket.keys()

        pizzas = Pizza.objects.filter(id_in=pizza_ids)

        for pizza in pizzas:
            self.basket[str(pizza.id)]['pizza'] = pizza

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True
