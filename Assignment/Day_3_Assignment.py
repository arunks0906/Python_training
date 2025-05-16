std_detail = {} # Global variable

class Student:

    def __init__(self, name, id, dept, avg_mark, mobile_no): #constructor
        self.name = name
        self._id = id
        self.dept = dept
        self.avg = avg_mark
        self.__mobile_no = mobile_no

    def add(self): # TO add new student details
        data = {self._id: {"Name": self.name,"Department": self.dept,"Average": self.avg,"Mobile_No": self.__mobile_no}}
        std_detail.update(data)

    @staticmethod
    def update_data(change): #To update the record
        if change in std_detail:
            name = input("Enter the name: ")
            dept = input("Enter the Department: ")
            mark = int(input("Enter the average mark: "))
            mob_no = int(input("Enter the mobile number: "))
            std_detail[change] = {"Name": name,"Department": dept,"Average": mark,"Mobile_No": mob_no}
        else:
            print("Enter a valid ID of the student.")

    @staticmethod
    def delete(delete): #delete the record
        if delete in std_detail:
            del std_detail[delete]
        else:
            print("Enter a valid ID of the student.")

    @staticmethod
    def view(opt): #to display the records
        
        if opt in std_detail:
            print("Student Details:")
            print(std_detail[id])
        else:
            print("Invalid ID, Here is the full data.\n")
            print(std_detail)


if __name__ == "__main__":
    
    while True:
        try:
            choice = int(input("1.Add\n2.View\n3.Update\n4.Delete\n5.Exit\nEnter the choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter the name: ")
            id = int(input("Enter the ID: "))
            dept = input("Enter the Department: ")
            mark = int(input("Enter the average mark: "))
            mob_no = int(input("Enter the mobile number: "))
            std = Student(name, id, dept, mark, mob_no)
            std.add()

        elif choice == 2:
            opt=int(input("Enter the ID: "))
            Student.view(opt)

        elif choice == 3:
            change = int(input("Enter the ID to update: "))
            Student.update_data(change)

        elif choice == 4:
            delete = int(input("Enter the ID to delete: "))
            Student.delete(delete)

        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Please enter a valid choice from 1-5.")
