class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality


    def to_string(self):
        return f"{self.name}, {self.age}, {self.nationality}"
file_path = ('PERSONS_LIST.txt')


def load_data():
    try:
        with open(file_path, 'r') as file:
            for line in file:
                values = line.strip().split(', ')
                if len(values) == 3:
                    name, age, nationality = values
                    persons_list.append(Person(name, int(age), nationality))
                else:
                    print(f"Ignoring invalid line: {line}")
    except FileNotFoundError:
        print("The file was not found. ")


def save_data():
    with open(file_path, 'w') as file:
        for person in persons_list:
            file.write(person.to_string() + '\n')


def login_credentials():
    credentials = {}
    try:
        with open('credentials.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                credentials[username] = password
    except FileNotFoundError:
        print("File missing, please return to directory or replace to continue. ")
        quit()
    return credentials, username, password


def login():
    credentials = login_credentials()
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in credentials and credentials.get(username) == password:
            print("Login Successful! ")
            break
        else:
            print("Login Unsuccessful! ")
        

def main_menu():
    load_data()
    
    while True:
        try:
            menu = input("\n===== Main Menu =====\nA) Add person\nB) Find person\nC) Remove person\nD) Change username or password\nE) Exit\n")

            if menu.upper() == 'A':
                add_person()

            if menu.upper() == 'B':
                find_person()

            if menu.upper() == 'C':
                remove_person()


            if menu.upper() == 'D':
                pass

            if menu.upper() == 'E':
                quit()

            else:
                print("Invalid input, please choose a valid option (A, B , C , D, E) ")
                
        except ValueError:
            print("There was an error with the main menu! Please try again:")


def add_person():
    def get_new_person():
        name = input('Enter full name: ')
        while True:
            try:
                age = int(input('Enter age: '))
                if age < 18:
                    raise ValueError("Age must be over 18: ")
                break
            except ValueError:
                print("Age must be over 18: ")
        nationality = input('Enter nationality: ')

        return name, age, nationality
    

    def create_new_person(name, age, nationality):
        return Person(name, age, nationality)


    def save_new_person(person):
        persons_list.append(person)
        save_data()

    
    def add_another_new_person():
        loop = input("Do you want to add another person? Y/N: ")
        return loop == 'Y'


    while True:
        try:
            name, age, nationality = get_new_person()
            cont = input(f'Is this correct?\n{name}, {age}, {nationality}\nY/N or exit: ')
            
            if cont.upper() == 'Y':
                new_person = create_new_person(name, age, nationality)
                save_new_person(new_person)

            elif cont.upper() == 'N':
                continue

            elif cont.lower() == 'exit':
                break
            if not add_another_new_person():
                main_menu()

            
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except FileNotFoundError:
            print("File not found: ")
        except Exception as e:
            print(f"Erorr: {e}")


def find_person():
    while True:
        try:
            target = input("Enter the desired name to be searched: ")
            with open(file_path, 'r') as file:
                for line in file:
                    if target in line:
                        details = line.strip().split(', ')
                        print(f"\n{target} was found in the file.\nDetails: Name: {details[0]}, Age: {details[1]}, Nationality: {details[2]}\n")
                        cont = input("Would you like to search for another person? Y/N: ")
                        if cont == 'Y':
                            break
                        elif cont == 'N':
                            main_menu()                        
                            return
                        else:
                            print("Invalid input, please enter only 'Y' or 'N': ")
                    else:
                        while True:
                            fail_cont = input(f"\n{target} was not found In the file. Would you like to search another person? Y/N: \n")
                            if fail_cont == 'Y':
                                break

                            elif fail_cont == 'N':
                                main_menu()
                                return
                            else:
                                print("Invalid input, please enter only 'Y' or 'N': ")
                            find_person()
        except Exception as e:
            print(f"Error removing person: {e}")


def remove_person():
    try:
        target = input("Enter the name of the person you want to remove: ")

        with open(file_path, 'r') as file:
            lines = file.readlines()

        found = False
        new_lines = []
        #with open(file_path, 'w') as file:
        for line in lines:
            if target not in line.strip():
                new_lines.append(line)
                #file.write(line)
            else:
                found = True
                details = line.strip().split(', ')
                print(f"\n\n{details[0]}, Age: {details[1]}, Nationality: {details[2]}, has been removed: ")
        if not found:
            print(f"\n{target} was not found In the file.")
        else:
            with open(file_path, 'w') as file:
                file.writelines(new_lines)
    except FileNotFoundError:
        print("File not found: ")
    except Exception as e :
        print(f"Error: {e} ")


"""def change_credentials(credentials):
    while True:
        try:
            what_to_change = input("What do you want to change?\nA) USERNAME\nB) PASSWORD\nC) Main menu")
            if what_to_change == 'A':
                new_username = input("Enter new username: ")
                

            if what_to_change == 'B':

            if what_to_change == 'C':
        except ValueError:
            pass"""
            
    


persons_list = []


if __name__ == "__main__":
    login()
    main_menu()