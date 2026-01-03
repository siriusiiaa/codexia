#!/usr/bin/env python3
"""
Aplicación de Gestión de Tareas (TODO)
Ejemplo de aplicación creada con Claude Code
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class TodoApp:
    """Clase principal para gestionar tareas"""

    def __init__(self, data_file: str = "todos.json"):
        self.data_file = data_file
        self.todos: List[Dict] = []
        self.load_todos()

    def load_todos(self) -> None:
        """Cargar tareas desde archivo JSON"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.todos = json.load(f)
            except json.JSONDecodeError:
                print(f"Error al leer {self.data_file}. Iniciando con lista vacía.")
                self.todos = []
        else:
            self.todos = []

    def save_todos(self) -> None:
        """Guardar tareas en archivo JSON"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.todos, f, indent=2, ensure_ascii=False)

    def add_todo(self, title: str, description: str = "") -> Dict:
        """Agregar una nueva tarea"""
        todo = {
            "id": len(self.todos) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save_todos()
        return todo

    def get_todos(self, completed: Optional[bool] = None) -> List[Dict]:
        """Obtener lista de tareas, opcionalmente filtradas por estado"""
        if completed is None:
            return self.todos
        return [todo for todo in self.todos if todo["completed"] == completed]

    def get_todo(self, todo_id: int) -> Optional[Dict]:
        """Obtener una tarea específica por ID"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, title: Optional[str] = None,
                    description: Optional[str] = None,
                    completed: Optional[bool] = None) -> Optional[Dict]:
        """Actualizar una tarea existente"""
        todo = self.get_todo(todo_id)
        if todo:
            if title is not None:
                todo["title"] = title
            if description is not None:
                todo["description"] = description
            if completed is not None:
                todo["completed"] = completed
            todo["updated_at"] = datetime.now().isoformat()
            self.save_todos()
            return todo
        return None

    def delete_todo(self, todo_id: int) -> bool:
        """Eliminar una tarea"""
        todo = self.get_todo(todo_id)
        if todo:
            self.todos.remove(todo)
            self.save_todos()
            return True
        return False

    def clear_completed(self) -> int:
        """Eliminar todas las tareas completadas"""
        initial_count = len(self.todos)
        self.todos = [todo for todo in self.todos if not todo["completed"]]
        self.save_todos()
        return initial_count - len(self.todos)


def print_todo(todo: Dict) -> None:
    """Imprimir una tarea de forma legible"""
    status = "✓" if todo["completed"] else "○"
    print(f"{status} [{todo['id']}] {todo['title']}")
    if todo['description']:
        print(f"    {todo['description']}")


def main():
    """Función principal - interfaz de línea de comandos"""
    app = TodoApp()

    while True:
        print("\n" + "="*50)
        print("GESTOR DE TAREAS - TODO APP")
        print("="*50)
        print("1. Ver todas las tareas")
        print("2. Ver tareas pendientes")
        print("3. Ver tareas completadas")
        print("4. Agregar nueva tarea")
        print("5. Marcar tarea como completada")
        print("6. Editar tarea")
        print("7. Eliminar tarea")
        print("8. Limpiar tareas completadas")
        print("9. Salir")
        print("="*50)

        choice = input("\nSelecciona una opción: ").strip()

        if choice == "1":
            todos = app.get_todos()
            if todos:
                print("\nTODAS LAS TAREAS:")
                for todo in todos:
                    print_todo(todo)
            else:
                print("\nNo hay tareas registradas.")

        elif choice == "2":
            todos = app.get_todos(completed=False)
            if todos:
                print("\nTAREAS PENDIENTES:")
                for todo in todos:
                    print_todo(todo)
            else:
                print("\n¡No hay tareas pendientes! 🎉")

        elif choice == "3":
            todos = app.get_todos(completed=True)
            if todos:
                print("\nTAREAS COMPLETADAS:")
                for todo in todos:
                    print_todo(todo)
            else:
                print("\nNo hay tareas completadas.")

        elif choice == "4":
            title = input("Título de la tarea: ").strip()
            if title:
                description = input("Descripción (opcional): ").strip()
                todo = app.add_todo(title, description)
                print(f"\n✓ Tarea creada con ID: {todo['id']}")
            else:
                print("\n✗ El título no puede estar vacío.")

        elif choice == "5":
            try:
                todo_id = int(input("ID de la tarea a completar: "))
                if app.update_todo(todo_id, completed=True):
                    print(f"\n✓ Tarea {todo_id} marcada como completada.")
                else:
                    print(f"\n✗ No se encontró la tarea con ID {todo_id}.")
            except ValueError:
                print("\n✗ ID inválido.")

        elif choice == "6":
            try:
                todo_id = int(input("ID de la tarea a editar: "))
                todo = app.get_todo(todo_id)
                if todo:
                    print(f"\nTarea actual: {todo['title']}")
                    new_title = input("Nuevo título (Enter para mantener): ").strip()
                    new_desc = input("Nueva descripción (Enter para mantener): ").strip()

                    app.update_todo(
                        todo_id,
                        title=new_title if new_title else None,
                        description=new_desc if new_desc else None
                    )
                    print(f"\n✓ Tarea {todo_id} actualizada.")
                else:
                    print(f"\n✗ No se encontró la tarea con ID {todo_id}.")
            except ValueError:
                print("\n✗ ID inválido.")

        elif choice == "7":
            try:
                todo_id = int(input("ID de la tarea a eliminar: "))
                if app.delete_todo(todo_id):
                    print(f"\n✓ Tarea {todo_id} eliminada.")
                else:
                    print(f"\n✗ No se encontró la tarea con ID {todo_id}.")
            except ValueError:
                print("\n✗ ID inválido.")

        elif choice == "8":
            count = app.clear_completed()
            print(f"\n✓ {count} tarea(s) completada(s) eliminada(s).")

        elif choice == "9":
            print("\n¡Hasta luego! 👋")
            break

        else:
            print("\n✗ Opción inválida. Por favor, selecciona un número del 1 al 9.")


if __name__ == "__main__":
    main()
