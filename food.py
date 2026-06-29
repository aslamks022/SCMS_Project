# Food Ordering System
import csv
def menu():
    print("1.Display Menu")
    print("2.Place Order")
    print("3.Calculate Bill")
    print("4.Exit")
    menu()
    choice = input("Enter your choice:")
    print("1.Idli - 40 rupees")
    print("2.Dosa - 60 rupees")
    print("3.Meals - 100 rupees")
    print("4.Tea - 15 rupees")
    if choice == "1":
        display_menu()
def place_order():
    item = input("Enter food item: ")
    with open("menu.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item])
        print("Order Placed Successfully")
    elif choice == "2":
        place_order()
def calculate_bill():
    quantity = int(input("Enter Qunatity: "))
    price = 100
    total = quantity*price
    print("Total Bill:rupees",total)
    elif choice == "3":
        calculate_bill()
    elif choice == "4":
        print("Exiting Food Ordering System")
    print("---------------------------")
    if item == "":
        print("Food otem cannot be Empty")
        return
    print("Processing your order...")
    print("Thank you for ordering...")
    print("==== FOOD ORDERING SYSTEM ====")
 




