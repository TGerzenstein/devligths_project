
FastAPI Backend

Este proyecto es un backend construido con FastAPI y gestionado con Poetry.


Requisitos:

    Python 3.8+
    pipx (para gestionar Poetry)
    

Instalación:


2. Configurar el entorno virtual en el proyecto

Configura Poetry para que cree el entorno virtual dentro del proyecto:

bash

poetry config virtualenvs.in-project true



Sigue los siguientes pasos para configurar el entorno y ejecutar el proyecto.
1. Instalar Poetry

Instala Poetry utilizando pipx:

bash

pipx install poetry


3. Inicializar el proyecto con Poetry

Inicia un nuevo proyecto de Poetry dentro de tu directorio actual:

bash

poetry init

Sigue las instrucciones para configurar tu proyecto.
4. Instalar dependencias

Instala las dependencias definidas en el archivo pyproject.toml:

bash

poetry install

5. Añadir FastAPI y dependencias estándar

Añade FastAPI y las dependencias estándar:

bash

poetry add "fastapi[standard]"
