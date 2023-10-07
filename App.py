def username_password():
    username = "Z!NX"
    password = "Echo3"
    return username, password


def incoming_username_password(username, password):
    incoming_username = input("Enter username: ")
    incoming_password = input("Enter pssword: ")
    if incoming_username == username and incoming_password == password:
        print("Succesful login!: ")
    elif incoming_username != username or incoming_password == password:
        print("Unvalid login: ")
        quit()


def credentials():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    nationality = input("Please enter your nationality: ")
    if age >= 18:
        adult = "Adult"
    if age <= 18:
        adult = "Non adult"
    print(name, age, nationality, adult)
    incorrect = input("Is this correct? Y/N: ")
    if incorrect == "Y":
        print("Continueing")
    elif incorrect == "N":
        correct = False
        while correct == False:
            name = input("Please enter your name: ")
            age = int(input("Please enter your age: "))
            nationality = input("Please enter your nationality: ")
            if age >= 18:
                adult = "Adult"
            if age <= 18:
                adult = "Non adult"
            print(name, age, nationality, adult)
            true = input("Is this correct? Y/N: ")
            if true == 'Y':
                correct = True
    return name, age, nationality, adult


def data_processing(name, age, nationality, adult):
    data_processing = open("user_data.txt", "w")
    data_processing.write(name)
    data_processing.write("\n")
    data_processing.write(str(age))
    data_processing.write("\n")
    data_processing.write(nationality)
    data_processing.write("\n")
    data_processing.write(adult)
    data_processing.write("\n")
    data_processing.close()


username, password = username_password()
incoming_username_password(username, password)
name, age, nationality, adult = credentials()
data_processing(name, age, nationality, adult)