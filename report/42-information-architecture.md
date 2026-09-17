## 4.2. Information Architecture

### 4.2.1. Organization Systems
En el sistema de Trazza, se implementa una organización jerárquica para destacar la información crítica de cada operación, como el estado del Shipment, la Available Capacity publicada por el Carrier y los resultados del emparejamiento (Match) sugerido por el Motor de IA. Esta jerarquía permite que tanto el Carrier como el Merchant identifiquen de inmediato los datos más relevantes para tomar una decisión rápida sobre aceptar o no una carga.

Se aplica una organización secuencial en los procesos que requieren una guía paso a paso, como la publicación de un nuevo Shipment por parte del Merchant, la publicación de Available Capacity por parte del Carrier, o la aceptación y confirmación de un Match. Estos flujos siguen una progresión lógica que reduce errores y asegura que se registre toda la información necesaria (origen, destino, tipo de carga) antes de completar la acción.

En cuanto a los esquemas de categorización, se emplea una organización cronológica para visualizar el historial de Matches completados y el Tracking en tiempo real del trayecto, mostrando el avance de la mercancía punto por punto. Además, el contenido se clasifica fundamentalmente según el tipo de usuario (audiencia): el Carrier accede a una interfaz orientada a publicar espacio disponible y revisar cargas sugeridas en su ruta, mientras que el Merchant accede a una interfaz enfocada en publicar envíos y monitorear transportistas disponibles. Esta separación asegura que cada usuario vea únicamente las funciones relevantes a su rol dentro de la plataforma.
### 4.2.2. Labeling Systems
A continuación, se presenta el sistema de etiquetado (labeling system) diseñado para la plataforma Trazza. El sistema busca representar los datos de forma clara, con etiquetas cortas y familiares que minimicen la carga cognitiva, para así mejorar la navegación y mantengan coherencia visual con el estilo definido en la guía de diseño.

Se ha priorizado la claridad semántica y la coherencia con el lenguaje visual del producto, especialmente con el tono de comunicación cercano y profesional.

1. Landing Page:
Inicio: Sección principal de bienvenida. Incluye el una bienvenida y acceso a la plataforma

Beneficios: Explicación segmentada de las ventajas de Rutina para nuestros usuarios.

Testimonios: Comentarios reales de usuarios sobre cómo la plataforma les ha ayudado en su gestión.

Preguntas Frecuentes: Preguntas comunes con respuestas claras. Ayuda a resolver dudas sin necesidad de contacto directo.

2. Aplicación Web:
Inicio: Vista general para el inicio de sesión y creación de cuenta.

Usuarios: Listado de usuarios que se puede agregar a tu cuenta.

### 4.2.3. SEO Tags and Meta Tags

### 4.2.4. Searching Systems

### 4.2.5. Navigation Systems