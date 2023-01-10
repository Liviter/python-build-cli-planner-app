from src.database import add_reminder, list_reminders, delete_reminders
from src.reminder import PoliteReminder
from src.deadlined_reminders import DeadlinedReminder


DeadlinedReminder.register(PoliteReminder)


def handle_input():
    choice = input("Choice: ")
    if choice == "4":
        return False

    if(choice == "1"):
        list_reminders()

    elif(choice == "2"):
        print()
        reminder = input("What would you like to be reminded about?: ")
        date = input("When is that due?: ")
        time = input("What time is it due?: ")

        add_reminder(reminder, date, time, PoliteReminder)
        list_reminders()

    elif(choice == "3"):
        delete_reminders()

    else:
        print("Invalid menu option")

    return True


def print_menu():
    print()
    print('|--------------|')
    print('|  Pluralsight |')
    print('|   Reminders  |')
    print('|     App      |')
    print('|--------------|')
    print('* * * * * * * * *')
    print('Please select an option:')
    print()
    print('1) List reminders')
    print('2) Add a reminder')
    print('3) Delete Reminders')
    print('4) Exit')


def main():
    print_menu()
    while handle_input():
        print_menu()


if __name__ == '__main__':
    main()
