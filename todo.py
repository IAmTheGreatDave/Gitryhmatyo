def view_tasks( lista ):
    if lista:
        for idx,data in enumerate(lista):
            print(f'( {idx} ) {lista[idx]}')
    else:
        print('Congrats. No tasks.')


def add_task(lista):
    task = input("Give task: ")
    lista.append(task)


