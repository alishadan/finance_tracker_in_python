
def run_help():
	help_menu()
	while True:
		key_press=input("please enter a correct alphabet \n")
		if key_press=="E":
			exit()
		elif key_press=="B":
			return
		else:
			print("please enter a correct alphabet \n")

	

def help_menu():
	print(
		"###################################################################\n"
		"# welcome to HELP f finance tracker#\n"
		"# with finance tracker you can enter income and expences #\n"
		"# this program have a useful UI and you can go with menus#\n"
		"# files saved on your computer#\n"
		"# for any problem or have questions email to alishadan84@gmail.com#\n"
		"##\n"
		"###################################################################\n"
		"#       E (exit)                       #\n"
		"#       B (back to main menu)          #\n"
	)






