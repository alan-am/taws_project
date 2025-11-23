# 🚚 Documentación de API: Módulo de Pedidos

## Información General

Esta API maneja la creación, consulta y administración de los pedidos dentro del sistema.

**Permisos por Defecto:**  
Todos los endpoints requieren autenticación JWT.  
Debes enviar el token en el header:

`Authorization: Bearer <access_token>`


---
## 1. 📢 Listar Pedidos Publicados (Muro de Pedidos)

Obtiene una lista filtrada mostrando únicamente los pedidos con estado **"Publicado"**, ordenados desde el más reciente. Esta es la lista principal que visualizan los repartidores para buscar encargos disponibles.

* **Método:** `GET`
* **Endpoint:** `/api/pedido/publicados/`
* **Permisos:** `IsAuthenticated`

### ✔ Respuesta Exitosa (200 OK)
```json
[
  {
    "codigoPedido": 15,
    "idCliente": 3,
    "cliente_nombre": "maria_s",
    "idRepartidor": null,
    "repartidor_nombre": null,
    "num_whats": "0998887777",
    "descripcion": "Impresión de tesis, 20 hojas",
    "punto_origen_id": "Copias Juanita",
    "punto_destino_id": "Facultad de Ingeniería",
    "estado": "Publicado",
    "fechaInicial": "2025-02-14T10:30:00Z",
    "horaDeseada": "2025-02-14T12:00:00Z",
    "fechaFinal": null,
    "costoEnvio": "1.50",
    "archivo_pdf": "[http://ejemplo.com/tesis.pdf](http://ejemplo.com/tesis.pdf)",
    "formato_color": "Blanco y Negro"
  }
]
 ```

---

# 1. 📄 Listar Todos los Pedidos

Obtiene una lista de todos los pedidos registrados en el sistema, independientemente de su estado (Publicado, Aceptado, Entregado, Cancelado).

**Método:** `GET`  
**Endpoint:** `/api/pedidos/listar/`  
**Permisos:** `IsAuthenticated`

### ✔ Respuesta Exitosa (200 OK)
```json
[
  {
    "codigoPedido": 1,
    "idCliente": 1,
    "cliente_nombre": "alan_p",
    "idRepartidor": 2,
    "repartidor_nombre": "marco_g",
    "num_whats": "0991112222",
    "descripcion": "Llevar documento a la facultad FCI",
    "punto_origen_id": "Biblioteca Central",
    "punto_destino_id": "Bloque F",
    "estado": "Entregado",
    "fechaInicial": "2025-02-10T16:00:00Z",
    "horaDeseada": null,
    "fechaFinal": "2025-02-10T16:45:00Z",
    "costoEnvio": "2.50",
    "archivo_pdf": null,
    "formato_color": null
  }
]
 ```

---
### 3. Crear un pedido
* **Método:** `POST`
* **Endpoint:** `/api/pedido/crear/`
* **Permisos:** `IsAuthenticated` (Requiere token)

* **Campos Obligatorios:**
idCliente: ID del usuario que solicita.

num_whats: Número de contacto.

descripcion: Detalle del pedido.

punto_origen: Ubicación de recogida (Texto).

punto_destino: Ubicación de entrega (Texto).

costoEnvio: Valor a pagar.

* **Campos Opcionales:**
horaDeseada: Fecha/Hora específica para la entrega.

archivo_pdf: URL del archivo (si es impresión).

formato_color: "Blanco y Negro" o "Color".

* **Ejemplo Peticion:**
```json
{
  "idCliente": 5,
  "num_whats": "0991234567",
  "descripcion": "Impresión de diapositivas",
  "punto_origen_id": "Cyber del frente",
  "punto_destino_id": "Aula 102",
  "costoEnvio": "3.00",
  "archivo_pdf": "https://nube.com/archivo.pdf",
  "formato_color": "Color"
}
```

* **Respuesta Exitosa (200 OK):**
```json
{
  "codigoPedido": 10,
  "idCliente": 5,
  "cliente_nombre": "joshua",
  "idRepartidor": null,
  "repartidor_nombre": null,
  "num_whats": "0991234567",
  "descripcion": "Impresión de diapositivas",
  "punto_origen_id": "Cyber del frente",
  "punto_destino_id": "Aula 102",
  "estado": "Publicado",
  "fechaInicial": "2025-02-12T19:40:00Z",
  "horaDeseada": null,
  "fechaFinal": null,
  "costoEnvio": "3.00",
  "archivo_pdf": "https://nube.com/archivo.pdf",
  "formato_color": "Color"
}
```

---


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
  "cliente_nombre": "joshua",
  "punto_origen_id": "Cyber del frente",
  "punto_destino_id": "Aula 102",
  "estado": "Publicado",
  "fechaInicial": "2025-02-12T19:40:00Z",
  "archivo_pdf": "https://nube.com/archivo.pdf",
  "formato_color": "Color",
  "costoEnvio": "3.00"
  // ... resto de campos
}
```
---
### 4. Actualizar pedido
* **Método:** `PATCH o PUT`
* **Endpoint:** `/api/pedidos/actualizar/<codigo>/`
* **Ejemplo:** `/api/pedidos/actualizar/10/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Request Body (Patch) - Ejemplo repartidor acepta pedido**
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
  "idCliente": 5,
  "cliente_nombre": "joshua",
  "idRepartidor": 4,
  "repartidor_nombre": "marco_repartidor",
  "num_whats": "0991234567",
  "descripcion": "Impresión de diapositivas",
  "punto_origen_id": "Cyber del frente",
  "punto_destino_id": "Aula 102",
  "estado": "Aceptado",
  "fechaInicial": "2025-02-12T19:40:00Z",
  "costoEnvio": "3.00",
  "archivo_pdf": "https://nube.com/archivo.pdf",
  "formato_color": "Color"
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