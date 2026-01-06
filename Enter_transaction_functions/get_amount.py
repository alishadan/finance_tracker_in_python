from save_data.load_data import load_data
def get_amount() :
    while True:
        amount = input("please enter amount with tooman and press Enter\n")
        #chcke if amount is a number
        if not amount.isdigit():
            print("please enter a vlid number")
            continue
        #convert to int
        amount=int(amount)
        break
    return amount
