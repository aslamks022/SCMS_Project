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
    
    

