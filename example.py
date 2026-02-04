#!/usr/bin/env python3
"""
Ejemplo de uso programático de la aplicación de tareas
Este archivo muestra cómo usar la aplicación desde código
"""

from todo import TodoApp
from utils import (
    get_statistics,
    filter_by_priority,
    sort_by_priority,
    validate_priority
)


def main():
    """Ejemplo de uso de la aplicación"""

    print("=" * 60)
    print("EJEMPLO DE USO DE LA APLICACIÓN DE TAREAS")
    print("=" * 60)

    # Crear una instancia de la aplicación
    app = TodoApp("example_tasks.json")

    # Agregar algunas tareas
    print("\n1. Agregando tareas...")
    app.add_task("Completar el proyecto de Python", "alta")
    app.add_task("Leer documentación de Claude Code", "media")
    app.add_task("Hacer ejercicio", "baja")
    app.add_task("Revisar emails", "media")
    app.add_task("Estudiar algoritmos", "alta")

    print(f"   ✓ Se agregaron {len(app.tasks)} tareas")

    # Listar todas las tareas
    print("\n2. Listando todas las tareas:")
    for task in app.list_tasks(show_completed=True):
        print(f"   - [{task['id']}] {task['description']} (Prioridad: {task['priority']})")

    # Filtrar por prioridad
    print("\n3. Filtrando tareas de prioridad alta:")
    high_priority = filter_by_priority(app.tasks, "alta")
    for task in high_priority:
        print(f"   - {task['description']}")

    # Ordenar por prioridad
    print("\n4. Tareas ordenadas por prioridad:")
    sorted_tasks = sort_by_priority(app.tasks)
    for task in sorted_tasks:
        print(f"   - [{task['priority'].upper()}] {task['description']}")

    # Completar algunas tareas
    print("\n5. Completando tareas...")
    app.complete_task(1)
    app.complete_task(3)
    print("   ✓ Tareas #1 y #3 marcadas como completadas")

    # Mostrar estadísticas
    print("\n6. Estadísticas de tareas:")
    stats = get_statistics(app.tasks)
    print(f"   - Total de tareas: {stats['total']}")
    print(f"   - Tareas pendientes: {stats['pending']}")
    print(f"   - Tareas completadas: {stats['completed']}")
    print(f"   - Tasa de completación: {stats['completion_rate']}%")
    print(f"   - Prioridad alta: {stats['by_priority']['alta']}")
    print(f"   - Prioridad media: {stats['by_priority']['media']}")
    print(f"   - Prioridad baja: {stats['by_priority']['baja']}")

    # Listar solo tareas pendientes
    print("\n7. Tareas pendientes:")
    pending = app.list_tasks(show_completed=False)
    for task in pending:
        print(f"   - [{task['id']}] {task['description']}")

    # Validar prioridades
    print("\n8. Validando prioridades:")
    priorities_to_test = ["alta", "media", "baja", "urgente", "normal"]
    for priority in priorities_to_test:
        is_valid = "✓" if validate_priority(priority) else "✗"
        print(f"   {is_valid} '{priority}' es {'válida' if validate_priority(priority) else 'inválida'}")

    # Eliminar una tarea
    print("\n9. Eliminando tarea #2...")
    if app.delete_task(2):
        print("   ✓ Tarea eliminada exitosamente")
        print(f"   Total de tareas restantes: {len(app.tasks)}")

    # Obtener una tarea específica
    print("\n10. Obteniendo información de tarea #4:")
    task = app.get_task(4)
    if task:
        print(f"    Descripción: {task['description']}")
        print(f"    Prioridad: {task['priority']}")
        print(f"    Completada: {'Sí' if task['completed'] else 'No'}")
        print(f"    Creada: {task['created_at'][:10]}")

    print("\n" + "=" * 60)
    print("EJEMPLO COMPLETADO")
    print("=" * 60)
    print("\nLos datos se han guardado en 'example_tasks.json'")
    print("Puedes ejecutar el programa principal con: python todo.py\n")


if __name__ == "__main__":
    main()
