print("Hello, welcome to Notepad test!")


def menu_func():
    menu = input("What would you like to use? \nA) Write: \nB) Read back notes: \nC) Clear Notes: ")
    return menu


def write_func(menu):
    
    if menu == 'A' or 'a':
        print('\n')
        f = open('Notepad.txt', 'a')
        print("You have chosen to write! ")
        write = input("What would you like to write: ")
        f.write(write)
        f.write('\n')
        f.close()


def read_func(menu):
    if menu == 'B' or 'b':
        f = open('Notepad.txt', 'r')
        read = f.read()
        print("\n\nYour notes are:\n", str(read), '\n\n')
        f.close()


def clear_func(menu):
        if menu == 'C' or 'c':
            caution = input("Are you sure you want to delete your notes, this Is irreversable. Y/N: ")
            if caution == 'Y':
                f = open('Notepad.txt', 'w')
                f.write('')
                print('\nYour notes have been cleared!\n')
            if caution == 'N':
                print('Canceled: ')


while True:
    menu = menu_func()
    write_func(menu)
    read_func(menu)
    clear_func(menu)