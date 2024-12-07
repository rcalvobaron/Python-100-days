

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""Program requirements
1. Print the report
2.Check resources are suficient
3.Process coins
4.Check transaction succesful
5.Make coffe
"""
coffe_maker=CoffeeMaker()
menu=Menu()
money_machine=MoneyMachine()




is_on=True

while is_on:
    choice = input(f"what would you like? {menu.get_items()}:  ").lower()

    if choice=="off":
        is_on=False
    elif choice=="report":
        #print report
        coffe_maker.report()
        money_machine.report()
    else:
        #make coffe if resourcs are suficient, deduct resources and ad up profit.
        drink=menu.find_drink(choice)
        print(drink.ingredients)

        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
