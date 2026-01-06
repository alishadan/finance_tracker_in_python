from clear import *
from datetime import datetime
from save_data.load_data import stream_data
def search_by_date():
    menu_search_by_date()
    print ("for sum of amount between tow date please enter first and last date\n")
    first_date=input("Enter first date (YYYY-MM-DD): \n")
    last_date=input("Enter last date (YYYY-MM-DD): \n")

    sum_amount_date=sum_amount_function_date(first_date,last_date)

    print(f"total of amount is:{sum_amount_date}")
    while True:
        key_press=input("enter a key: B or E  \n")
        if key_press=="B":
            return
        if key_press=="E":
            exit
def menu_search_by_date():
    clear()
    print(
        "############################\n"
        "# B (Back)                 #\n"
        "# E (exit)                 #\n"
        "############################\n"
        )

def sum_amount_function_date(start_date:str,end_date:str)->float:
    try:
        start = datetime.fromisoformat(start_date)
        end= datetime.fromisoformat(end_date)
    except:
        print("❌ Invalid date format. Please use YYYY-MM-DD (e.g., 2025-01-31).")
        return 0.0
    sum_total=0.0
    for t in stream_data():
        if start<=t.date_trans <=end:
            sum_total+=t.amount
        
    return sum_total
