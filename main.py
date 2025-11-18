from task_manager import TaskManager

def print_menu():
        print("\n---  Gestor de Tareas Inteligente ---")
        print("1. Añadir Tarea")
        print("2. Listar Tarea")
        print("3. Completar Tarea")
        print("4. Eliminar Tarea")
        print("5. Salir")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:

            choice = int(input("Elige una opcion: "))

            match choice:

                case "1":
                    description = input("Descripcion de la tarea: ")
                    manager.add_task(description)
                    
                case "2":
                    manager.list_task()

                case "3":
                    id = int(input("ID de la tarea a completar: "))
                    manager.complete_task(id)

                case "4":
                    id = input("Id de la tarea a Eliminar: ")
                    manager.delete_task(id)

                case "5":
                    print("Saliendo.....")
                    break

                case _:
                    print("Opcion no valida. Selecciona otra.")

        except ValueError:
            print("Opcion no valida. Selecciona otra.")

if __name__ == "__main__":
    main()
