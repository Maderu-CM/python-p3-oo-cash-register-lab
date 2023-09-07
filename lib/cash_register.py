#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        
        self.discount = discount
        self.items = []
        self.prices = []
        self.last_transaction = 0

    def add_item(self, item, price, quantity=1):
      
        self.items.extend([item] * quantity)
        self.prices.extend([price] * quantity)
        self.last_transaction = price * quantity

    def calculate_total(self):
        
        return sum(self.prices)

    def apply_discount(self):
       
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.calculate_total()
            return self.calculate_total() - discount_amount
        else:
            return self.calculate_total()

    def void_last_transaction(self):
     
        if self.last_transaction > 0:
            self.prices.pop()
            self.items.pop()
            self.last_transaction = 0

