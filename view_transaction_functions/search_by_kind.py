from clear import *
from save_data.load_data import stream_data
def search_by_kind():
    menu_search_by_kind()
    kind_income=input("please enter kind of income\n")
    sum_amount_kind=sum_amount_kind_function(kind_income)
    print(f"total of amount is:{sum_amount_kind}")
    while True:
        key_press=input("\nenter a key B or E \n")
        if key_press=="B":
            return
        if key_press=="E":
            exit
def menu_search_by_kind():
    clear()
    print(
        "############################\n"
        "# B (Back)                 #\n"
        "# E (exit)                 #\n"
        "############################\n"
        )
def sum_amount_kind_function(kind_income:str):
    sum_amount=0
    for t in stream_data():
        if t.type_trans==kind_income:
            sum_amount+=t.amount
    return sum_amount
