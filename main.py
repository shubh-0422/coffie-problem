import json
from coffee_machine.coffee_machine import CoffeeMachine

def coffee_machine():
   
    input_config_file = open("./resources/input.json", "r")
    input_config = json.load(input_config_file)
    
    try:
        coffee_machine = CoffeeMachine(input_config["machine"]["outlets"]["count_n"], input_config["machine"]["total_items_quantity"])
        coffee_machine.serve(input_config["machine"]["beverages"])
    except Exception as e:
        print("Unable to serve the beverages.\nReason: " + str(e))

if __name__ == "__main__":
    coffee_machine()