# Web de Favores (Proyecto TAWS)

Plataforma web para conectar estudiantes de la ESPOL que necesitan favores (envíos, compras, impresiones) con otros estudiantes dispuestos a realizarlos a cambio de una tarifa.

## 🚀 Funcionalidades Implementadas (Frontend & Lógica Visual)

Las siguientes características están completas a nivel de interfaz y lógica de frontend en frontend/script2.html, listas para conectarse a los endpoints finales.

### 1. Gestión de Usuarios

- **Registro de Estudiantes:** Formulario funcional con validación básica.

- **Inicio de Sesión:** Simulación de autenticación y almacenamiento de token en localStorage.

- **Perfil de Usuario:** Modal de edición de datos personales (Nombre, Apellido, Teléfono).
Menú "Mi Cuenta":

- **Menú "Mi Cuenta":** 
   - Desplegable adaptativo según el rol (Estudiante vs. Repartidor).
   - Opción de "Cerrar Sesión".

Opción de "Cerrar Sesión".

### 2. Rol de Repartidor
- **Registro de Repartidor:** Flujo completo de onboarding.
- **Carga de Documentos (Simulada):**
    - Subida de foto de Carnet Estudiantil.
    - Captura de Foto de Perfil usando la cámara del dispositivo.
- **Feed de Pedidos:** Vista para que los repartidores vean los pedidos disponibles "Publicados".
- **Interruptor de Disponibilidad:** Toggle visual para activar/desactivar la recepción de pedidos.
- **Perfil de Repartidor (Dashboard):** Vista completa con historial de entregas en formato de tarjetas.

### 3. Creación de Pedidos (Cliente)
- **Servicios:**
    - 📦 **Enviar/Recoger:** Formulario con mapa para puntos de origen/destino.
    - 🖨️ **Impresiones Rápidas:** Configuración de copias, color/B&N y subida de archivos.
    - 🛍️ **Comprar/Llevar:** Lista de compras dinámica y cálculo estimado.
- **Confirmación de Pedido:** Modal con desglose de costos:
    - Tarifa base (arranque).
    - Cálculo de envío por distancia (simulado con Haversine).
    - Costo del producto (manual o calculado).
  - Total a pagar.

### 4. Gestión de Pedidos (Flujo)

**Simulación de Flujo Completo:**
    - Publicación -> Aceptación (Simulada) -> Entrega (Simulada).
- **Notificaciones (Simuladas):**
    - Modal IncomingOrderModal que imita una notificación Push para el repartidor.
- **Aceptación de Pedidos:**
    - Modal DriverAcceptanceModal para que el repartidor confirme los detalles antes de aceptar.
- **Seguimiento:** Vista ActiveOrderView con mapa y estado del pedido en tiempo real (simulado).
- **Historial:** Panel flotante de "Mis Pedidos" recientes.

---

## 🛠️ Pendiente de Conexión con Backend (TODO)

### 1. Autenticación Real
- [ ] **Token Refresh:** Manejo automático de expiración de tokens JWT.
- [ ] **Persistencia de Sesión:** Validar token al recargar la página contra /usuario/me/.

### 2. Gestión de Archivos
- [ ] **Subida de Imágenes:** Reemplazar uploadToCloudMock por una subida real a un servicio de almacenamiento (S3, Cloudinary o servidor propio) para las fotos de perfil y carnet.

### 3. Lógica de Pedidos
- [ ] **Cálculo de Ruta Real:** Conectar la API de rutas (Google Maps / OSRM) para obtener la distancia real en km en lugar de la fórmula de Haversine (línea recta).
- [ ] **WebSockets / Polling:** Implementar la lógica real para que el repartidor reciba pedidos entrantes sin recargar la página (actualmente se simula con un botón).
- [ ] **Estados del Pedido:** Sincronizar correctamente los estados Publicado -> Aceptado -> En Camino -> Entregado entre cliente y repartidor.

### 4. Datos Dinámicos
- [ ] **Código Único de Pedido:** Reemplazar el placeholder PENDIENTE-BACKEND-ID por el ID real generado por la base de datos.
- [ ] **Lista de Repartidores:** Asignar el repartidor real en la vista de confirmación (actualmente dice "Por asignar...").

## 📦 Estructura del Proyecto

```
/
├── backend/            # API Django REST Framework
│   ├── pedidos/        # App de gestión de pedidos
│   ├── usuario/        # App de gestión de usuarios
│   └── ...
└── frontend/
    ├── script2.html    # Aplicación React Monolítica (Single File Component)
    └── app.js          # Lógica auxiliar (Legacy)
```

## 🔧 Cómo correr el proyecto

1. **Backend:**`
   ```bash
   cd backend
   python manage.py runserver

Frontend:

Abrir frontend/script2.html en cualquier navegador moderno o servir con Live Server.



### Ventanas Esqueletizadas (Frontend Only)

Estas son las vistas que has visto implementadas visualmente pero que dependen de datos simulados o lógica local temporal hasta que conectes los endpoints del backend.

IncomingOrderModal (Modal de Pedido Entrante)

Qué es: Es la ventana emergente que simula una notificación Push para el repartidor cuando hay un nuevo pedido disponible.

Estado actual: Se activa manualmente con el botón "🔔 Simular Push" en DriverFeedView. Usa datos del primer pedido de la lista para rellenar la información.

Falta: Conectar a WebSockets o Polling real para que aparezca automáticamente cuando el servidor detecte un nuevo pedido.

DriverAcceptanceModal (Modal de Aceptación Manual)

Qué es: Es la ventana de confirmación que aparece cuando el repartidor hace clic en "Aceptar Pedido" desde la lista (DriverFeedView).

Estado actual: Muestra el desglose de precios y detalles del pedido seleccionado antes de confirmar la llamada a la API.

Falta: Validar en tiempo real si el pedido sigue disponible (aunque la API ya hace una validación básica).

DriverProfileView (Perfil de Repartidor)

Qué es: El dashboard completo que ve el repartidor al entrar a "Mi Perfil".

Estado actual: Muestra el saludo, avatar y una lista de tarjetas de historial. Filtra los pedidos locales (/pedido/listar/) para mostrar solo los que coinciden con el ID del usuario actual.

Falta: Un endpoint dedicado de "Mis Entregas" si la lista general se vuelve muy grande, y estadísticas reales de ganancias.

UserMenuDropdown (Menú Desplegable)

Qué es: El menú flotante que aparece al hacer clic en el icono de usuario/avatar.

Estado actual: Alterna opciones según el rol (estudiante vs repartidor). El interruptor "Activar pedidos" es puramente visual (cambia de rojo a verde).

Falta: Persistir el estado "Activo/Inactivo" del repartidor en el backend.

ProfileEditModal (Edición de Perfil Estudiante)

Qué es: El formulario modal para actualizar nombre, teléfono, etc.

Estado actual: Funcional. Llama a la API PATCH para guardar cambios, pero falta asegurar que todos los campos (como WhatsApp) tengan su contraparte exacta en el modelo de base de datos si se agregan a futuro.

¿Qué sigue?
Para que estas dejen de ser "esqueletos" y cobren vida completa, los siguientes pasos lógicos serían (cuando estés listo para tocar el backend):

WebSockets (Django Channels): Para que IncomingOrderModal aparezca sola.

Endpoint de Métricas: Para que el DriverProfileView muestre ganancias reales.

Gestión de Estado del Repartidor: Un campo is_active o disponible en el modelo Usuario para guardar el estado del interruptor del menú.
