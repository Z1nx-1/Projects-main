from UserClass import userclass


def credentials():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    nationality = input("Please enter your nationality: ")
    adult = True
    if age >= 18:
        print("Adult")
    elif age <= 18:
            adult = False
            print("Non-Adult")
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
            print(name, age, nationality, adult)
            true = input("Is this correct? Y/N: ")
            if true == 'Y':
                correct = True


credentials()
