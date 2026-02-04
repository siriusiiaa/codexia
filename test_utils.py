"""
Tests para el módulo de utilidades
"""

import unittest
from datetime import datetime
from utils import (
    format_date,
    filter_by_priority,
    get_pending_count,
    get_completed_count,
    calculate_completion_rate,
    sort_by_priority,
    get_statistics,
    validate_priority
)


class TestUtils(unittest.TestCase):
    """Tests para las funciones de utilidades"""

    def setUp(self):
        """Configuración de datos de prueba"""
        self.tasks = [
            {"id": 1, "description": "Tarea 1", "priority": "alta", "completed": False},
            {"id": 2, "description": "Tarea 2", "priority": "media", "completed": True},
            {"id": 3, "description": "Tarea 3", "priority": "baja", "completed": False},
            {"id": 4, "description": "Tarea 4", "priority": "alta", "completed": True},
        ]

    def test_format_date(self):
        """Test: Formatear fecha ISO"""
        iso_date = "2024-01-15T14:30:00"
        formatted = format_date(iso_date)
        self.assertIn("15/01/2024", formatted)

    def test_filter_by_priority(self):
        """Test: Filtrar tareas por prioridad"""
        high_priority = filter_by_priority(self.tasks, "alta")
        self.assertEqual(len(high_priority), 2)

        medium_priority = filter_by_priority(self.tasks, "media")
        self.assertEqual(len(medium_priority), 1)

        low_priority = filter_by_priority(self.tasks, "baja")
        self.assertEqual(len(low_priority), 1)

    def test_get_pending_count(self):
        """Test: Contar tareas pendientes"""
        pending = get_pending_count(self.tasks)
        self.assertEqual(pending, 2)

    def test_get_completed_count(self):
        """Test: Contar tareas completadas"""
        completed = get_completed_count(self.tasks)
        self.assertEqual(completed, 2)

    def test_calculate_completion_rate(self):
        """Test: Calcular tasa de completación"""
        rate = calculate_completion_rate(self.tasks)
        self.assertEqual(rate, 50.0)

    def test_calculate_completion_rate_empty(self):
        """Test: Calcular tasa con lista vacía"""
        rate = calculate_completion_rate([])
        self.assertEqual(rate, 0.0)

    def test_sort_by_priority(self):
        """Test: Ordenar tareas por prioridad"""
        sorted_tasks = sort_by_priority(self.tasks)

        self.assertEqual(sorted_tasks[0]["priority"], "alta")
        self.assertEqual(sorted_tasks[1]["priority"], "alta")
        self.assertEqual(sorted_tasks[2]["priority"], "media")
        self.assertEqual(sorted_tasks[3]["priority"], "baja")

    def test_get_statistics(self):
        """Test: Obtener estadísticas"""
        stats = get_statistics(self.tasks)

        self.assertEqual(stats["total"], 4)
        self.assertEqual(stats["pending"], 2)
        self.assertEqual(stats["completed"], 2)
        self.assertEqual(stats["completion_rate"], 50.0)
        self.assertEqual(stats["by_priority"]["alta"], 2)
        self.assertEqual(stats["by_priority"]["media"], 1)
        self.assertEqual(stats["by_priority"]["baja"], 1)

    def test_validate_priority(self):
        """Test: Validar prioridades"""
        self.assertTrue(validate_priority("alta"))
        self.assertTrue(validate_priority("media"))
        self.assertTrue(validate_priority("baja"))
        self.assertTrue(validate_priority("ALTA"))
        self.assertFalse(validate_priority("urgente"))
        self.assertFalse(validate_priority(""))


if __name__ == "__main__":
    unittest.main()
