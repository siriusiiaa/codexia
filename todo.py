#!/usr/bin/env python3
"""
Aplicación de Lista de Tareas - Ejemplo básico de Claude Code
Una simple aplicación de línea de comandos para gestionar tareas
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class TodoApp:
    """Clase principal para gestionar la lista de tareas"""

    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Dict] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        """Cargar tareas desde el archivo JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                print(f"Error al leer {self.filename}, iniciando con lista vacía")
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self) -> None:
        """Guardar tareas al archivo JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)

    def add_task(self, description: str, priority: str = "media") -> Dict:
        """Agregar una nueva tarea"""
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def list_tasks(self, show_completed: bool = False) -> List[Dict]:
        """Listar todas las tareas"""
        if show_completed:
            return self.tasks
        return [task for task in self.tasks if not task["completed"]]

    def complete_task(self, task_id: int) -> Optional[Dict]:
        """Marcar una tarea como completada"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """Eliminar una tarea"""
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < initial_length:
            self.save_tasks()
            return True
        return False

    def get_task(self, task_id: int) -> Optional[Dict]:
        """Obtener una tarea por su ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None


def print_tasks(tasks: List[Dict]) -> None:
    """Imprimir tareas en formato legible"""
    if not tasks:
        print("No hay tareas para mostrar")
        return

    print("\n" + "="*60)
    for task in tasks:
        status = "✓" if task["completed"] else " "
        priority = task.get("priority", "media")
        print(f"[{status}] #{task['id']} - {task['description']}")
        print(f"    Prioridad: {priority} | Creada: {task['created_at'][:10]}")
    print("="*60 + "\n")


def main():
    """Función principal con interfaz de línea de comandos"""
    app = TodoApp()

    print("=== Aplicación de Lista de Tareas ===")
    print("Ejemplo básico desarrollado con Claude Code\n")

    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Listar tareas pendientes")
        print("3. Listar todas las tareas")
        print("4. Completar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        choice = input("\nSelecciona una opción (1-6): ").strip()

        if choice == "1":
            description = input("Descripción de la tarea: ").strip()
            if description:
                priority = input("Prioridad (baja/media/alta) [media]: ").strip() or "media"
                task = app.add_task(description, priority)
                print(f"✓ Tarea #{task['id']} agregada exitosamente")
            else:
                print("La descripción no puede estar vacía")

        elif choice == "2":
            tasks = app.list_tasks(show_completed=False)
            print_tasks(tasks)

        elif choice == "3":
            tasks = app.list_tasks(show_completed=True)
            print_tasks(tasks)

        elif choice == "4":
            try:
                task_id = int(input("ID de la tarea a completar: "))
                task = app.complete_task(task_id)
                if task:
                    print(f"✓ Tarea #{task_id} marcada como completada")
                else:
                    print(f"No se encontró la tarea #{task_id}")
            except ValueError:
                print("ID inválido")

        elif choice == "5":
            try:
                task_id = int(input("ID de la tarea a eliminar: "))
                if app.delete_task(task_id):
                    print(f"✓ Tarea #{task_id} eliminada")
                else:
                    print(f"No se encontró la tarea #{task_id}")
            except ValueError:
                print("ID inválido")

        elif choice == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
