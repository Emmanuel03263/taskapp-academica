# TaskApp Academica

Aplicacion movil hibrida creada con Ionic y Angular para gestionar tareas academicas con una interfaz moderna, validaciones, filtros, progreso visual y persistencia local.

## ¿Qué es este proyecto?

TaskApp Academica es una app para que un estudiante pueda registrar, visualizar, completar y eliminar tareas del dia a dia. El objetivo de la practica es demostrar manejo de componentes Ionic, formularios reactivos en Angular, paso de datos entre vista y logica, servicio Angular y persistencia local.

La interfaz incluye un resumen superior tipo dashboard, tarjetas de metricas, barra de progreso, filtros por estado, listado movil, pagina de registro y acciones de completar/eliminar.

## Frontend y backend

Este proyecto **solo tiene frontend**.

- **Frontend:** Ionic + Angular. Es la aplicacion visual que se abre en el navegador o en un entorno movil.
- **Backend:** no se implementa porque la practica no lo pide. No hay API, servidor Node, base de datos externa ni autenticacion.
- **Persistencia:** se usa `localStorage`, que guarda las tareas en el navegador. Esto cumple el punto extra sugerido por el enunciado.

Si el profesor pidiera login, usuarios, sincronizacion entre dispositivos o administracion centralizada, ahi si haria falta backend. Para este supuesto practico, no.

## Tecnologías usadas

- **Ionic:** framework de componentes visuales para construir interfaces moviles hibridas. Aqui se usan `ion-header`, `ion-content`, `ion-list`, `ion-item`, `ion-badge`, `ion-checkbox`, `ion-fab`, `ion-progress-bar` e `ion-footer`.
- **Angular:** framework que maneja la logica de la app, los componentes, el formulario reactivo, las validaciones, los signals y el servicio de tareas.
- **localStorage:** almacenamiento local del navegador. No es una base de datos externa, pero cumple el punto extra de persistencia para esta practica.

## ¿Hace falta base de datos?

No. El enunciado marca la persistencia como opcional/puntos extra y propone `localStorage`. Por eso el proyecto guarda las tareas en el navegador mediante un servicio Angular. Para esta practica no hace falta MySQL, PostgreSQL, MongoDB, Firebase ni backend.

## Requisitos

- Node.js instalado.
- npm instalado.

## Instalacion

```bash
npm install
```

Este comando instala las dependencias del proyecto, por ejemplo Angular, Ionic, Capacitor, Ionicons, TypeScript y las herramientas necesarias para compilar.

## Ejecutar en desarrollo

```bash
npm run start
```

Este comando enciende el frontend en modo desarrollo. Internamente ejecuta `ionic serve` y abre/expone la app normalmente en:

```bash
http://localhost:8100
```

Tambien puedes usar el comando explicito:

```bash
npm run start:frontend
```

Si tienes Ionic instalado globalmente, tambien puedes usar:

```bash
ionic serve
```

## Ejecutar backend

No hay backend que encender. La app no necesita servidor de datos porque guarda la informacion en `localStorage`.

Por eso **no existe** un comando como `npm run start:backend`.

## Generar build

```bash
npm run build
```

Tambien puedes usar:

```bash
npm run build:frontend
```

Este comando verifica que el proyecto compile correctamente y genera la carpeta `www`.

## Estructura principal

- `src/app/models/tarea.model.ts`: interfaz `Tarea` con `id`, `titulo`, `descripcion`, `prioridad` y `completada`.
- `src/app/services/tareas.service.ts`: servicio `@Injectable` que centraliza creacion, eliminacion, completado y guardado en `localStorage`.
- `src/app/pages/tareas/tareas.page.ts`: logica de la pagina, formulario reactivo, signals, filtros y conexion con el servicio.
- `src/app/pages/tareas/tareas.page.html`: interfaz Ionic de dashboard, lista, filtros con botones, checkbox, contador, boton flotante y footer.
- `src/app/pages/tareas/tareas.page.scss`: estilos de la pantalla principal.
- `src/app/pages/nueva-tarea/`: pagina independiente con el formulario reactivo para crear tareas.
- `output/pdf/TaskApp_paso_a_paso.pdf`: documento con el paso a paso de desarrollo.

## Funcionalidades

- Listado de tareas con `ion-list`, `ion-item` e `ion-label`.
- Dashboard superior con resumen de tareas y barra de progreso.
- Filtros por todas, pendientes y completadas usando botones claros.
- Creacion de tareas en una pagina independiente con formularios reactivos y validaciones.
- Marcado de tarea completada con `ion-checkbox` y texto tachado.
- Eliminacion con boton de icono y soporte visual de `ion-item-sliding`.
- Servicio Angular `TareasService` con persistencia en `localStorage`.
- Diseno responsive enfocado en pantalla movil.

## Resumen de comandos

| Comando | Para que sirve |
| --- | --- |
| `npm install` | Instala todas las dependencias necesarias. |
| `npm run start` | Enciende el frontend con Ionic en modo desarrollo. |
| `npm run start:frontend` | Hace lo mismo que `npm run start`, pero con nombre mas explicito. |
| `npm run build` | Compila el proyecto para verificar que no tenga errores. |
| `npm run build:frontend` | Compila el frontend con nombre mas explicito. |

## Para subir a GitHub

La carpeta `node_modules` no debe subirse. Ya está incluida en `.gitignore`, junto con carpetas generadas como `www`, `dist` y `.angular`.

Pasos recomendados:

1. Entra a GitHub y crea un repositorio nuevo, por ejemplo `taskapp-academica`.
2. No subas la carpeta `node_modules`. Esa carpeta se genera sola cuando otra persona ejecute `npm install`.
3. Abre una terminal en la carpeta del proyecto:

```bash
cd "C:\Users\ENMANUEL\OneDrive\Escritorio\practica_6to1"
```

4. Prepara los archivos para el repositorio:

```bash
git init
git add .
git commit -m "Entrega TaskApp academica"
git branch -M main
```

5. Conecta tu repositorio local con GitHub. Cambia `TU_USUARIO` por tu usuario real de GitHub:

```bash
git remote add origin https://github.com/TU_USUARIO/taskapp-academica.git
git push -u origin main
```

Si ya existia un remoto configurado y Git muestra error, usa:

```bash
git remote set-url origin https://github.com/TU_USUARIO/taskapp-academica.git
git push -u origin main
```

## Qué entregar

- Enlace del repositorio de GitHub con el codigo fuente.
- Archivo `README.md` incluido dentro del repositorio.
- PDF del paso a paso: `output/pdf/TaskApp_paso_a_paso.pdf`.

No entregues `node_modules`, porque pesa mucho y no se sube a GitHub. El profesor podra instalar todo con:

```bash
npm install
npm run start
```
