from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

machine_ready=True
while(machine_ready):
    inp=input(f"Enter Your Option ({menu.get_items()}):")
    if(inp=="exit"):
        machine_ready=False
    elif(inp=="report"):
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(inp)
        if(not drink==None):
            if(coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)