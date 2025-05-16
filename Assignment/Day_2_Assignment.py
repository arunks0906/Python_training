# Function used to write in the file.

def write_file(file_name,data):
    file= open (file_name, "w")
    file.write(data)
    file.close()

# Function used to read the file.

def read_file(file_name):
    try:
        with open (file_name, "r") as file:
                return(file.read())
    except FileNotFoundError:
        return("Error: File not found.")
    
#Function used to append the content in file.

def append_file(file_name,data):
    file=open(file_name,"a")
    file.write(data)
    file.close()

if __name__ == '__main__':

    file_name=input("Enter the file name: ")        #to get the file name from the user

    while True:       # Repeat until when the user types 4
            
        choice=int(input("\n1.Write in file\n2.Read the file\n3.Append the file\n4.Exit\nEnter the choice:"))   # To get the cohice from user

        if choice== 1:
            data=input("\nWrite the content here: ")
            write_file(file_name,data)
            print("\nSuccessfully completed the process.\n")

        elif choice==2:
            print(f"\n{file_name}:\n",read_file(file_name))

        elif choice==3:
            data=input('\nWrite the content to add in the file: ')
            append_file(file_name,data)
            print('\nSuccessfully completed the process.\n')

        elif choice==4:
            print('\nThank You!')
            break

        else:
            print("\nEnter the valid choice.")
            continue

