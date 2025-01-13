import todo

lista = []

global active
active = True

def init(status):
	print('+------------------------------------------------+') # fancy menu
	print('|       [Welcome to TODO-main.py]                |')
	print('|                                                |')
	print('| Choose one of the following:                   |')
	print('|                                                |')
	print('|  1): Add new task     2): Remove task          |')
	print('|                                                |')
	print('|  3): View tasks     4): Exit TODO app          |')
	print('|                                                |')
	#print('|  5): Export todo-list   6): Import todo-list   |')
	print('|                                                |')
	print('|                           /!\ User Input       v')
	choice = input('+----------------------------------------------->')

	try:
		int(choice)
	except:
		print('Invalid input, not a number')
	else:
		choice = int(choice)

	if choice == 1:
		print('c1')
		todo.add_task(lista)
	elif choice == 2:
		print('c2')
	elif choice == 3:
		print('c3')
		i = 0
		for items in lista:
			print(lista[i])
			i+=1
	elif choice == 4:
		status = False
	else:
		print('Invalid choice')
		
	if status == True:
		init(status)
		
init(active)
