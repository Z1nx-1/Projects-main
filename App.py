def credentials():
    global name, age, nationality, adult
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


def data_processing():
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

#
credentials()
data_processing()