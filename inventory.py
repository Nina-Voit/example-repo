import os

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)


    def get_cost(self):
        cost = self.cost
        return cost
        

    def get_quantity(self):
       quantity = self.quantity
       return quantity
    
    def to_csv_line(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    def __str__(self):
        return f"Country: {self.country}    Code: {self.code}    Product: {self.product}    Cost: {self.cost}    Stock: {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    # The below is another approach, but opted for the one we've
    # covered in the lectures
    # csv = pd.read_csv("inventory.txt")
    # shoe_list = [Shoe(x[0], x[1], x[2], x[3], x[4]) for x in csv.values]

    # Try with open(inventory.txt) as file ....

    try:
        file = open("inventory.txt")
        for s in file.readlines()[1:]:
            x = s.split(",")
            shoe_list.append(Shoe(x[0], x[1], x[2], x[3], x[4]))
    
    except FileNotFoundError:
        print("The file outlined in this function is not found")



def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("\nPlease enter the country the product is located in: ")
    code = input("Please enter the code of the product: ")
    product = input("Please enter the name of the product: ")
    while True:
        try:
            cost = float(input("Please enter the cost of the product: ")) 
            break
        except ValueError:
            print("Oops! That's not a valid price format. Please try entering" \
                    " the number with no other symbols (eg. 100): ")    
    while True:
        try:
            quantity = int(input("Please enter the quantity of the stock: ")) 
            break
        except ValueError:
            print("Oops! That's not a valid quantity format. Please try entering" \
                    " the whole number with no other symbols (eg. 10): ")    
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print("\nThe new category of shoe was successfully added to the list")

    update_inventory(shoe_list)


def view_all():
    print("\n Printing out all the items in the list of shoes")
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Need to overwrite the changes to this list in the list itself
    
    sorted_shoe_list = sorted(shoe_list, key= lambda shoe: shoe.quantity)
   

    print(sorted_shoe_list[0])
    while True:
        try:
            restock = int(input("\nPlease " \
                    "enter the amount you would like" \
                    " to order to stock: "))
            break
        except ValueError:
            restock = print("Oops! That's not a valid price format. Please try entering" \
                    " the number with no other symbols (eg. 100).")    

    sorted_shoe_list[0].quantity += restock

    print(sorted_shoe_list[0])

    update_inventory(shoe_list)
    
    print("\nYour inventory file has been updated with the restocked quantity!")
    

def search_shoe(): #Need to look into this further
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    code = input("Please input the code of the product you'd like to look up: ")

    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return 
    print(f"\nShoe with code {code} is not found in this inventory")
    

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        print("\n")
        print(shoe)
        print(f"The total cost for the {shoe.product} in {shoe.country} is: £{total_value}")


def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    sorted_shoe_list_discount = sorted(shoe_list, key= lambda shoe: shoe.quantity)
    print(sorted_shoe_list_discount[-1])

    while True:
        try:
            discount = int(input("Please enter the discount amount here: ")) 
            break
        except ValueError:
            print("Oops! That didn't work. Please enter a valid discount as a" \
            "whole number without any additional symbols (eg. 15)")

    sorted_shoe_list_discount[-1].cost *= (1 - discount/100)

    print(f"The new price per pair of shoes after applying a {discount}% is £{sorted_shoe_list_discount[-1].cost}")

    update_inventory(shoe_list)

    print("\nYour inventory has now been updated with the new price!")

def update_inventory(shoe_list):
    '''
    Created a helper function to save the updates to the txt file for
    the inventory.
    '''
    string_shoes = [s.to_csv_line() for s in shoe_list]
    file_content_to_write = "Country,Code,Product,Cost,Quantity"

    for s_s in string_shoes:
        file_content_to_write += (os.linesep + s_s)

    with open("inventory.txt", "w") as file:
        file.write(file_content_to_write)

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

read_shoes_data() # putting this here to pre-populate the list that each of the options works with

print("Hello and welcome to your inventory app!")

while True:
    user_choice = int(
        input(
            """\n Please select from the menu below.
            
    What would you like to:
    1. Add new item to the inventory
    2. View all items in the inventory 
    3. Restock the item with the lowest stock
    4. Search the shoe in the inventory
    5. See the total value per item for the whole inventory
    6. Apply a custom discount to the item with the highest quantity
    7. Quit the app

    Enter selection: """
        )
    )

    if user_choice == 1:
        capture_shoes()

    elif user_choice == 2:
        view_all()

    elif user_choice == 3:
        re_stock()

    elif user_choice == 4:
        search_shoe()
    
    elif user_choice == 5:
        value_per_item()
    
    elif user_choice == 6:
        highest_qty()
    
    elif user_choice == 7:
        print("Closing the app... Bye for now!")
        break

    else:
        print("Oops! Incorrect input, try again.")