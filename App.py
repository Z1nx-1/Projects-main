
def login_func():
    print("Hello & welcome to my program!: ")
    username = 'Z!NX'
    password = 'Echo3'
    start = input("Do you have an existing login? Y/N: ")
    if start  == 'Y':
        user_entered_username = input("Enter username: ")
        user_entered_password = input("Enter password: ")
        if user_entered_username == username and user_entered_password == password:
            print("Correct login, continueing: ")
        else:
            print("Incorrect: ")
            quit()
    if start == 'N':
        print("Continueing")


def credentials():
    global user_data, name, age, nationality, adult
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    nationality = input("Please enter your nationality: ")
    adult = True
    print (name, age, nationality)
    if age >= 18:
        print("Adult")
    elif age <= 18:
            adult = False
            print("Non-Adult")
    incorrect = input("Is this correct? Y/N: ")
    if incorrect == "Y":
        print("Continueing")
    elif incorrect == "N":
        correct = False
        while correct == False:
            name = input("Please enter your name: ")
            age = int(input("Please enter your age: "))
            nationality = input("Please enter your nationality: ")
            true = input("Is this correct? Y/N: ")
            print(name, age, nationality, adult)
            if true == 'Y':
                correct = True
        print (name, age, nationality, adult)
    user_data = (name, age, nationality, adult)


def data_processing():
    data_processing = input("Would you like to save your data? Y/N: ")
    if data_processing == 'Y':
        data_processing = open("user_data.txt", "w")
        data_processing.write(name)
        data_processing.write("\n")
        data_processing.write(str(age))
        data_processing.write("\n")
        data_processing.write(nationality)
        data_processing.write("\n")
        if adult == True:
            data_processing.write("Adult")
        if adult == False:
            data_processing.write("Non-Adult")
        data_processing.close()
        print("Your data has been saved!: ")
    elif data_processing == 'N':
        print("Data has not been saved: ")


login_func ()  
credentials()
data_processing()
