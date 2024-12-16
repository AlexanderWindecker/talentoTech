# **Gestión de Productos**

Este proyecto es una aplicación de gestión de productos que permite a los usuarios agregar, ver, actualizar y eliminar productos de una base de datos. La aplicación está diseñada para ser fácil de usar y proporciona una interfaz de línea de comandos.

## Características

- Agregar productos a la base de datos.
- Ver la lista de productos.
- Actualizar la información de un producto existente.
- Eliminar productos de la base de datos.
- Consultar el stock de productos.
- Prevención de duplicados: no se permite agregar productos con el mismo nombre.

## Requisitos

- Python 3.x
- SQLite (o cualquier otro sistema de gestión de bases de datos que desees usar)

## ✨Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/AlexanderWindecker/talentoTech.git
   cd tu_repositorio
   ```

## Instalacion de dependencias

```text
pip install colorama
```

## 📂 Estructura del proyecto

El proyecto consta de los siguientes archivos y directorios:

```text
talento_tech/
├── productos/
│   ├── __init__.py
│   ├── data.py          # Módulo para la gestión de la base de datos
│   └── gestion.py       # Módulo para la gestión de productos
│
├── main.py              # Script principal para ejecutar la aplicación
└── README.md            # Este archivo
```

## 💻 Uso

Ejecuta el archivo main.py para iniciar la aplicación:

```text
python main.py
```

```markdown
Sigue las instrucciones en pantalla para interactuar con la base de datos. Puedes:

+ Agregar nuevos productos.

+ Consultar la lista de productos existentes.

+ Actualizar información de un producto.

+ Eliminar productos de forma permanente.

+ Verificar el stock disponible de un producto.
```

Los mensajes en la consola estarán formateados con colores para mejorar la experiencia del usuario, gracias a la biblioteca colorama.
