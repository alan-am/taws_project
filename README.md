# 🚀 TAWS Project - Plataforma de Favores Universitarios

Aplicación web Fullstack que conecta a estudiantes universitarios para realizar favores (mensajería, compras, impresiones) dentro del campus de forma rápida y segura.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Django REST Framework (Python 3.10+)
* **Frontend:** React.js (Implementación ligera vía CDN/Babel)
* **Base de Datos:** MySQL 8.0
* **Autenticación:** JWT (JSON Web Tokens)
* **Driver DB:** PyMySQL (Para máxima compatibilidad en Windows)

---

## ⚙️ Guía de Instalación y Despliegue

Sigue estos pasos para levantar el proyecto en un entorno local (Windows/Linux/Mac).

### 📋 Prerrequisitos
Asegúrate de tener instalado:
* [Python](https://www.python.org/downloads/)
* [MySQL Server](https://dev.mysql.com/downloads/mysql/) (o XAMPP/WAMP)
* [Visual Studio Code](https://code.visualstudio.com/)
* Extensión **"Live Server"** en VS Code.

---

### 1️⃣ Configuración del Backend (Django)

1.  **Clonar el repositorio:**
    ```bash
    git clone -b feature/integracion-fullstack https://github.com/alan-am/taws_project.git
    cd taws_project/backend
    ```

2.  **Crear entorno virtual:**
    ```bash
    python -m venv venv
    ```

3.  **Activar entorno virtual: DENTRO DE LA CARPETA BACKEND cd Backend**
    * **Windows:** `.\venv\Scripts\activate`
    * **Mac/Linux:** `source venv/bin/activate`
    * *⚠️ Nota: Si tienes errores de seguridad en Windows, ver la sección "Solución de Problemas" abajo.*

4.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configurar Variables de Entorno (.env):**
    Crea un archivo llamado `.env` dentro de la carpeta `backend/` (al mismo nivel que `manage.py`) y pega lo siguiente:
    ```env
    DEBUG=True
    SECRET_KEY=django-insecure-clave-secreta-desarrollo
    # Credenciales de Base de Datos
    DB_NAME=integracion
    DB_USER=root
    DB_PASSWORD=root
    DB_HOST=127.0.0.1
    DB_PORT=3306
    ```
    *(Ajusta `DB_PASSWORD` si tu MySQL tiene otra contraseña o déjala vacía si usas XAMPP).*

6.  **Preparar la Base de Datos:**
    Abre tu gestor de MySQL (Workbench o Terminal) y ejecuta:
    ```sql
    CREATE DATABASE integracion CHARACTER SET utf8mb4;
    ```

7.  **Ejecutar Migraciones y Servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
    ✅ El backend estará corriendo en: `http://127.0.0.1:8000/`

---

### 2️⃣ Configuración del Frontend (React)

Este proyecto utiliza una arquitectura ligera sin necesidad de `npm install` ni `node_modules` pesados.

1.  En VS Code, navega a la carpeta `frontend/`.
2.  Haz clic derecho sobre el archivo **`script.html`**.
3.  Selecciona la opción **"Open with Live Server"**.
4.  El navegador se abrirá automáticamente con la aplicación funcionando.

---

## ❗ Solución de Problemas Comunes

### 🔴 Error en Windows: "La ejecución de scripts está deshabilitada"
Si al ejecutar `activate` recibes un error rojo de seguridad en PowerShell.
**Solución:** Ejecuta este comando en la terminal y escribe 'S' o 'Y' para confirmar:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser