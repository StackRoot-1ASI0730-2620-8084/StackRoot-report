# Capítulo V: Product Implementation, Validation & Deployment
 
## 5.1. Software Configuration Management
 
### 5.1.1. Software Development Environment Configuration
 
### 5.1.2. Source Code Management
Para la gestión del código fuente se implementa el modelo de ramificación GitFlow, el versionado semántico y las convenciones de mensajes de commit, detallados a continuación:

**GitFlow Workflow**

Se utiliza el modelo de ramificación propuesto por Vincent Driessen (“A successful Git branching model”), conocido como GitFlow. Las ramas principales son:

- **main**: Rama principal, contiene siempre el código en producción.
- **develop**: Rama de desarrollo principal, donde se integran las funcionalidades antes de pasar a producción.
- **feature/\***: Ramas creadas a partir de develop para nuevas funcionalidades.  
  Convención: `feature/<nombre-corto-descriptivo>`  
  Ejemplo: `feature/login-auth`
- **release/\***: Ramas creadas desde develop para preparar una nueva versión.  
  Convención: `release/<versión>`  
  Ejemplo: `release/1.2.0`
- **hotfix/\***: Ramas creadas desde main para corregir errores críticos en producción.  
  Convención: `hotfix/<descripción-corta>`  
  Ejemplo: `hotfix/fix-payment-bug`

**Versionado Semántico**

Se aplica Semantic Versioning 2.0.0, con el formato:

- **MAJOR**: Cambios incompatibles en la API.
- **MINOR**: Nuevas funcionalidades compatibles.
- **PATCH**: Correcciones menores y ajustes sin afectar funcionalidades.

Ejemplo de versión: `v1.3.2`

**Convenciones de Commits**

Se emplea el estándar Conventional Commits para los mensajes de commit, facilitando la automatización en integración continua y generación de changelogs.

Ejemplos de mensajes:
```
- feat: add login functionality
- fix: correct null pointer exception on user service
- docs: update API documentation
- style: fix indentation and formatting
- refactor: improve user service structure
- test: add unit tests for authentication
- chore: update dependencies
```
Estas prácticas aseguran trazabilidad, organización y calidad en la gestión del código fuente del proyecto.

 
### 5.1.3. Source Code Style Guide & Conventions
#### Landing Page Style Guide & Conventions

##### Project Structure

```
/public        (images, favicon, manifest.json)
/src
    /css         (styles.css + partials/modules)
    /js            (main.js + modules)
    /components    (HTML fragments if needed)
    /index.html
```

###### HTML

- **Semantics first**: use `header`, `nav`, `main`, `section`, `article`, `footer`.
- **Accessibility (a11y)**:
  - Add `alt` text to images.
  - Use `aria-*` attributes for dynamic components.
  - Keep logical tab order in the DOM.
  - Always show a visible focus state.
- **SEO**:
  - Include `<title>` and `<meta name="description">`.
  - Add Open Graph / Twitter meta tags.
  - Set `lang="en"` (or appropriate language) on `<html>`.
- **Performance**:
  - Use `loading="lazy"` on `<img>`.
  - Minimize inline CSS/JS.
- **Conventions**:
  - Use **kebab-case** for class names.
  - Use `id` only for JS hooks or anchors, not for styling.

###### CSS
- **Indentation**: Use **2 spaces** for indentation.
- **Naming**: Use descriptive English class names following **kebab-case**.
- **Format**:
  - One selector per line.
  - Opening brace on the same line as the selector.
- **Responsive**:
  - Prefer relative units (`%`, `rem`, `vh`, `vw`) for better adaptation across devices.
- **Architecture**:
  - Keep stylesheets modular and separated by components/sections of the Landing Page (e.g. Header, Hero, Benefits, FAQ).
- **Property order & readability**:
  - Group related properties together.
  - Maintain a consistent order inside every CSS rule.

###### JavaScript

- **Structure**:
  - Modular design; keep one `main.js` entry point.
  - Split reusable logic into separate modules.
- **Conventions**:
  - Use **camelCase** for variables/functions.
  - Use **PascalCase** for classes/constructors.
  - Constants in `UPPER_CASE`.
- **Best Practices**:
  - Prefer `const` and `let` over `var`.
  - Add comments for non-trivial logic.
  - Keep DOM selectors cached.
  - Use `addEventListener` (avoid inline `onclick`).
  - Wrap code in IIFEs or modules to avoid global leaks.

 
### 5.1.4. Software Deployment Configuration
#### 1. Landing Page – HTML, CSS y JavaScript

##### Repositorio de Código Fuente

La Landing Page se implementa empleando únicamente HTML, CSS y JavaScript nativo. Todos los archivos del proyecto deben almacenarse en un repositorio en GitHub, asegurando que el archivo **`index.html`** se ubique en la raíz del repositorio (`/`). Esto es indispensable para que GitHub Pages lo reconozca automáticamente como punto de entrada del sitio.

##### Activación de GitHub Pages

1. Acceder al repositorio en GitHub.
2. Ir a la pestaña **Settings**.
3. En el menú lateral, seleccionar la opción **Pages**.
4. En el campo **Source**, configurar:
   - Rama: `main`
   - Carpeta: `/ (root)`
5. Guardar los cambios.

##### Publicación

Tras guardar la configuración, GitHub generará de forma automática una URL pública donde estará disponible la Landing Page. El formato de la URL es:

```
https://<usuario>.github.io/<repositorio>/
```

##### Actualizaciones

Cualquier commit realizado en la rama `main` será desplegado automáticamente en la página publicada, sin necesidad de pasos adicionales.

 
## 5.2. Landing Page, Services & Applications Implementation
 
### 5.2.1. Sprint 1
 
#### 5.2.1.1. Sprint Planning 1
 <table style="width:100%; border-collapse:collapse;" border="1">
  <tr>
    <td style="width:30%; background-color:#E4E4E4;"><b>Sprint #</b></td>
    <td>Sprint 1</td>
  </tr>
  <tr>
    <td colspan="2" style="background-color: #AEAEAE;"><b>Sprint Planning Background</b></td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Date</b></td>
    <td >YYYY-MM-DD</td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Time</b></td>
    <td>HH:MM AM/PM</td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Location</b></td>
    <td>(Descripción de la ubicación de la reunión, física o virtual)</td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Prepared By</b></td>
    <td> </td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Attendees (to planning meeting)</b></td>
    <td> / / / /Medina Ingrid</td>
  </tr>
  <tr>
    <td style="width:30%;"><b>Sprint n – 1 Review Summary</b></td>
    <td>(Resumen del Sprint anterior, en términos de resultados alcanzados a nivel de productos de software, opiniones de miembros y feedback de product owner.)</td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Sprint n – 1 Retrospective Summary</b></td>
    <td>(Resumen del Sprint anterior, en términos de opiniones de miembros del equipo sobre aciertos u oportunidades de mejora en su forma de trabajo)</td>
  </tr>
  <tr>
    <td colspan="2" style="background-color: #AEAEAE;"><b>Sprint Goal & User Stories</b></td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Sprint n Goal</b></td>
    <td>(Definir el Goal del Sprint n y la métrica de cumplimiento.)</td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Sprint n Velocity</b></td>
    <td>(Definir el Velocity establecido para el Sprint n, es decir cuántos Story Points puede aceptar el equipo para este Sprint n.)</td>
  </tr>
  <tr>
    <td style="background-color:#E4E4E4;"><b>Sum of Story Points</b></td>
    <td>(Colocar la suma de los Story Points para los User Stories que se están incluyendo en este Sprint n.)</td>
  </tr>
</table>

#### 5.2.1.2. Aspect Leaders and Collaborators
|Team Member (Last Name, First Name)|GitHub Username|Mockup (L/C)|Entrevistas (L/C)|Wireframes (L/C)|Landing Page (L/C)|
|---|---|---|---|---|---|
|  | | | | | |
|  | | | | | |
|  | | | | | |
|  | | | | | |
| Medina, Ingrid | Grini913 | | | | |

 
#### 5.2.1.3. Sprint Backlog 1
 
#### 5.2.1.4. Development Evidence for Sprint Review
| Repository | Branch | Commit Id | Commit Message  | Commit Message Body  | Commited on (Date) |
| --- | --- | --- | --- | --- | --- |
|  |   |  |  |  |  |
|  |   |  |  |  |  |
|  |   |  |  |  |  |
 
#### 5.2.1.5. Execution Evidence for Sprint Review
 
#### 5.2.1.6. Services Documentation Evidence for Sprint Review
 
#### 5.2.1.7. Software Deployment Evidence for Sprint Review
 
#### 5.2.1.8. Team Collaboration Insights during Sprint
 
## 5.3. Validation Interviews
 
### 5.3.1. Diseño de Entrevistas
 
### 5.3.2. Registro de Entrevistas
 
### 5.3.3. Evaluaciones según heurísticas
 
## 5.4. Video About-the-Product
