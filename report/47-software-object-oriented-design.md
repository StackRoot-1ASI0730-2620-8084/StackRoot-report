# 4.7. Software Object-Oriented Design

En esta sección, el equipo presenta los diagramas que detallan la implementación orientada a objetos de los componentes definidos en la arquitectura. La estructura refleja el uso del patrón arquitectónico de capas acoplado a Domain-Driven Design (DDD) bajo el framework ASP.NET Core (C#). 

Las principales características evidenciadas en estos diagramas son:
* **Uso de Inyección de Dependencias:** Acoplamiento débil a través de interfaces (`IService`, `IRepository`).
* **Separación de Responsabilidades:** Controladores para la capa de presentación (REST), Servicios para la lógica de negocio, y Repositorios para el acceso a datos mediante Entity Framework Core.
* **Agregados y Entidades de Dominio:** Clases ricas que encapsulan atributos y comportamientos clave del negocio.

## 4.7.1. Class Diagrams

A continuación se presenta el diagrama de clases correspondiente al Bounded Context Core de la plataforma: **Matchmaking & Routing**. Este diagrama ilustra cómo se estructura el emparejamiento entre la oferta (espacio en camiones) y la demanda (solicitudes de flete).

![Diagrama de Clases - Matchmaking](../assets/images/chapter4/software-object-oriented-design/class-diagram-matchmaking.png)

A continuación se detalla la estructura y flujo del diagrama:

* **Controladores (`MatchController`):** Representa la puerta de entrada de las peticiones HTTP (REST). No accede directamente a la base de datos, sino que delega el trabajo a través de la interfaz `IMatchService`, logrando un bajo acoplamiento en el sistema.
* **Lógica de negocio y servicios (`MatchService`):** Es el componente encargado de las operaciones del dominio. Implementa la lógica para emparejar cargas con rutas disponibles, evaluar la compatibilidad de trayectos y validar la confirmación de acuerdos.
* **Acceso a datos y repositorios (`MatchRepository`):** Es la capa responsable de comunicarse con la base de datos mediante Entity Framework Core (`AppDbContext`), permitiendo consultar y persistir el estado de los viajes y acuerdos.
* **Entidades y Agregados de Dominio (`Match`, `RutaRetorno`, `SolicitudCarga`):** Modelan los elementos centrales del negocio. Cuentan con lógica y comportamiento propio (como `ConfirmarAcuerdo()` o `RestarCapacidad()`), protegiendo sus datos y asegurando que las reglas del negocio se cumplan siempre.
