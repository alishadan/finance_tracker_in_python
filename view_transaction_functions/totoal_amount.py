from clear import *
from save_data.load_data import stream_data
import json
def total_amount():
    menu_total_amount()
    sum_amount=sum_amount_function()
    print(f"total of amount is:{sum_amount}")
    while True:
        key_press=input("enter a key \n")
        if key_press=="B":
            return
        if key_press=="E":
            exit
def menu_total_amount():
    clear()
    print(
        "##########################\n"
        "# B (back)               \n"
        "# E(exit)                \n"
        "#########################\n"
        )
def sum_amount_function():
    sum_total=0
    #read data from trans.jsonl
    for t in stream_data():
        sum_total+=t.amount
    return sum_total
