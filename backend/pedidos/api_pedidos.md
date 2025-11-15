# 🚚 Documentación de API: Módulo de Pedidos

## Información General

Esta API maneja la creación, consulta y administración de los pedidos dentro del sistema.

**Permisos por Defecto:**  
Todos los endpoints requieren autenticación JWT.  
Debes enviar el token en el header:

`Authorization: Bearer <access_token>`

---

# 1. 📄 Listar Todos los Pedidos

Obtiene una lista de todos los pedidos registrados.

**Método:** `GET`  
**Endpoint:** `/api/pedidos/listar/`  
**Permisos:** `IsAuthenticated`

### ✔ Respuesta Exitosa (200 OK)
```json
[
  {
    "codigoPedido": 1,
    "cliente": "alan_p",
    "repartidor": "marco_g",
    "num_whats": "0991112222",
    "descripcion": "Llevar documento a la facultad FCI",
    "punto_origen_id": 3,
    "punto_destino_id": 6,
    "estado": "Publicado",
    "fechaInicial": "2025-02-10T16:00:00Z",
    "horaDeseada": "2025-02-11",
    "fechaFinal": null,
    "costoEnvio": "2.50"
  }
]
 ```

---

### 2. Crear un Usuario (Registro)
```json
{
  "num_whats": "0991234567",
  "descripcion": "Enviar paquete pequeño",
  "punto_origen_id": 2,
  "punto_destino_id": 5,
  "horaDeseada": "2025-02-13",
  "costoEnvio": "3.00"
}
```
* **Respuesta Exitosa (201 Created):**
```json
{
  "codigoPedido": 10,
  "cliente": "joshua",
  "repartidor": null,
  "num_whats": "0991234567",
  "descripcion": "Enviar paquete pequeño",
  "punto_origen_id": 2,
  "punto_destino_id": 5,
  "estado": "Publicado",
  "fechaInicial": "2025-02-12T19:40:00Z",
  "horaDeseada": "2025-02-13",
  "fechaFinal": null,
  "costoEnvio": "3.00"
}
```
---
### 3. Obtener detalle de un pedido
* **Método:** `GET`
* **Endpoint:** `/api/pedidos/detalle/<codigo>/`
* **Ejemplo:** `/api/pedidos/detalle/10/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Respuesta Exitosa (200 OK):**
```json
{
  "codigoPedido": 10,
  "cliente": "joshua",
  "repartidor": null,
  "num_whats": "0991234567",
  "descripcion": "Enviar paquete pequeño",
  "punto_origen_id": 2,
  "punto_destino_id": 5,
  "estado": "Publicado",
  "fechaInicial": "2025-02-12T19:40:00Z",
  "horaDeseada": "2025-02-13",
  "fechaFinal": null,
  "costoEnvio": "3.00"
}
```
---
### 4. Actualizar pedido
* **Método:** `PATCH`
* **Endpoint:** `/api/pedidos/actualizar/<codigo>/`
* **Ejemplo:** `/api/pedidos/actualizar/10/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Request Body (Patch)**
```json
{
  "estado": "Aceptado",
  "idRepartidor": 4
}
```
* **Respuesta Exitosa (200 OK):**
```json

{
  "codigoPedido": 10,
  "cliente": "joshua",
  "repartidor": "marco_g",
  "descripcion": "Enviar paquete pequeño",
  "estado": "Aceptado",
  "costoEnvio": "3.00"
}
```
---
### 5. Eliminar pedido
* **Método:** `DELETE`
* **Endpoint:** `/api/pedidos/eliminar/<codigo>/`
* **Ejemplo:** `/api/pedidos/eliminar/10/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Respuesta Exitosa (204 No Content):**
    * No se devuelve ningún contenido en el cuerpo de la respuesta.