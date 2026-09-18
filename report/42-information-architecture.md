## 4.2. Information Architecture.

En esta sección se definen las decisiones y fundamentos que orientan la organización del contenido dentro de las experiencias web de Trazza, tanto en el Landing Page como en la Web Application. El objetivo principal es facilitar la adaptación de los usuarios, como transportistas independientes y emprendedores MYPE, permitiéndoles acceder de manera rápida y sencilla a la información de sus rutas, subastas de carga, telemetría y liquidaciones. Para ello, se plantea una estructuración lógica basada en sistemas de organización, etiquetado, búsqueda y navegación, que optimizan la experiencia de uso y reducen el esfuerzo cognitivo.

### 4.2.1. Organization Systems.

Para la interfaz principal de Trazza, tanto en el dashboard web como en su versión móvil, se ha optado por un **sistema de organización** que prioriza el acceso rápido a la información crítica de la operación logística. Dado que la plataforma está orientada a la optimización de fletes de retorno y la reducción de pérdidas, se busca que transportistas y emprendedores puedan comprender de forma inmediata el estado general del sistema y tomar decisiones de emparejamiento con el menor esfuerzo posible.

Se adopta una **organización jerárquica**, ya que permite estructurar la información según su nivel de importancia e inmediatez. Este enfoque facilita que la capa superior muestre métricas clave (como rutas frecuentes activas, retornos programados o tasa de ocupación), mientras que los niveles inferiores agrupan información detallada como corredores habituales, matches sugeridos o el historial de liquidaciones. Complementariamente, se emplea una **organización secuencial** en procesos críticos que requieren una guía paso a paso, como la publicación de capacidad ociosa, la publicación de un *shipment* o el wireflow de 8 estados del *carrier*.

En cuanto a la categorización del contenido, el sistema agrupa la información en función de objetos de negocio y criterios específicos mediante las siguientes modalidades:

| Criterio de Organización | Aplicación en Trazza |
| :--- | :--- |
| **Jerárquica (Visual hierarchy)** | Métricas clave e indicadores de rendimiento ubicados en la capa superior del Panel de Control por encima del detalle operativo. |
| **Secuencial (Step-by-step)** | Wireflow de publicación de retorno, publicación de envío (*Shipment*) y confirmación de match. |
| **Matricial** | Tabla comparativa de soluciones en el Landing Page cruzando dimensiones frente a la competencia. |
| **Cronológica** | Historial de matches completados, timeline de retornos programados y tracking en tiempo real del trayecto sobre el mapa. |
| **Por audiencia (Rol)** | Vistas diferenciadas para Carrier y Merchant mediante el selector de modo (*Modo Transportista* / *Modo Emprendedor*) en la barra superior. |

### 4.2.2. Labeling Systems.

Esta sección se centra en la forma en que se nombran los grupos de información dentro de Trazza. El objetivo es que las **etiquetas** sean precisas, consistentes y alineadas al tono de comunicación serio, respetuoso y directo definido en el Style Guide (sección 4.1). En un contexto logístico, es fundamental que el usuario comprenda de inmediato el significado de cada sección para evitar errores en las operaciones de carga.

Se han priorizado etiquetas claras y estandarizadas en español, reservando en inglés únicamente los términos del *Ubiquitous Language* del dominio (`Carrier`, `Merchant`, `Shipment`, `Match`) cuando se referencian internamente en el diseño técnico. A continuación se detallan las etiquetas principales:

#### Landing Page
| Etiqueta | Descripción / Asociación en la mente del visitante |
| :--- | :--- |
| **Inicio** | Sección principal de bienvenida y acceso a la propuesta de valor. |
| **Cómo funciona** | Explicación del flujo de 3 pasos (publicación, matching automático, aceptación y monitoreo). |
| **Beneficios** | Ventajas segmentadas por rol (sin comisión, motor de IA, monitoreo IoT/GPS, calificación bilateral). |
| **Testimonios** | Validación social con casos reales de *carriers* y *merchants*. |
| **Contacto** | Vía de comunicación directa con el equipo Trazza. |
| **Soy Transportista / Soy Emprendedor** | Par de CTAs que segmentan al visitante y dirigen a su flujo correspondiente en la Web Application. |

#### Web Application (Sidebar)
| Etiqueta | Asociación en la mente del usuario |
| :--- | :--- |
| **Panel de Control** | Vista general de indicadores y estado de la operación activa. |
| **Rutas y Retornos** | Gestión de corredores habituales y programación de retornos vacíos. |
| **Subastas de Carga** | Mercado spot de lotes disponibles para pujar o consolidar. |
| **Telemetría en Vivo** | Seguimiento GPS/IoT del viaje en curso y alertas de desvío. |
| **Liquidaciones y Pagos** | Registro y trazabilidad de los montos acordados externamente (*External Settlement*). |
| **Métricas de Flota** | Indicadores agregados de desempeño, ahorro de combustible y sostenibilidad. |

Las etiquetas de la navegación principal no exceden de dos a tres palabras, manteniéndose simples y fáciles de escanear tanto en el sidebar de escritorio como en el menú colapsable de la versión Mobile Web.

### 4.2.3. SEO Tags and Meta Tags.

En esta sección se definen los **SEO Tags** y **Meta Tags** que serán implementados en las principales páginas de la experiencia de Trazza, tanto en el Landing Page como en la Web Application. Estos elementos permiten mejorar el posicionamiento del producto en motores de búsqueda y facilitar su descubrimiento por parte de transportistas independientes, dueños de flotas y emprendedores MYPE.

#### Landing Page
| Elemento | Valor |
| :--- | :--- |
| **Title** | Trazza \| Conecta tus Retornos Vacíos con Carga Real en Lima |
| **Meta Description** | Plataforma logística que conecta transportistas con capacidad ociosa y emprendedores que necesitan enviar carga en Lima, mediante un motor de emparejamiento con IA, sin comisiones por transacción. |
| **Meta Keywords** | fletes vacíos Lima, transporte de carga terrestre, matchmaking logístico, optimización de rutas, transportistas independientes, envíos para pymes, trazabilidad GPS |
| **Author** | Equipo StackRoot - UPC Ingeniería de Software |

#### Web Application
| Elemento | Valor |
| :--- | :--- |
| **Title** | Panel de Control \| Trazza |
| **Meta Description** | Gestiona tus rutas de retorno, encuentra cargas compatibles y monitorea tus envíos en tiempo real con Trazza. |
| **Meta Keywords** | panel transportista, gestión de retornos, matching de carga, monitoreo GPS, dashboard logístico |
| **Author** | Equipo StackRoot - UPC Ingeniería de Software |


### 4.2.4. Searching Systems.

En esta sección se describen los **mecanismos de búsqueda** que ofrece Trazza para ayudar al usuario a encontrar información dentro del sistema, evitando que se sienta perdido frente al volumen de lotes, rutas y liquidaciones generadas en la operación diaria.

#### Opciones de búsqueda
* Búsqueda de lotes de carga disponibles (*Subastas de Carga*) por código de lote, cliente o zona.
* Búsqueda de corredores y rutas habituales registradas por el *carrier*.
* Búsqueda dentro del historial de liquidaciones por código, cliente o distrito.
* Búsqueda de *carriers* disponibles desde la perspectiva del *merchant*.

#### Filtros de búsqueda
| Filtro | Descripción |
| :--- | :--- |
| **Corredor / Zona** | Permite acotar resultados a un corredor logístico específico (ej. Corredor Sur, Gamarra/Textil). |
| **Tipo de carga** | Filtra por naturaleza de la mercancía (alimentos, carga frágil, textiles, etc.). |
| **Estado** | Distingue entre lotes activos, adjudicados, liquidados o en custodia. |
| **Tiempo restante** | Ordena las subastas o retornos por cercanía de cierre. |
| **Fecha / Periodo** | Acota el historial de retornos o liquidaciones a un rango de tiempo específico. |

#### Presentación de resultados y características
* Los resultados se muestran en tarjetas (*cards*) o filas de tabla, ordenadas por defecto por relevancia (menor desvío y mayor coincidencia con el Motor de IA).
* Cada resultado incluye información mínima esencial para decidir sin abrir el detalle: ruta (origen → destino), volumen/peso, distancia estimada y ganancia neta sugerida.
* Se utilizan chips e indicadores visuales de color para diferenciar estados críticos (urgente, en curso, completado).
* El sistema permite búsquedas rápidas dentro de cada módulo, reduciendo la sobrecarga de información y facilitando la identificación de oportunidades con ventanas de tiempo crítico.

### 4.2.5. Navigation Systems.

En esta sección se describen las **acciones y técnicas de navegación** que permiten guiar a los usuarios a través del Landing Page y la Web Application de Trazza, facilitando el cumplimiento de sus objetivos e interacción satisfactoria con el producto.

#### Tipos de navegación
| Tipo | Descripción |
| :--- | :--- |
| **Navegación global** | Menú principal del Landing Page y rutas de entrada por segmento (*Soy Transportista* / *Soy Emprendedor*). |
| **Navegación local (Sidebar)** | Menú lateral fijo de la Web Application con acceso directo a Panel de Control, Rutas y Retornos, Subastas de Carga, Telemetría en Vivo, Liquidaciones y Pagos, y Métricas de Flota. |
| **Navegación jerárquica (Breadcrumb)** | Ruta de migas de pan que ubica al usuario dentro del flujo activo (ej. `Inicio > Envíos Activos > En Ruta GPS #TRZ-9104`). |
| **Navegación contextual** | Acciones disponibles según el estado del elemento (ej. "Aceptar Carga Inmediata", "Confirmar Entrega y Descarga en Destino"). |
| **Navegación por rol** | Selector superior (*Modo Transportista* / *Modo Emprendedor*) que reconfigura el contenido del sidebar y panel de control. |

#### Recorrido del usuario
* **En el Landing Page:** Inicio → Cómo funciona → Beneficios → Tabla comparativa / Validación de mercado → Selección de segmento (CTA) → Registro en la Web Application.
* **En la Web Application (Carrier):** Auth Gateway → Panel de Control → Publicar Capacidad → Match Results → Inspección de carga → Telemetría en Vivo → Cierre de servicio → Auditoría/Historial.
* **En la Web Application (Merchant):** Auth Gateway → Panel de Control → Publicación de Shipment → Revisión de ofertas disponibles → Seguimiento del envío → Confirmación de entrega.

#### Características del sistema
* Permite una navegación clara y estructurada, manteniendo consistencia entre el Landing Page y la Web Application mediante redirecciones directas de los CTAs.
* Facilita el acceso directo a los módulos principales mediante un sidebar persistente, sin superar un nivel de profundidad para las funciones críticas.
* Reduce la cantidad de pasos necesarios para publicar capacidad o aceptar cargas sugeridas por el motor de IA.
* Se adapta de forma fluida a diferentes dispositivos, desde pantallas de escritorio de 1440px hasta layouts de una sola columna en dispositivos móviles de 390px.
