# 4.6. Domain-Driven Software Architecture

## 4.6.1. Design-Level Event Storming

![Design-Level Event Storming 1](../assets/images/chapter4/domain-drive-architecture/design-level-event-storming-1.png)

![Design-Level Event Storming 2](../assets/images/chapter4/domain-drive-architecture/design-level-event-storming-2.png)

![Design-Level Event Storming 3](../assets/images/chapter4/domain-drive-architecture/design-level-event-storming-3.png)

**Enlace de Figma:** [Event Storming](https://www.figma.com/board/WxMU6oKF4Vo3Z5UQ5XZrkm/Event-Storming?node-id=0-1&t=aqD0ryVwMf3WdoTD-1)

A continuación se detallan las entidades principales de Trazza, organizadas por Bounded Context, distinguiendo cuáles actúan como Raíz de Agregado (Aggregate Root) y cuáles son entidades hijas o Value Objects asociados:

### 1. Contexto: IAM & Perfiles (Identity & Profile Management)
- **Usuario (Aggregate Root):** Identidad central del sistema.
  - Atributos clave: id, email, passwordHash, rol (Transportista / Emprendedor), estadoCuenta (Pendiente, Activo, Suspendido).
- **PerfilTransportista (Entidad / Aggregate Root):** Representa los datos operativos del conductor.
  - Atributos clave: id, usuarioId, dni, nombres, apellidos, telefono, estadoVerificacion (No verificado, En revisión, Verificado).
- **Vehiculo (Entidad dentro del agregado o Aggregate Root de Flota):** Unidad de transporte asignada a los viajes.
  - Atributos clave: id, transportistaId, placa, tipoCarroceria, capacidadCargaKg, volumenM3.
- **PerfilEmprendedor (Entidad / Aggregate Root):** Representa a la empresa o MYPE solicitante.
  - Atributos clave: id, usuarioId, razonSocial, ruc, direccionComercial, contacto.

### 2. Contexto: Matchmaking & Routing (Core Domain)
- **RutaRetorno (Aggregate Root):** Publicación de disponibilidad de un transportista.
  - Atributos clave: id, vehiculoId, transportistaId, origen, destino, fechaSalidaEstimada, capacidadDisponibleKg, estado (Abierta, Parcialmente asignada, Cerrada).
- **SolicitudEnvio (Aggregate Root):** Requerimiento logístico creado por el emprendedor.
  - Atributos clave: id, emprendedorId, origen, destino, fechaLimiteRecojo, pesoKg, volumenM3, descripcionCarga, estado (Buscando, En negociación, Asignado).
- **PropuestaMatch / Negociacion (Aggregate Root):** El acuerdo transaccional entre ambas partes.
  - Atributos clave: id, solicitudEnvioId, rutaRetornoId, montoOfrecido, tarifaAcordada, estado (Pendiente, Contrapropuesta, Aceptada, Rechazada).

### 3. Contexto: Service Execution & Monitoring (IoT & Tránsito)
- **ViajeLogistico / Shipment (Aggregate Root):** La ejecución del transporte en el mundo real.
  - Atributos clave: id, propuestaMatchId, transportistaId, emprendedorId, fechaRecojoReal, fechaEntregaEstimada, estadoViaje (PendienteRecojo, EnTransito, Desviado, Entregado, Completado, Cancelado).
- **Incidencia (Entidad hija dentro de ViajeLogistico):** Registro de anomalías durante el traslado.
  - Atributos clave: id, viajeId, tipoIncidencia (DesvíoDeRuta, Retraso, DañoCarga), descripcion, marcaTiempo, atendida (booleano).

### 4. Contexto: Payment & Billing (Pagos)
- **TransaccionPago (Aggregate Root):** Control monetario del servicio.
  - Atributos clave: id, viajeId, montoTotal, comisionPlataforma, montoNetoTransportista, estadoPago (RetenidoEnGarantia, Liberado, Reembolsado, Penalizado).
- **Comprobante (Entidad / Aggregate Root):** Documento contable emitido.
  - Atributos clave: id, transaccionId, tipoComprobante (Factura, Boleta), numeroSerie, urlPdf.

### 5. Contexto: Loyalty & Reputation (Calificaciones)
- **Calificacion (Aggregate Root):** Reseña bilateral de reputación.
  - Atributos clave: id, viajeId, evaluadorId, evaluadoId, puntuacion (1 a 5), comentario, fecha.

## 4.6.2. Software Architecture Context Diagram

![C4 Context Diagram](../assets/images/chapter4/domain-drive-architecture/c4-context.png)

## 4.6.3. Software Architecture Container Diagrams

Como una ampliación del [Diagrama de Contexto](#462-software-architecture-context-diagram), el siguiente nivel detalla los contenedores principales del sistema:

![C4 Container Diagram](../assets/images/chapter4/domain-drive-architecture/c4-container.png)

## 4.6.4. Software Architecture Components Diagrams

Para la sección 4.6.4. Software Architecture Components Diagrams, hacemos un "zoom" dentro del contenedor API Application enfocándonos en el Bounded Context principal de Trazza: Matchmaking & Routing. Este diagrama demuestra cómo la arquitectura orientada a dominios se refleja en tu código backend en C#.
