from __future__ import annotations
from abc import ABC, abstractmethod

class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self) -> Pizza:
        pass
    
class NYPizzaFactory(PizzaFactory):
    def create_pizza(self) -> NYPizza:
        return NYPizza()

class Pizza(ABC):
    def prepare(self):
        return 'prepare pizza'
    
    def bake(self):
        return 'bake pizza'

    def cut(self):
        return 'cut pizza'

    def box(self):
        return 'put pizza into box'

class NYPizza(Pizza):
    def useful_function_nypizza(self) -> str:
        return 'The result of NYPizza'


def order_pizza(factory: PizzaFactory) -> None:
    ny_pizza = factory.create_pizza()
    print(f'{ny_pizza.prepare()} \n {ny_pizza.bake()} \n {ny_pizza.cut()} \n {ny_pizza.box()}')
    

if __name__ == "__main__":
    order_pizza(NYPizzaFactory())