
from clear import *
from view_transaction_functions.view_transaction import view_transaction
from Enter_transaction_functions.enter_transaction import enter_transaction
from help_functions.help import run_help
from about_function.about import run_about
def menu1():
	clear()
	print("##########################\n"
	"#press one key of bellow #\n"
	"# I (enter transaction)  #\n"
	"# V (view trans)         #\n"
	"# H      (help)          #\n"
	"# A     (about)          #\n"
	"# E      (exit)          #\n"
	"##########################\n");
def run_menu1():
	while True:
		menu1()
		key_press=input("please enter a correct key \n")
		if key_press=="I":
			clear()
			enter_transaction()
			clear()
			menu1()

		elif key_press=="V":
			clear()
			view_transaction()
			clear()
			menu1
		elif key_press=="H":
			clear()
			run_help()
			clear()
			menu1()
		elif key_press=="E":
			exit()
		elif key_press=="A":
			clear()
			run_about()
			menu1()
			clear()
		else:
			print("please enter a correct key")
	


