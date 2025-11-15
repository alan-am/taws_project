# 🚀 Documentación de API: Módulo de Usuarios

## Información General

Esta API maneja la creación, autenticación y gestión de usuarios en el sistema.

**Permisos por Defecto:** La mayoría de los endpoints requieren autenticación. Las peticiones a endpoints protegidos deben incluir la cabecera:
`Authorization: Bearer <access_token>`

**Excepción:** El endpoint de registro (`POST /api/usuario/crear/`) y los de autenticación (`/api/login/`) son públicos.

---

## 🔐 Autenticación (JWT)

El sistema usa JSON Web Tokens (JWT) para manejar la autenticación. El token de acceso tiene una duración de **360 minutos** (6 horas). Después de eso, el usuario tendrá que loguearse de nuevo.

### 1. Obtener Token (Login)

Autentica a un usuario y devuelve un par de tokens (acceso y refresco).

* **Método:** `POST`
* **Endpoint:** `/api/login/`
* **Permisos:** `AllowAny`
* **Cuerpo de Petición (Request Body):**
    ```json
    {
      "email": "alan@correo.com",
      "password": "unPasswordSeguro123"
    }
    ```
* **Respuesta Exitosa (200 OK):**
    ```json
    {
      "refresh": "eyJhbGciOi... (token largo) ...",
      "access": "eyJ0eXAiOi... (token corto - usar este) ..."
    }
    ```
* **Respuesta de Error (401 Unauthorized):**
    ```json
    {
      "detail": "No active account found with the given credentials"
    }
    ```

### 2. Refrescar Token (Ignorar por ahora)

Obtiene un nuevo token de acceso usando un token de refresco válido.

* **Método:** `POST`
* **Endpoint:** `/api/login/refresh/`
* **Permisos:** `AllowAny`
* **Cuerpo de Petición (Request Body):**
    ```json
    {
      "refresh": "eyJhbGciOi... (el token de refresco) ..."
    }
    ```
* **Respuesta Exitosa (200 OK):**
    ```json
    {
      "access": "eyJ0eXAiOi... (un nuevo token de acceso) ..."
    }
    ```

---

## 👤 Endpoints de Gestión de Usuarios

### 3. Obtener Perfil de Usuario (mediante token access obtenido)

Obtiene los detalles completos del usuario que está actualmente autenticado (basado en el token de acceso).

* **Método:** `GET`
* **Endpoint:** `/api/usuario/me/`
* **Permisos:** `IsAuthenticated` (Requiere token en el header de la peticion)
* **Respuesta Exitosa (200 OK):**
    ```json
    {
      "id": 1,
      "nombre_usuario": "alan_p",
      "correo": "alan@correo.com",
      "nombre": "Alan",
      "apellido": "Perez",
      "telefono": "0991234567",
      "rol": "estudiante",
      "foto_perfil": "[http://example.com/perfil.jpg](http://example.com/perfil.jpg)",
      "foto_carnet": "[http://example.com/carnet.jpg](http://example.com/carnet.jpg)"
    }
    ```
* **Respuesta de Error (401 Unauthorized):**
    ```json
    {
      "detail": "Authentication credentials were not provided."
    }
    ```

---


### 1. Listar Usuarios

Obtiene una lista de todos los usuarios registrados. Todos requieren del token corto (access) incluido en el header.

* **Método:** `GET`
* **Endpoint:** `/api/usuario/listar/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Respuesta Exitosa (200 OK):**
    ```json
    [
      {
        "id": 1,
        "nombre_usuario": "alan_p",
        "correo": "alan@correo.com",
        "nombre": "Alan",
        "apellido": "Perez",
        "telefono": "0991234567",
        "rol": "estudiante",
        "foto_perfil": "[http://example.com/perfil.jpg](http://example.com/perfil.jpg)",
        "foto_carnet": "[http://example.com/carnet.jpg](http://example.com/carnet.jpg)"
      }
    ]
    ```

---

### 2. Crear un Usuario (Registro)

Registra un nuevo usuario en el sistema.

* **Método:** `POST`
* **Endpoint:** `/api/usuario/crear/`
* **Permisos:** `AllowAny` (Público)
* **Cuerpo de Petición Mínimo (Request Body):**
    ```json
    {
      "correo": "nuevo@correo.com",
      "nombre": "Nombre",
      "apellido": "Apellido",
      "contrasena": "unPasswordSeguro123",
      "rol": "estudiante"
    }
    ```
* **Cuerpo de Petición Completo (Opcional):**
    ```json
    {
      "nombre_usuario": "nuevo_usuario",
      "correo": "nuevo@correo.com",
      "nombre": "Nombre",
      "apellido": "Apellido",
      "contrasena": "unPasswordSeguro123",
      "telefono": "0999999999",
      "rol": "estudiante",
      "foto_perfil": "[http://example.com/foto.jpg](http://example.com/foto.jpg)",
      "foto_carnet": "[http://example.com/carnet.jpg](http://example.com/carnet.jpg)"
    }
    ```
* **Notas del Body:**
    * **Campos Requeridos:** `correo`, `nombre`, `apellido`, `contrasena`, `rol`.
    * **Campos Opcionales:** `nombre_usuario`, `telefono`, `foto_perfil`, `foto_carnet`.
    * `rol`: Debe ser uno de los valores definidos: `'estudiante'` o `'repartidor'`.
* **Respuesta Exitosa (201 Created):**
    * Devuelve el objeto del usuario recién creado (sin el campo `contrasena`).
    ```json
    {
      "id": 3,
      "nombre_usuario": "nuevo_usuario",
      "correo": "nuevo@correo.com",
      "nombre": "Nombre",
      "apellido": "Apellido",
      "telefono": "0999999999",
      "rol": "estudiante",
      "foto_perfil": "[http://example.com/foto.jpg](http://example.com/foto.jpg)",
      "foto_carnet": "[http://example.com/carnet.jpg](http://example.com/carnet.jpg)"
    }
    ```

---

### 3. Obtener un Usuario Específico

Obtiene los detalles de un solo usuario usando su `id`.

* **Método:** `GET`
* **Endpoint:** `/api/usuario/detalle/<id>/`
* **Ejemplo:** `/api/usuario/detalle/1/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Respuesta Exitosa (200 OK):**
    ```json
    {
      "id": 1,
      "nombre_usuario": "alan_p",
      "correo": "alan@correo.com",
      "nombre": "Alan",
      "apellido": "Perez",
      "telefono": "0991234567",
      "rol": "estudiante",
      "foto_perfil": "[http://example.com/perfil.jpg](http://example.com/perfil.jpg)",
      "foto_carnet": "[http://example.com/carnet.jpg](http://example.com/carnet.jpg)"
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
      "detail": "Not found."
    }
    ```

---

### 4. Actualizar Usuario (Completo o Parcial)

Actualiza los campos de un usuario existente.

* **Método:** `PUT` (para actualizar todo) o `PATCH` (para actualizar parcialmente)
* **Endpoint:** `/api/usuario/actualizar/<id>/`
* **Ejemplo:** `/api/usuario/actualizar/1/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Cuerpo de Petición (Request Body - `PATCH`):**
    * Incluye solo los campos que deseas cambiar.
    ```json
    {
      "telefono": "0988888888",
      "rol": "estudiante"
    }
    ```
* **Respuesta Exitosa (200 OK):**
    * Devuelve el objeto del usuario actualizado.

---

### 5. Eliminar un Usuario

Elimina un usuario del sistema de forma permanente.

* **Método:** `DELETE`
* **Endpoint:** `/api/usuario/eliminar/<id>/`
* **Ejemplo:** `/api/usuario/eliminar/1/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Respuesta Exitosa (204 No Content):**
    * No se devuelve ningún contenido en el cuerpo de la respuesta.