# **HUM - Tienda de Cervezas Artesanales**

Bienvenido al proyecto de la **Tienda de Cervezas HUM**, una tienda ficticia dedicada a la venta de cervezas artesanales, tanto nacionales como importadas. Este sitio web ha sido desarrollado utilizando el framework **Django** en **Python**, y ofrece una experiencia completa de exploración de productos con diversas funcionalidades.

![Logo de la cervecería HUM](Proyecto%20Final%20BIOS%20Cerveceria/static/img/Logo%20Hum.png)

## **Funcionalidades**

- **Búsqueda avanzada de productos**: Los usuarios pueden buscar cervezas por nombre, fabricante, origen o tipo de cerveza.
- **Registro y autenticación de usuarios**: Los usuarios pueden crear una cuenta, iniciar sesión y acceder a funciones exclusivas.
- **Formulario de contacto**: Permite a los usuarios enviar consultas o sugerencias directamente desde el sitio web.
- **Catálogo de productos**: Cada cerveza tiene su propia página con detalles sobre el precio, origen, variedad y una imagen del producto.

## **Tecnologías utilizadas**

- **Backend**: Django (Python)
- **Base de datos**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Recursos estáticos**: Imágenes, estilos y scripts gestionados mediante `settings.py`.

## **Estructura del proyecto**

```bash
Proyecto Final BIOS Cerveceria/
│
├── cerveceria/
│   ├── migrations/               # Archivos de migración de la base de datos
│   ├── static/                   # Archivos estáticos como imágenes y CSS
│   ├── templates/                # Plantillas HTML del sitio
│   ├── __init__.py               # Inicialización del módulo
│   ├── admin.py                  # Configuración del panel de administración
│   ├── apps.py                   # Configuración de la aplicación
│   ├── forms.py                  # Formularios de Django
│   ├── models.py                 # Definición de los modelos de base de datos
│   ├── views.py                  # Vistas de la aplicación
│   └── urls.py                   # Rutas de la aplicación
│
├── misitio/
│   ├── settings.py               # Configuración general del proyecto
│   ├── urls.py                   # Rutas principales del proyecto
│   └── wsgi.py                   # Configuración para el servidor
│
├── db.sqlite3                    # Base de datos del proyecto
├── manage.py                     # Script de administración de Django
└── README.md                     # Este archivo


El proyecto fue desarrollado por Pablo Salina como parte de su trabajo final. Se realizó bajo la supervisión del equipo docente de BIOS.

