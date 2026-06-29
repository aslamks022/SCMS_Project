# Attendance Managemant System
import csv
print("==== ATTENDANCE MANAGEMENT SYSTEM ====")
def menu():
    print("1.Mark Attendance")
    print("2.Calculate Attendance")
    print("3.Display Student Details")
    print("4.Exit")
    menu()
    choice = input("Enter your choice:")
    def mark_attendance():
        name = input("Enter Student Name: ")
    status = input("Enter Attendance(present/Absent): ")
    with open("attendance.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name,status])
       print("Attendance Markes Successfully")
    if choice == "1":
        mark_attendance()
     calculate_attendance():
        total = int(input("Enter Total Classes: "))
        present = int(input("Enter Clases Attended:"))
        percentage = (present / total)*100
        print("Attendance Percentage:",percentage,"%")
    elif choice == "2":
        calculate_attendance()
def display_student():
    with open("attendance.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("Name:",row[0],"| Status:",row[1])
    elif choice == "4":
        print("Thank you")
    break
    else:
        print("Invalid Choice")
    print("-------------------------------")


