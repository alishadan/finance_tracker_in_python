from clear import *
import transaction
from Enter_transaction_functions.enter_trans import enter_trans
from save_data.save_data import save_data
def menu_enter_transaction():
    clear()
    print(
        "#############################\n"
        "# A (enter transaction)    #\n"
        "# B (back to main menu)     #\n"
        "# E (end)                   #\n"
        "#############################\n"
        )
def enter_transaction():
    while True:
        menu_enter_transaction()
        key_press=input("please enter a correct alphabet \n")
        if key_press=="E":
            exit()
        elif key_press=="B":
            return
        elif key_press=="A":
            enter_list_of_transactions()
            menu_enter_transaction()
        else:
            print("please enter a correct alphabet \n")
def enter_list_of_transactions():
    #create a list of transactions
    while True:
        trans=enter_trans()
        save_data(trans)
        return





