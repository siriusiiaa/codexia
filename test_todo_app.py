#!/usr/bin/env python3
"""
Tests unitarios para la aplicación TODO
"""

import unittest
import os
import json
from todo_app import TodoApp


class TestTodoApp(unittest.TestCase):
    """Pruebas para la clase TodoApp"""

    def setUp(self):
        """Configurar ambiente de prueba"""
        self.test_file = "test_todos.json"
        self.app = TodoApp(data_file=self.test_file)

    def tearDown(self):
        """Limpiar después de las pruebas"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_todo(self):
        """Probar agregar una tarea"""
        todo = self.app.add_todo("Tarea de prueba", "Descripción de prueba")
        self.assertEqual(todo["title"], "Tarea de prueba")
        self.assertEqual(todo["description"], "Descripción de prueba")
        self.assertFalse(todo["completed"])
        self.assertEqual(len(self.app.todos), 1)

    def test_get_todos(self):
        """Probar obtener todas las tareas"""
        self.app.add_todo("Tarea 1")
        self.app.add_todo("Tarea 2")
        todos = self.app.get_todos()
        self.assertEqual(len(todos), 2)

    def test_get_todos_filtered(self):
        """Probar filtrar tareas por estado"""
        self.app.add_todo("Tarea pendiente")
        todo2 = self.app.add_todo("Tarea completada")
        self.app.update_todo(todo2["id"], completed=True)

        pending = self.app.get_todos(completed=False)
        completed = self.app.get_todos(completed=True)

        self.assertEqual(len(pending), 1)
        self.assertEqual(len(completed), 1)

    def test_get_todo_by_id(self):
        """Probar obtener una tarea específica"""
        todo = self.app.add_todo("Tarea específica")
        found = self.app.get_todo(todo["id"])
        self.assertIsNotNone(found)
        self.assertEqual(found["title"], "Tarea específica")

        not_found = self.app.get_todo(999)
        self.assertIsNone(not_found)

    def test_update_todo(self):
        """Probar actualizar una tarea"""
        todo = self.app.add_todo("Tarea original")
        updated = self.app.update_todo(
            todo["id"],
            title="Tarea actualizada",
            completed=True
        )

        self.assertIsNotNone(updated)
        self.assertEqual(updated["title"], "Tarea actualizada")
        self.assertTrue(updated["completed"])

    def test_delete_todo(self):
        """Probar eliminar una tarea"""
        todo = self.app.add_todo("Tarea a eliminar")
        result = self.app.delete_todo(todo["id"])
        self.assertTrue(result)
        self.assertEqual(len(self.app.todos), 0)

        result = self.app.delete_todo(999)
        self.assertFalse(result)

    def test_clear_completed(self):
        """Probar limpiar tareas completadas"""
        todo1 = self.app.add_todo("Tarea 1")
        todo2 = self.app.add_todo("Tarea 2")
        todo3 = self.app.add_todo("Tarea 3")

        self.app.update_todo(todo1["id"], completed=True)
        self.app.update_todo(todo3["id"], completed=True)

        count = self.app.clear_completed()
        self.assertEqual(count, 2)
        self.assertEqual(len(self.app.todos), 1)
        self.assertEqual(self.app.todos[0]["id"], todo2["id"])

    def test_persistence(self):
        """Probar que las tareas se guardan correctamente"""
        self.app.add_todo("Tarea persistente")
        self.app.add_todo("Otra tarea")

        new_app = TodoApp(data_file=self.test_file)
        self.assertEqual(len(new_app.todos), 2)
        self.assertEqual(new_app.todos[0]["title"], "Tarea persistente")


if __name__ == "__main__":
    unittest.main()
