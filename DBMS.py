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
        pass


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
        pass
    return credentials


def login():
    credentials = login_credentials()
    print(credentials)
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
            menu = input("Menu:\nA) Add person\nB) Find person\nC) Remove person\nD) Change username or password\nE) Exit\n")
            if menu == 'exit':
                quit()

            if menu == 'A':
                add_person()

            if menu == 'B':
                find_person()

            if menu == 'C':
                remove_person()

            return menu
        except Exception as e:
            print(f"Error in main menu: {e}")


def add_person():
    while True:
        try:
            name = input('Enter full name: ')
            age = int(input('Enter age: '))
            nationality = input('Enter nationality: ')
            cont = input(f'Is this correct?\n{name, age, nationality}\nY/N: ')
            if cont == 'Y':
                new_person = Person(name, age, nationality)
                persons_list.append(new_person)
                save_data()
                break
            elif cont == 'N':
                continue
            main_menu()
        except ValueError:
            print("Please enter a valid age: ")
        except Exception:
            print(f"Erorr adding {new_person}")



def find_person():
    while True:
        try:
            target_name = input("Enter the desired name to be searched: ")
            with open(file_path, 'r') as file:
                for line in file:
                    if target_name in line:
                        details = line.strip().split(', ')
                        print(f"\n{target_name} found in the file.\nDetails: Name: {details[0]}, Age: {details[1]}, Nationality: {details[2]}\n")
                        main_menu()
                        return target_name
                else:
                    print(f"\n{target_name} not found In the file. \n")
                    find_person()
        except Exception as e:
            print(f"Error removing person: {e}")


def remove_person():
    try:
        target_name = input("Enter the name of the person you want to remove: ")

        with open(file_path, 'r') as file:
            lines = file.readlines()

        found = False
        with open(file_path, 'w') as file:
            for line in lines:
                if target_name not in line.strip():
                    file.write(line)
                else:
                    found = True
                    details = line.strip().split(', ')
                    print(f"\n\n{details[0]}, Age: {details[1]}, Nationality: {details[2]}, has been removed: ")
                    break     
        if not found:
            print(f"\n{target_name} was not found In the file.")
    except Exception:
        print(f"Error removing {target_name}:")


persons_list = []

login()
main_menu()
