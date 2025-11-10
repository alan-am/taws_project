# 🚀 Documentación de API: Módulo de Usuarios

## Información General

**URL Base:** `/api/usuario/`

**Permisos Globales:** `AllowAny` (Abierto a cualquier cliente sin autenticación).

---

## 1. Listar Usuarios

Obtiene una lista de todos los usuarios registrados en el sistema.

* **Método:** `GET`
* **Endpoint:** `/api/usuario/`
* **Permisos:** `AllowAny`
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
      },
      {
        "id": 2,
        "nombre_usuario": "carla_r",
        "correo": "carla@correo.com",
        "nombre": "Carla",
        "apellido": "Reyes",
        "telefono": "0987654321",
        "rol": "repartidor",
        "foto_perfil": "[http://example.com/perfil2.jpg](http://example.com/perfil2.jpg)",
        "foto_carnet": "[http://example.com/carnet2.jpg](http://example.com/carnet2.jpg)"
      }
    ]
    ```

---

## 2. Crear un Usuario (Registro)

Registra un nuevo usuario en el sistema.


* **Método:** `POST`
* **Endpoint:** `/api/usuario/`
* **Permisos:** `AllowAny`
* **Cuerpo de Petición (Request Body):**
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
    * Todos los campos son **requeridos**
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

## 3. Obtener un Usuario Específico

Obtiene los detalles de un solo usuario usando su `id`.

* **Método:** `GET`
* **Endpoint:** `/api/usuario/<id>/`
* **Ejemplo:** `/api/usuario/1/`
* **Permisos:** `AllowAny`
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

## 4. Actualizar Usuario (Completo)

Actualiza *todos* los campos de un usuario existente. Si omites un campo, se establecerá como nulo o por defecto (lo cual puede dar error si es requerido).

* **Método:** `PUT`
* **Endpoint:** `/api/usuario/<id>/`
* **Permisos:** `AllowAny`
* **Cuerpo de Petición (Request Body):**
    * Debe incluir *todos* los campos del serializer (excepto `contrasena` si no se desea cambiar).
    ```json
    {
      "nombre_usuario": "alan_actualizado",
      "correo": "alan_nuevo@correo.com",
      "nombre": "Alan",
      "apellido": "Perez G.",
      "telefono": "0991111111",
      "rol": "repartidor",
      "foto_perfil": "[http://example.com/perfil_nuevo.jpg](http://example.com/perfil_nuevo.jpg)",
      "foto_carnet": "[http://example.com/carnet_nuevo.jpg](http://example.com/carnet_nuevo.jpg)"
    }
    ```
* **Respuesta Exitosa (200 OK):**
    * Devuelve el objeto del usuario actualizado.

---

## 5. Actualizar Usuario (Parcial)

Actualiza *solo* los campos proporcionados de un usuario existente.

* **Método:** `PATCH`
* **Endpoint:** `/api/usuario/<id>/`
* **Permisos:** `AllowAny`
* **Cuerpo de Petición (Request Body):**
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

## 6. Eliminar un Usuario

Elimina un usuario del sistema de forma permanente.

* **Método:** `DELETE`
* **Endpoint:** `/api/usuario/<id>/`
* **Permisos:** `AllowAny`
* **Respuesta Exitosa (204 No Content):**
    * No se devuelve ningún contenido en el cuerpo de la respuesta.