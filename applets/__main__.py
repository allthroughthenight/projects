from modules import budget as budget
# from modules import ip_addr as ip_addr
from modules import life_clock as life_clock
from modules import mastery as mastery
# from modules import ping as ping

if (__name__ == '__main__'):
    while True:
        print("Main Menu")
        print("1: Budget")
        print("2: Life Clock")
        print("3: Mastery")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            budget.run()
        elif choice == 2:
            life_clock.run()
        elif choice == 3:
            mastery.run()
