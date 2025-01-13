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
	print('|  5): Export todo-list   6): Import todo-list   |')
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
		i = 0
		for items in lista:
			print('Index: ' + str(i) + lista[i])
			i+=1
		rem_index = int(input('Specify List Index To Remove:'))
		todo.remove_task(lista, rem_index)
		print('c2')
	elif choice == 3:
		print('c3')
		i = 0
		for items in lista:
			print(lista[i])
			i+=1
	elif choice == 4:
		status = False
	elif choice == 5:
		file_name = input('Specify file name to export to: ')
		export_file = open(file_name, 'a')
		
		for items in lista:
			export_file.write(items)

	else:
		print('Invalid choice')
		
	if status == True:
		init(status)
		
init(active)
