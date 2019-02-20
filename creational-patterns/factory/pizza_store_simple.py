from __future__ import annotations
from abc import ABC, abstractmethod

class PizzaFactory(ABC):
    def create_pizza(self, topping) -> Pizza:
        if topping == 'Seafood':
            return SeafoodPizza()
        elif topping == 'HA':
            return HawaiianPizza()

class Pizza(ABC):
    def prepare(self):
        return 'prepare pizza'
    
    def bake(self):
        return 'bake pizza'

    def cut(self):
        return 'cut pizza'

    def box(self):
        return 'put pizza into box'

class SeafoodPizza(Pizza):
    def topping(self):
        return f'topping is Seafood'

class HawaiianPizza(Pizza):
    def topping(self):
        return f'topping is Hawaiian'

def order_pizza() -> None:
    menu = {
        'seafood_cocktail': 'Seafood',
        'ha': 'HA'
    }

    seafood_pizza = PizzaFactory().create_pizza(menu['seafood_cocktail'])
    print(f'{seafood_pizza.prepare()}\n{seafood_pizza.bake()}\n{seafood_pizza.cut()}\n{seafood_pizza.box()}\n{seafood_pizza.topping()}')
    print('*'*60)
    ha_pizza = PizzaFactory().create_pizza(menu['ha'])
    print(f'{ha_pizza.prepare()}\n{ha_pizza.bake()}\n{ha_pizza.cut()}\n{ha_pizza.box()}\n{ha_pizza.topping()}')
    
if __name__ == "__main__":
    order_pizza()