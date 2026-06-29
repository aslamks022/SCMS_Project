#Library Management System
import csv
def menu():
    print("1,Add Book")
    print("2,Search Book")
    print("3,Issue Book")
    print("4,Return Book")
    print("5,Exit")
    menu()
    choice = input("Enter your choice:")
def add_book():
    book = input("Enter Book Name:")
    with open("books.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book])
        print("Book Added Successfully")
    choice = input("Enter your choice:")
    if choice =="1":
        add_book()
def search_book():
    book = input("Enter Book Name to Search:")
    with open("books.csv","r") as file:
        reader = csv.reader(file)
        found = False
    for row in reader:
        if book == row[0]:
            found = True
        if found:
            print("Book Found")
        else:
            print("Book Not Found")
       if choice == "1":
           add_book()
        elif choice == "2":
            search_book()
def issue_bool():
    book = input("Enter Book Name to issue:"
                 print("Book Issued Succesfully")
       elif choice == "3":
            issue_book()
def return_book():
                 book = input("Enter Book name return:")
               print("Book Returned Succesfully")
       elif choice == "4":
                 return_book()
       elif choice == "5":
                 print("Exiting Library System...")
    print("==== LIBRARY MANAGEMENT SYSTEM ====")
       else:
                 print("Invalid Choice")
       if book =="":
                 print("Book Name cannot be Empty")
                 return
    print("Searching....")


 
