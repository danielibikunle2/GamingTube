#!/usr/bin/env python3
import ast

class Burger:
    def __init__(self, name, base_price, is_vegan):
        self.name = name
        self.base_price = float(base_price)
        self.toppings = []
        self.is_vegan = is_vegan

    def add_topping(self, topping_name, price_increase):
        self.toppings.append(topping_name)
        self.base_price += float(price_increase)
        
        # Correct logic: Bacon and Cheese make it non-vegan
        if topping_name in ["Bacon", "Cheese"]:
            self.is_vegan = False

    def __str__(self):
        return f"Burger({self.name}, price={self.base_price})"


class ComboDeal:
    def __init__(self):
        self.burgers = []                     # plural is better

    def add_burger(self, burger_obj):
        self.burgers.append(burger_obj)

    def apply_discount(self, percent):
        h = 1 - percent / 100
        for burger in self.burgers:
            burger.base_price *= h

    def get_vegan_options(self):
        vegan_names = []
        for burger in self.burgers:
            if burger.is_vegan:
                vegan_names.append(burger.name)
        return vegan_names


# ===================== Main Code =====================
s = ast.literal_eval(input())

combo = ComboDeal()

for item in s:
    # Create burger
    b = Burger(item["name"], item["price"], item["vegan"])
    
    # Add topping correctly
    topping_name, price_increase = item["extra"]
    b.add_topping(topping_name, price_increase)
    
    # Add to combo
    combo.add_burger(b)


# Expected operations
combo.apply_discount(10)
print(combo.get_vegan_options())