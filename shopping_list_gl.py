# Generosa's shopping list

# Shopping list
shopping_list = {"TJ":["milk","cheese"], "Lucky":["paper towel", "soap"], "Ace":["screwdriver","drill"]}

# 0
def user_menu():
    print "0 - Main Menu"
    print "1 - Show all lists."
    print "2 - Show a specific list."
    print "3 - Add a new shopping list."
    print "4 - Add an item to a shopping list."
    print "5 - Remove an item from a shopping list."
    print "6 - Remove a list by nickname."
    print "7 - Exit when you are done."

#1
def show_all_list():
    print shopping_list

#2
def show_spec_list(key):
    key = key.lower()
    if key in shopping_list:
        shopping_list = shopping_list_by_name[key]
        shopping_list.sort()
        return shopping_list
    else:
        None    
    

#3
def add_list():
    pass

#4
def add_item():
    pass

#5
def remove_item():
    pass

#6
def remove_list():
    pass

#7
def quit_prog():
    pass


def main():
    choice = user_menu()
    print shopping_list

    while True:
        #0
        if choice == 0:
            choice = user_menu()
         
        # 1
        elif choice == 1:
            choice= show_all_list()
            choice = 0
        #2
        elif choice == 2:
            list_store = raw_input("What store would you like to see: ")
            print show_spec_list(list_store)
            choice = 0

        # #3
        # elif choice == 3:
        #     choice = add_list()
        #     choice = 0

        # #4
        # elif choice == 4:
        #     choice = add_item()
        #     choice = 0

        # #5
        # elif choice == 5:
        #     choice = remove_item()
        #     choice = 0

        # #6
        # elif choice == 6:
        #     choice = remove_list()
        #     choice = 0

        # #7
        # elif choice == 7
        #     choice = quit_prog()



if __name__ == '__main__':
    main()
