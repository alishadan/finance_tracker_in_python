from clear import *
from view_transaction_functions.totoal_amount import total_amount
from view_transaction_functions.search_by_date import search_by_date
from view_transaction_functions.search_by_kind import search_by_kind
def menu_view_transaction():
	clear()
	print(
	"##########################\n"
	"#press one key of bellow #\n"
	"# A (total amounts)      #\n"
	"# K (search by kind)     #\n"
	"# D (search by date)     #\n"
	"# B (back to main menu)  #\n"
	"# E (exit)               #\n"
	"##########################\n");
    
def view_transaction():
	menu_view_transaction()
	while True:
		menu_view_transaction()
		key_press=input("please enter a key\n")
		if key_press=="A":
			total_amount()
		if key_press=="K":
			search_by_kind()
		if key_press=="D":
			search_by_date()
		if key_press=="B":
			return
		if key_press=="E":
			exit

		
