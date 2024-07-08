print("WELCOME TO COFFEE-CAFE")

from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine


coffee_maker =CoffeeMaker()
money_machine =MoneyMachine()
menu =Menu()



is_machine_off =False

while not is_machine_off:
    choice =input("enter off to machine to be off, report for current resources, coffee name fro order coffee ").lower()
    if choice =="off":
        is_machine_off =True
    elif choice =="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)  
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)      