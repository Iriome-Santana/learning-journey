"""Simple To-Do List Application"""

import os
import json
"""Variable to store tasks"""
tasks = []

FILE_NAME = "tasks.json"

def load_tasks():
    global tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    else:
        tasks = []
        
def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)



def add_task():
    """Adds a new task to the to-do list after validation."""
    
    if len(tasks) >= 10:
        print("No se pueden agregar mas tareas")
        return
    task = input("\nIngrese una tarea: ")
    if task in tasks:
        print("La tarea ya existe")
        return
    if not task.strip():
        print("La tarea no puede estar vacia")
        return
    else:
        tasks.append(task)
        save_tasks()
        print("Tarea agregada")

def show_tasks():
    """Displays all tasks in the to-do list."""
    if not tasks:
        print("No hay tareas en la lista")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def delete_task():
    """Deletes a task from the to-do list based on user input."""

    if not tasks:
        print("No hay tareas para eliminar")
        return
    print("\n----Tareas----:")
    show_tasks()
    task = input("Ingrese el índice de la tarea a eliminar: ")
    
    if not task.isdigit():
        print("Índice no válido")
        return
    
    if int(task) - 1 < len(tasks):
        tasks.pop(int(task) - 1)
        save_tasks()
        print("Tarea eliminada")
    else:
        print("Tarea no encontrada")

        
print("Bienvenido al to-do list")

def main():
    """Displays the menu and handles user input for the to-do list application."""
    while True:
        print("\nMenu:")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        option = input("Ingrese una opcion: ")
    
        if option == "1":
            add_task()

        elif option =="2":
            print("\n----Tareas----:")
            show_tasks()

        elif option =="3":
            delete_task()

        elif option =="4":
            print("Gracias por su visita...")
            break

        else:
            print("\nOPCIÓN NO VÁLIDA, INTENTE DE NUEVO")
            
if __name__ == "__main__":
    load_tasks()
    main()
        