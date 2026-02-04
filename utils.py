"""
Módulo de Utilidades - Funciones auxiliares para la aplicación
"""

from datetime import datetime
from typing import List, Dict


def format_date(iso_date: str) -> str:
    """
    Formatear una fecha ISO a formato legible

    Args:
        iso_date: Fecha en formato ISO (YYYY-MM-DDTHH:MM:SS)

    Returns:
        Fecha formateada (DD/MM/YYYY)
    """
    try:
        date = datetime.fromisoformat(iso_date)
        return date.strftime("%d/%m/%Y %H:%M")
    except (ValueError, AttributeError):
        return iso_date


def filter_by_priority(tasks: List[Dict], priority: str) -> List[Dict]:
    """
    Filtrar tareas por prioridad

    Args:
        tasks: Lista de tareas
        priority: Nivel de prioridad (baja, media, alta)

    Returns:
        Lista de tareas filtradas
    """
    return [task for task in tasks if task.get("priority", "media") == priority]


def get_pending_count(tasks: List[Dict]) -> int:
    """
    Contar tareas pendientes

    Args:
        tasks: Lista de tareas

    Returns:
        Número de tareas pendientes
    """
    return sum(1 for task in tasks if not task.get("completed", False))


def get_completed_count(tasks: List[Dict]) -> int:
    """
    Contar tareas completadas

    Args:
        tasks: Lista de tareas

    Returns:
        Número de tareas completadas
    """
    return sum(1 for task in tasks if task.get("completed", False))


def calculate_completion_rate(tasks: List[Dict]) -> float:
    """
    Calcular tasa de completación

    Args:
        tasks: Lista de tareas

    Returns:
        Porcentaje de tareas completadas (0-100)
    """
    if not tasks:
        return 0.0

    completed = get_completed_count(tasks)
    return (completed / len(tasks)) * 100


def sort_by_priority(tasks: List[Dict]) -> List[Dict]:
    """
    Ordenar tareas por prioridad

    Args:
        tasks: Lista de tareas

    Returns:
        Lista de tareas ordenadas (alta, media, baja)
    """
    priority_order = {"alta": 1, "media": 2, "baja": 3}
    return sorted(
        tasks,
        key=lambda x: priority_order.get(x.get("priority", "media"), 2)
    )


def get_statistics(tasks: List[Dict]) -> Dict:
    """
    Obtener estadísticas de las tareas

    Args:
        tasks: Lista de tareas

    Returns:
        Diccionario con estadísticas
    """
    total = len(tasks)
    pending = get_pending_count(tasks)
    completed = get_completed_count(tasks)
    completion_rate = calculate_completion_rate(tasks)

    high_priority = len(filter_by_priority(tasks, "alta"))
    medium_priority = len(filter_by_priority(tasks, "media"))
    low_priority = len(filter_by_priority(tasks, "baja"))

    return {
        "total": total,
        "pending": pending,
        "completed": completed,
        "completion_rate": round(completion_rate, 2),
        "by_priority": {
            "alta": high_priority,
            "media": medium_priority,
            "baja": low_priority
        }
    }


def validate_priority(priority: str) -> bool:
    """
    Validar que la prioridad sea válida

    Args:
        priority: Nivel de prioridad a validar

    Returns:
        True si la prioridad es válida, False en caso contrario
    """
    return priority.lower() in ["baja", "media", "alta"]
