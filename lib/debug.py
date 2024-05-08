#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    customer = Customer("Sleepy")
    customer_2 = Customer("Toad")
    coffee = Coffee("Latte")
    coffee_2 = Coffee("Frappe")
    price = 3.0

    Order(customer, coffee, price)
    Order(customer, coffee_2, price)
    Order(customer_2, coffee, price)

    ipdb.set_trace()
