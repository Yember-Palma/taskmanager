# TaskManager

## Descripción

**TaskManager** es una aplicación en Python para la gestión y automatización de tareas. Permite crear, listar, actualizar y eliminar tareas, además de integrarse con servicios de inteligencia artificial para sugerencias y automatización.

## Estructura del Proyecto

```
├── ia_service.py         # Servicios de IA y automatización
├── main.py               # Punto de entrada principal
├── README.md             # Documentación del proyecto
├── requirements.txt      # Dependencias del proyecto
├── task_manager.py       # Lógica de gestión de tareas
├── tasks.json            # Almacenamiento de tareas en formato JSON
├── tests/
│   └── test_main.py      # Pruebas unitarias
└── __pycache__/          # Archivos temporales de Python
```

## Instalación

1. Clona el repositorio:
	```zsh
	git clone https://github.com/Yember-Palma/taskmanager.git
	cd taskmanager
	```

2. Instala las dependencias:
	```zsh
	pip install -r requirements.txt
	```

## Uso

Ejecuta la aplicación principal:
```zsh
python main.py
```

## Funcionalidades

- Crear, listar, actualizar y eliminar tareas.
- Almacenamiento persistente en `tasks.json`.
- Integración con servicios de IA para sugerencias automáticas.
- Pruebas unitarias incluidas.

## Ejemplo de Uso

```python
from task_manager import TaskManager

tm = TaskManager()
tm.add_task("Estudiar Python")
tm.list_tasks()
```

## Pruebas

Para ejecutar las pruebas:
```zsh
python -m unittest discover tests
```

## Requisitos

- Python 3.8+
- Las dependencias listadas en `requirements.txt`

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.
