from dest.actions import add_destination, print_destinations
from storage.load_save import load, save
from icecream import ic
my_destinations = []


def menu():
    load()
    while True:
        ic("1-add")
        ic("2-list")
        ic("3-exit")
        selection = input("Your command? ")
        if selection == "1":
            add_destination(my_destinations)
        if selection == "2":
            print_destinations(my_destinations)
            pass
        if selection == "3":
            save()
            exit()
if __name__ == "__main__":
    menu()
