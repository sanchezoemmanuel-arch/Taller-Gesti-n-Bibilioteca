# Taller Django – Sistema de Biblioteca

## Descripción del proyecto

Este proyecto corresponde al desarrollo de un taller utilizando el framework **Django** de Python.
El objetivo es construir una aplicación web que permita gestionar un **catálogo de libros**, aplicando la estructura básica de un proyecto Django, manejo de rutas, modelos, vistas y plantillas.

El sistema permite visualizar, crear, editar y eliminar libros dentro de un catálogo.

---

## Tecnologías utilizadas

* Python
* Django
* HTML
* Git
* GitHub

---

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```
Taller/
│
├── manage.py
├── requirements.txt
│
├── biblioteca/        # Configuración principal del proyecto
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── catalog/           # Aplicación del catálogo de libros
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── migrations/
    └── templates/
        └── catalog/
            ├── base.html
            ├── book_list.html
            ├── book_detail.html
            ├── book_form.html
            └── book_confirm_delete.html
```

---

## Funcionalidades del sistema

El sistema implementa las siguientes funcionalidades:

* Visualizar lista de libros
* Ver detalles de un libro
* Crear nuevos libros
* Editar información de libros
* Eliminar libros del catálogo

Estas funciones se implementan mediante **vistas basadas en clases de Django (CRUD)**.

---

## Instalación del proyecto

### 1. Clonar el repositorio

```
git clone https://github.com/usuario/nombre-del-repositorio.git
```

### 2. Entrar a la carpeta del proyecto

```
cd nombre-del-repositorio
```

### 3. Instalar dependencias

```
pip install -r requirements.txt
```

### 4. Ejecutar migraciones

```
python manage.py migrate
```

### 5. Ejecutar el servidor

```
python manage.py runserver
```

---

## Acceso al sistema

Una vez iniciado el servidor, abrir el navegador y entrar a:

```
http://127.0.0.1:8000/
```

Desde allí se podrá acceder al catálogo de libros.

---

## Rutas principales

Ejemplos de rutas del sistema:

* `/` → Página principal
* `/catalog/` → Lista de libros
* `/catalog/book/<id>/` → Detalle de un libro
* `/catalog/book/create/` → Crear libro
* `/catalog/book/<id>/update/` → Editar libro
* `/catalog/book/<id>/delete/` → Eliminar libro

---

## Autor

Emmanuel Sánchez
Estudiante de desarrollo web con Django
