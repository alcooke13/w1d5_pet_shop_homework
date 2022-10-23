# WRITE YOUR FUNCTIONS HERE
#Test #1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#Test #2

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

#Test #3 and #4

def add_or_remove_cash(shop, number):
   shop["admin"]["total_cash"]+= number
    
#Test #5

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
        
#Test #6

def increase_pets_sold(pet_shop, amount_increased):
    pet_shop["admin"]["pets_sold"] += amount_increased

#Test #7

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#Test #8
# Notes
# What -> Finding out how many pets of the same breed based on breed input
# How -> Iterate through pet_shop["pets"] to see if there is a match with breed input
#     -> If it matches append to breed_list which is an empty list

def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    for animal in pet_shop["pets"]:
        if breed == animal["breed"]:
            breed_list.append(animal["breed"])
    return breed_list

# Test #9/#10
# Notes
# Based on the name, loop through and find the list. if name matches -> print the key value pairs associated with the name. name: "" , pet_type: "" etc
def find_pet_by_name(pet_shop, name):
    for element in pet_shop["pets"]:
        if name == element["name"]:
            return element
    return None

# Test #11
# Notes 
# Based on the given name remove the dictionary associated with the name from the list
# iterate through with indices based on how many pets there are. Conditional if the name matches to reassign the dictionary to None  
def remove_pet_by_name(pet_shop, name):
    for i in range(len(pet_shop["pets"])):
        if pet_shop["pets"][i]["name"] == name:
            pet_shop["pets"][i]["name"] = None

# Test #12
# Add new pet dictionary to the list
# It's a list -> .append the new pet
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# Test #13

def get_customer_cash(customers):
    return customers["cash"]

# Test #14

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

# Test #15
def get_customer_pet_count(customer):
    return len(customer["pets"])

# Test #16
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# Test #17
def customer_can_afford_pet(customer, pet_cost):
    if customer["cash"] >= pet_cost["price"]:
        return True
    else:
        return False

# Test #18
# Notes ->
    # petcount for customer to go up
    # petsold for petshop to go up by 1 
    # customer cash should go down based on petcost
    # petshop admin cash should go up based on petcost
# def sell_pet_to_customer(pet_shop, customer, pet_name):
