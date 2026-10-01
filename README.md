# Sistema de productos
Aplicación web desarrollada con django para registrar y listar productos almacenados en una base de datos.

# Tecnologías
- Python
- Django
- SQLite
- HTML
- Git y GitHub

## Ejecución
1. Crear y activar el entorno virtual.
2. Instalar las dependencias.
3. Ejecutar las migraciones.
4. Iniciar el servidor de desarrollo.

### Crear el entorno virtual
python -m venv venv
### Activar el entorno virtual
venv\scripts\activate
### Instalar dependencias
pip install -r requirements.txt
### Ejecutar migraciones
python manage.py migrate
### Ejecutar el servidor 
python manage.py runserver

La clave incluida en la configuración solo es para desarrollo local. En despliegues, define `DJANGO_SECRET_KEY` y desactiva `DEBUG`.

# Funcionalidades implementadas
- Registro de productos
- Listado de productos
- Eliminar de productos
- Editar productos