IncomingOrderModal (Modal "Nuevo Pedido"):

Propósito: Es una notificación emergente para el repartidor. Le avisa cuando el sistema detecta un nuevo pedido disponible en su zona o le asigna uno directamente. Funciona como una alerta "Push".

Funcionalidad: Muestra los detalles clave (origen, destino, tarifa base, costo por distancia y total) para que el repartidor decida rápidamente si aceptar o rechazar.

Estado actual: Se activa manualmente con un botón de simulación ("🔔 Simular Push") en la vista de lista de pedidos (DriverFeedView).

DriverAcceptanceModal (Modal de Confirmación Manual):

Propósito: Es una ventana de seguridad para cuando el repartidor selecciona voluntariamente un pedido de la lista "Pedidos Disponibles".

Funcionalidad: Evita que acepte un pedido por error. Le muestra el mismo desglose detallado de precios y ruta que el modal anterior, pero se activa al hacer clic en "Aceptar Pedido" dentro del feed.

Estado actual: Totalmente implementado visualmente y conectado al flujo de la lista de pedidos.

DriverProfileView (Perfil de Repartidor):

Propósito: Es el panel de control principal ("Dashboard") exclusivo para usuarios con el rol de "repartidor".

Funcionalidad: Reemplaza el formulario de edición de perfil simple. Muestra un saludo personalizado y, lo más importante, un historial visual de sus entregas con tarjetas de colores según el estado (Verde: Entregado, Naranja: En curso, Rojo: Cancelado).

Estado actual: Obtiene todos los pedidos y filtra localmente los que pertenecen al repartidor actual.

UserMenuDropdown (Menú "Mi Cuenta"):

Propósito: Es el menú flotante que aparece al hacer clic en el avatar/nombre de usuario en la barra de navegación.

Funcionalidad: Es adaptativo. Si eres estudiante, muestra opciones estándar (Perfil, Carrito). Si eres repartidor, muestra opciones de trabajo (Perfil Dashboard) y un interruptor visual para ponerte "Activo" o "Inactivo" para recibir pedidos.

Estado actual: Implementado con lógica condicional de roles. El interruptor es visualmente funcional.

OrderHistoryPopup (Historial Flotante):

Propósito: Ofrecer un acceso rápido a los últimos pedidos del usuario sin tener que navegar a una página completa.

Funcionalidad: Se despliega al hacer clic en el icono del carrito de compras. Muestra una lista resumida de los últimos 3 pedidos con su estado.

Estado actual: Conectado a la API /pedido/listar/ con filtrado local.

ActiveOrderView (Seguimiento de Pedido - Rediseñada):

Propósito: Pantalla principal para seguir el estado de un pedido en curso.

Funcionalidad: Ahora tiene un diseño de "Split View" (dos columnas). A la izquierda, una línea de tiempo (timeline) con los estados del pedido y la tarjeta de información del contacto. A la derecha, un mapa grande interactivo.

Estado actual: Rediseñada visualmente para coincidir con la estética moderna solicitada.

ProfileEditModal (Edición de Perfil - Estudiante):

Propósito: Permitir a los usuarios con rol de "estudiante" actualizar sus datos básicos.

Funcionalidad: Un formulario modal sencillo para cambiar nombre, apellido y teléfono.

Estado actual: Funcional y conectado al endpoint de actualización de usuario.
