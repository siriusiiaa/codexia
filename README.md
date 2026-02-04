# Codexia - Aplicación de Lista de Tareas

Código generado con Claude Code - Ejemplo básico de aplicación Python

## Descripción

Este es un ejemplo básico de una aplicación de lista de tareas (TODO) desarrollada con Claude Code. La aplicación demuestra conceptos fundamentales de programación en Python, incluyendo:

- Programación orientada a objetos
- Manejo de archivos JSON
- Interfaz de línea de comandos (CLI)
- Funciones de utilidad y helpers
- Pruebas unitarias con unittest
- Gestión de datos con persistencia

## Características

- ✅ Agregar tareas con diferentes prioridades
- ✅ Listar tareas (pendientes o todas)
- ✅ Marcar tareas como completadas
- ✅ Eliminar tareas
- ✅ Persistencia de datos en JSON
- ✅ Estadísticas y reportes
- ✅ Filtrado y ordenamiento por prioridad

## Estructura del Proyecto

```
codexia/
├── todo.py           # Aplicación principal con CLI interactiva
├── utils.py          # Funciones de utilidad
├── example.py        # Ejemplo de uso programático
├── test_todo.py      # Tests para la aplicación principal
├── test_utils.py     # Tests para las utilidades
└── README.md         # Este archivo
```

## Instalación

No se requieren dependencias externas. Solo necesitas Python 3.7 o superior.

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd codexia

# Verificar que tienes Python instalado
python3 --version
```

## Uso

### Modo Interactivo

Ejecuta la aplicación en modo interactivo:

```bash
python3 todo.py
```

Verás un menú con las siguientes opciones:

```
1. Agregar tarea
2. Listar tareas pendientes
3. Listar todas las tareas
4. Completar tarea
5. Eliminar tarea
6. Salir
```

### Ejemplo Programático

Ejecuta el archivo de ejemplo para ver cómo usar la aplicación desde código:

```bash
python3 example.py
```

### Uso desde Código

```python
from todo import TodoApp
from utils import get_statistics, filter_by_priority

# Crear instancia de la aplicación
app = TodoApp("mis_tareas.json")

# Agregar tareas
app.add_task("Completar el proyecto", "alta")
app.add_task("Revisar documentación", "media")

# Listar tareas pendientes
tareas = app.list_tasks(show_completed=False)

# Completar una tarea
app.complete_task(1)

# Obtener estadísticas
stats = get_statistics(app.tasks)
print(f"Tasa de completación: {stats['completion_rate']}%")

# Filtrar por prioridad
tareas_urgentes = filter_by_priority(app.tasks, "alta")
```

## Ejecutar Tests

El proyecto incluye tests unitarios completos:

```bash
# Ejecutar todos los tests
python3 -m unittest discover

# Ejecutar tests específicos
python3 test_todo.py
python3 test_utils.py

# Ejecutar con verbose para más detalle
python3 -m unittest discover -v
```

## API de la Clase TodoApp

### Constructor

```python
TodoApp(filename: str = "tasks.json")
```

Crea una nueva instancia de la aplicación de tareas.

### Métodos

- `add_task(description: str, priority: str = "media") -> Dict`
  - Agrega una nueva tarea
  - Prioridades: "baja", "media", "alta"

- `list_tasks(show_completed: bool = False) -> List[Dict]`
  - Lista tareas (pendientes o todas)

- `complete_task(task_id: int) -> Optional[Dict]`
  - Marca una tarea como completada

- `delete_task(task_id: int) -> bool`
  - Elimina una tarea

- `get_task(task_id: int) -> Optional[Dict]`
  - Obtiene una tarea por su ID

## Funciones de Utilidad (utils.py)

- `format_date(iso_date: str) -> str` - Formatear fechas
- `filter_by_priority(tasks, priority) -> List[Dict]` - Filtrar por prioridad
- `get_pending_count(tasks) -> int` - Contar tareas pendientes
- `get_completed_count(tasks) -> int` - Contar tareas completadas
- `calculate_completion_rate(tasks) -> float` - Calcular % de completación
- `sort_by_priority(tasks) -> List[Dict]` - Ordenar por prioridad
- `get_statistics(tasks) -> Dict` - Obtener estadísticas completas
- `validate_priority(priority) -> bool` - Validar prioridad

## Formato de Datos

Las tareas se almacenan en formato JSON:

```json
[
  {
    "id": 1,
    "description": "Completar el proyecto",
    "priority": "alta",
    "completed": false,
    "created_at": "2024-01-15T10:30:00"
  }
]
```

## Ejemplos de Uso

### Ejemplo 1: Gestión básica de tareas

```python
app = TodoApp()
app.add_task("Estudiar Python", "alta")
app.add_task("Hacer ejercicio", "media")
app.complete_task(1)
```

### Ejemplo 2: Obtener estadísticas

```python
from utils import get_statistics

stats = get_statistics(app.tasks)
print(f"Completadas: {stats['completed']}/{stats['total']}")
```

### Ejemplo 3: Filtrar y ordenar

```python
from utils import filter_by_priority, sort_by_priority

# Solo tareas urgentes
urgentes = filter_by_priority(app.tasks, "alta")

# Ordenadas por prioridad
ordenadas = sort_by_priority(app.tasks)
```

## Desarrollo y Contribución

### Agregar nuevas características

1. Modifica el código en los archivos correspondientes
2. Agrega tests para las nuevas funcionalidades
3. Ejecuta los tests para verificar que todo funciona
4. Actualiza la documentación

### Extensiones posibles

- Agregar fechas de vencimiento
- Implementar categorías/etiquetas
- Agregar búsqueda de tareas
- Exportar a otros formatos (CSV, Markdown)
- Implementar una interfaz gráfica (GUI)
- Agregar recordatorios
- Soporte para subtareas

## Tecnologías Utilizadas

- Python 3.7+
- JSON para persistencia de datos
- unittest para testing
- Biblioteca estándar de Python (sin dependencias externas)

## Licencia

Este es un proyecto de ejemplo educativo desarrollado con Claude Code.

## Autor

Desarrollado con Claude Code - Ejemplo básico de aplicación Python 
