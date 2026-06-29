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


