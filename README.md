# Regístro de eventos - Proyecto Django 📆

Aplicación en la que los usuarios pueden registrar eventos con información como el nombre del evento, fecha, ubicación y participantes (nombre y correo electrónico).

## Objetivo 📌

Practicar conceptos como:
- Creación y validación de formularios
- Uso de plantillas reutilizables
- Integración con modelos
- Manejo de vistas GET y POST

## Implementación 🎯

- Modelos: Evento y Participante
- Creación de formularios para eventos y participantes
- Manejo de solicitudes GET: para mostrar los formularios
- Manejo de solicitudes POST: para procesar los datos enviados
- Validación de errores en formulario
- Template base reutilizable
- Template inicio, registro, contacto y confirmación de envío
- Mensaje de confirmacion para formulario

## Ejecución del proyecto 🚀

1. Clonar el repositorio
2. Crear y activar entorno virtual
3. Instalar dependencias necesarias: `pip install -r requirements.txt`
4. Ejecuta las migraciones: 
    `python manage.py makemigrations`
	`python manage.py migrate`
4. Ejecutar el servidor: `python manage.py runserver`
5. Acceder a http://localhost:8000

## Autores 👩‍💻👨‍💻

Jasmin Salvador - Tatu Vergara
