"""
Tests para la aplicación de Lista de Tareas
"""

import unittest
import os
import json
from todo import TodoApp


class TestTodoApp(unittest.TestCase):
    """Tests para la clase TodoApp"""

    def setUp(self):
        """Configuración antes de cada test"""
        self.test_filename = "test_tasks.json"
        self.app = TodoApp(self.test_filename)

    def tearDown(self):
        """Limpieza después de cada test"""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_task(self):
        """Test: Agregar una tarea"""
        task = self.app.add_task("Comprar leche", "alta")
        self.assertEqual(task["description"], "Comprar leche")
        self.assertEqual(task["priority"], "alta")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.app.tasks), 1)

    def test_list_tasks(self):
        """Test: Listar tareas"""
        self.app.add_task("Tarea 1", "baja")
        self.app.add_task("Tarea 2", "media")
        self.app.add_task("Tarea 3", "alta")

        tasks = self.app.list_tasks()
        self.assertEqual(len(tasks), 3)

    def test_complete_task(self):
        """Test: Completar una tarea"""
        task = self.app.add_task("Hacer ejercicio", "media")
        task_id = task["id"]

        completed_task = self.app.complete_task(task_id)
        self.assertIsNotNone(completed_task)
        self.assertTrue(completed_task["completed"])
        self.assertIn("completed_at", completed_task)

    def test_delete_task(self):
        """Test: Eliminar una tarea"""
        task = self.app.add_task("Tarea temporal", "baja")
        task_id = task["id"]

        result = self.app.delete_task(task_id)
        self.assertTrue(result)
        self.assertEqual(len(self.app.tasks), 0)

    def test_get_task(self):
        """Test: Obtener una tarea por ID"""
        task = self.app.add_task("Estudiar Python", "alta")
        task_id = task["id"]

        retrieved_task = self.app.get_task(task_id)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task["description"], "Estudiar Python")

    def test_get_nonexistent_task(self):
        """Test: Intentar obtener una tarea que no existe"""
        task = self.app.get_task(999)
        self.assertIsNone(task)

    def test_list_tasks_filter_completed(self):
        """Test: Listar solo tareas pendientes"""
        self.app.add_task("Tarea 1", "media")
        task2 = self.app.add_task("Tarea 2", "media")
        self.app.complete_task(task2["id"])

        pending_tasks = self.app.list_tasks(show_completed=False)
        all_tasks = self.app.list_tasks(show_completed=True)

        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(len(all_tasks), 2)

    def test_persistence(self):
        """Test: Verificar que las tareas se persisten en archivo"""
        self.app.add_task("Tarea persistente", "media")
        self.app.save_tasks()

        new_app = TodoApp(self.test_filename)
        self.assertEqual(len(new_app.tasks), 1)
        self.assertEqual(new_app.tasks[0]["description"], "Tarea persistente")

    def test_empty_tasks_file(self):
        """Test: Manejar archivo de tareas vacío"""
        with open(self.test_filename, 'w') as f:
            f.write("")

        app = TodoApp(self.test_filename)
        self.assertEqual(len(app.tasks), 0)


if __name__ == "__main__":
    unittest.main()
