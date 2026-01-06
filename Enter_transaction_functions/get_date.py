from datetime import datetime
def get_date() :
    while True :
       user_input = input("Enter date (YYYY-MM-DD): ")
       try:
           date_value=datetime.strptime(user_input,"%Y-%m-%d")
           print("valid time\n")
           break
       except ValueError:
             print("Invalid date format or invalid date. Try again.")
    return date_value
