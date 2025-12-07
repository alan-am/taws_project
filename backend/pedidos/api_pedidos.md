# 🚚 Documentación de API: Módulo de Pedidos

## Información General

Esta API maneja la creación, consulta y administración de los pedidos dentro del sistema.

**Permisos por Defecto:**  
Todos los endpoints requieren autenticación JWT.  
Debes enviar el token en el header:

`Authorization: Bearer <access_token>`


---
## 📢 Listar Pedidos Publicados (Muro de Pedidos)

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
    "punto_origen": "Copias Juanita",
    "punto_destino": "Facultad de Ingeniería",
    "estado": "Publicado",
    "fechaInicial": "2025-02-14T10:30:00Z",
    "horaDeseada": "2025-02-14T12:00:00Z",
    "fechaFinal": null,
    "costoEnvio": "1.50",
    "archivo_pdf": "http://ejemplo.com/tesis.pdf",
    "formato_color": "Blanco y Negro",
    "codigo_entrega": null
  }
]
 ```

 ### 🤝 Aceptar Pedido (Repartidor)
 Permite a un repartidor tomar un pedido "Publicado".
Importante: Al usar este endpoint, el sistema genera automáticamente un PIN de seguridad (OTP) único para la entrega y que se guardara en la db.
 
* **Método:** `PATCH`
* **Endpoint:** `/api/pedido/aceptar/<codigo>/`
* **Ejemplo:** `/api/pedido/aceptar/10/`
* **Permisos:** `IsAuthenticated`  (Solo usuarios con rol 'repartidor')
* **Respuesta Exitosa (200 OK):**
```json
{
  "mensaje": "Pedido aceptado correctamente.",
  "pedido": {
    "codigoPedido": 10,
    "estado": "Aceptado",
    "idRepartidor": 4,
    "repartidor_nombre": "marco_repartidor",
    "codigo_entrega": "8291" // PIN Generado
    // ... resto de datos
  }
}
```
---
 ### ✅ Finalizar Entrega (Validación OTP)
 Permite al repartidor marcar el pedido como "Entregado". Para que sea exitoso, debe ingresar el PIN que el cliente le proporcionó.

* **Método:** `POST`
* **Endpoint:** `/api/pedido/finalizar/<codigo>/`
* **Ejemplo:** `/api/pedido/finalizar/10/`
* **Permisos:** `IsAuthenticated`   (Solo el repartidor asignado)

* **Cuerpo de la peticion:**
```json
{
  "otp": "8291"
}

```
* **Respuesta exitosa(200 OK)**
```json
{
    "mensaje": "Código correcto, Entrega finalizada exitosamente.",
    "estado": "Entregado"
}

```

* **Respuesta de error(400 Bad request)**
```json
{
  "error": "Código incorrecto. Pídale al cliente que verifique el codigo."
}


```
---

# 📄 Listar Todos los Pedidos

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
    "punto_origen": "Biblioteca Central",
    "punto_destino": "Bloque F",
    "estado": "Entregado",
    "fechaInicial": "2025-02-10T16:00:00Z",
    "horaDeseada": null,
    "fechaFinal": "2025-02-10T16:45:00Z",
    "costoEnvio": "2.50",
    "archivo_pdf": null,
    "formato_color": null,
    "codigo_entrega": "4582"
  }
]
 ```

---
### Crear un pedido
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
  "punto_origen": "Cyber del frente",
  "punto_destino": "Aula 102",
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
  "punto_origen": "Cyber del frente",
  "punto_destino": "Aula 102",
  "estado": "Publicado",
  "fechaInicial": "2025-02-12T19:40:00Z",
  "horaDeseada": null,
  "fechaFinal": null,
  "costoEnvio": "3.00",
  "archivo_pdf": "https://nube.com/archivo.pdf",
  "formato_color": "Color",
  "codigo_entrega": null
}

```

---


---
### Obtener detalle de un pedido
Obtiene la información completa de un pedido.
Nota: Aquí es donde el Cliente podrá ver el codigo_entrega (PIN) una vez que el pedido haya sido aceptado, para dictárselo al repartidor.
* **Método:** `GET`
* **Endpoint:** `/api/pedidos/detalle/<codigo>/`
* **Ejemplo:** `/api/pedidos/detalle/10/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Respuesta Exitosa (200 OK):**
```json
{
  "codigoPedido": 10,
  "cliente_nombre": "joshua",
  "repartidor_nombre": "marco_repartidor",
  "punto_origen": "Cyber del frente",
  "punto_destino": "Aula 102",
  "estado": "Aceptado",
  "fechaInicial": "2025-02-12T19:40:00Z",
  "archivo_pdf": "https://nube.com/archivo.pdf",
  "formato_color": "Color",
  "costoEnvio": "3.00",
  "codigo_entrega": "8291" 
}
```
---
###  Actualizar pedido(General)
Permite modificar campos generales de un pedido (ej. corregir descripción). No debe usarse para cambiar estados de flujo (Aceptar/Entregar), use los endpoints específicos arriba.

* **Método:** `PATCH o PUT`
* **Endpoint:** `/api/pedidos/actualizar/<codigo>/`
* **Ejemplo:** `/api/pedidos/actualizar/10/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Request Body (Patch) - Ejemplo corregir descripcion**
```json
{
  "descripcion": "Impresión de diapositivas deben ser 2 de cada una"
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
  "descripcion": "Impresión de diapositivas deben ser 2 de cada una",
  "punto_origen_id": "Cyber del frente",
  "punto_destino_id": "Aula 102",
  "estado": "Publicado",
  "fechaInicial": "2025-02-12T19:40:00Z",
  "costoEnvio": "3.00",
  "archivo_pdf": "https://nube.com/archivo.pdf",
  "formato_color": "Color"
}
```
---
###  Eliminar pedido
* **Método:** `DELETE`
* **Endpoint:** `/api/pedidos/eliminar/<codigo>/`
* **Ejemplo:** `/api/pedidos/eliminar/10/`
* **Permisos:** `IsAuthenticated` (Requiere token)
* **Respuesta Exitosa (204 No Content):**
    * No se devuelve ningún contenido en el cuerpo de la respuesta.

---

##  GET /pedidos/calcular_precio/
Calcula el precio dinámico de un pedido utilizando la fórmula implementada en el backend.  
Este servicio reemplaza el precio fijo por una estructura basada en variables reales.

###  Parámetros (query)
| Parámetro | Tipo | Obligatorio | Descripción |
|----------|------|-------------|-------------|
| distancia | float | Sí | Distancia total del recorrido en kilómetros. |
| tipo_favor | string | Sí | Tipo de pedido. Ej: "normal", "pesado", etc. |
| tarifa_base | float | Sí | Tarifa mínima establecida por la plataforma. |

###  Ejemplo de petición

###  Respuesta exitosa 
```json
{
    "distancia": 2.5,
    "tipo_favor": "normal",
    "tarifa_base": 0.5,
    "costo_total": 1.87
}