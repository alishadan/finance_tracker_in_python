def about_menu():
	print("###############################\n"
		"# finance tracker program     #\n"
		"# whit this program you can enter expences and incomes an view them#\n"
		"# developed by Ali Shadan #\n"
		"# this project hosted in Github.com/alishadan#\n"
		"# emali: alishadan84@gmail.com#\n"
		"# website: http://ngarsh.ir#\n"
		"###############################\n"
		"# press E (exit) #\n"
		"# press B (back to main menu) #\n")

def run_about(): 
	about_menu();
	while True:
		key_press=input("please enter a correct alphabet \n")
		if key_press=="E":
			exit()
		elif key_press=="B":
			return
		else:
			print("please enter a correct alphabet \n")
