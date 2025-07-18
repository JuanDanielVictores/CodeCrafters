# 🎨 CodeCrafters - Proyecto Django

[![Python Version](https://img.shields.io/badge/python-3.12.3-blue?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3123/)
[![Django Version](https://img.shields.io/badge/django-4.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![SonarQube](https://img.shields.io/badge/SonarQube-Quality%20Gate-brightgreen?logo=sonarqube&logoColor=white)](https://www.sonarqube.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 📋 Índice

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Estado del Proyecto](#estado-del-proyecto)
- [Demostración](#demostración)
- [Cómo usarlo](#cómo-usarlo)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura de Directorios](#estructura-de-directorios)
- [Contribuidores](#contribuidores)
- [Licencia](#licencia)
- [Contacto](#contacto)

---

## 📖 Descripción del Proyecto

CodeCrafters es un proyecto backend desarrollado con Django que provee un sistema de autenticación (login/logout/registro). El frontend utiliza **Tailwind CSS** integrado directamente en las templates de Django para un diseño moderno y responsivo.

El proyecto incorpora buenas prácticas como:

- Uso de entornos virtuales con `django-environ` para gestión segura de variables de entorno.
- Integración de análisis de calidad de código con **SonarQube**.
- Automatización y estandarización de tareas con un **Makefile**.
- Compatible con Python 3.12.3 y Django 4.2.

---

## 🚧 Estado del Proyecto

Este proyecto se encuentra en **fase inicial** enfocada en la funcionalidad de autenticación y estructura base. Próximamente se añadirán funcionalidades adicionales y mejora en el despliegue.

---

## 🚀 Cómo usarlo

### Requisitos previos

- Python 3.12.3
- Docker (opcional, para contenerización)
- Node.js y npm (para compilar Tailwind CSS)
- Make (para comandos automáticos)
- Entorno virtual recomendado (`venv` o `virtualenv`)

### Instalación rápida

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/juandanielvictores-codecrafters.git
cd juandanielvictores-codecrafters

# Crear y activar entorno virtual
python3 -m venv env
source env/bin/activate  # Linux/Mac
# env\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements/development.txt

# Configurar variables de entorno
cp .env.sample .env
# Edita .env para tus valores locales

# Instalar dependencias de frontend
npm install

# Compilar Tailwind CSS
npx tailwindcss -i ./config/static/css/input.css -o ./config/static/css/output.css --minify

# Ejecutar migraciones y servidor
make run
