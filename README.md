# Codexia - Aplicación TODO de Ejemplo

> Ejemplo de aplicación creada con **Claude Code** - un asistente de IA para desarrollo de software

## 📋 Descripción

Esta es una aplicación de gestión de tareas (TODO app) completamente funcional desarrollada en Python. Demuestra las capacidades de Claude Code para:

- ✅ Crear aplicaciones completas desde cero
- ✅ Implementar operaciones CRUD (Create, Read, Update, Delete)
- ✅ Gestionar persistencia de datos con JSON
- ✅ Escribir tests unitarios completos
- ✅ Generar código limpio y bien documentado

## 🚀 Características

- **Gestión completa de tareas**: crear, ver, editar, eliminar
- **Filtrado de tareas**: ver todas, pendientes o completadas
- **Persistencia de datos**: guarda automáticamente en archivo JSON
- **Interfaz de línea de comandos**: fácil de usar
- **Tests unitarios**: 8 tests que verifican toda la funcionalidad
- **Timestamps**: seguimiento de creación y actualización

## 📦 Instalación

No se requieren dependencias externas, solo Python 3.6+

```bash
# Clonar el repositorio
git clone <repository-url>
cd codexia

# Dar permisos de ejecución
chmod +x todo_app.py
```

## 🎯 Uso

### Ejecutar la aplicación

```bash
python3 todo_app.py
```

### Ejecutar los tests

```bash
python3 test_todo_app.py -v
```

## 💡 Ejemplo de Uso

```python
from todo_app import TodoApp

# Crear instancia de la app
app = TodoApp()

# Agregar tareas
app.add_todo("Aprender Python", "Completar tutorial básico")
app.add_todo("Hacer ejercicio", "30 minutos de cardio")

# Ver todas las tareas
todos = app.get_todos()

# Marcar como completada
app.update_todo(1, completed=True)

# Ver solo pendientes
pending = app.get_todos(completed=False)
```

## 🧪 Tests

La aplicación incluye 8 tests unitarios que verifican:

- ✓ Agregar tareas
- ✓ Obtener todas las tareas
- ✓ Filtrar por estado (completadas/pendientes)
- ✓ Obtener tarea por ID
- ✓ Actualizar tareas
- ✓ Eliminar tareas
- ✓ Limpiar tareas completadas
- ✓ Persistencia de datos

Todos los tests pasan exitosamente ✅

## 📁 Estructura del Proyecto

```
codexia/
├── README.md           # Este archivo
├── todo_app.py         # Aplicación principal
├── test_todo_app.py    # Tests unitarios
└── todos.json          # Datos persistentes (generado automáticamente)
```

## 🤖 Creado con Claude Code

Este proyecto fue generado completamente por **Claude Code**, demostrando cómo un asistente de IA puede:

1. Entender requerimientos en lenguaje natural
2. Diseñar arquitectura de software
3. Implementar código funcional
4. Crear tests exhaustivos
5. Documentar apropiadamente

## 📝 Licencia

Proyecto de ejemplo - libre para usar y modificar
