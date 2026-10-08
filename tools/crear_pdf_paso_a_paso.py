from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "TaskApp_paso_a_paso.pdf"


def paragraph(text, style):
    return Paragraph(text, style)


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=12) for item in items],
        bulletType="bullet",
        leftIndent=18,
    )


def numbered(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=12) for item in items],
        bulletType="1",
        leftIndent=18,
    )


def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(0.65 * inch, 0.42 * inch, "TaskApp Academica - Ionic + Angular")
    canvas.drawRightString(7.85 * inch, 0.42 * inch, f"Pagina {doc.page}")
    canvas.restoreState()


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.7 * inch,
        title="Paso a paso - TaskApp Academica",
        author="Practica Ionic Angular",
    )

    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=28,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=18,
    )
    subtitle = ParagraphStyle(
        "SubtitleCustom",
        parent=styles["Normal"],
        fontSize=11,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#475569"),
        spaceAfter=20,
    )
    h1 = ParagraphStyle(
        "HeadingCustom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#1D4ED8"),
        spaceBefore=14,
        spaceAfter=8,
    )
    h2 = ParagraphStyle(
        "HeadingTwoCustom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#0F766E"),
        spaceBefore=10,
        spaceAfter=6,
    )
    body = ParagraphStyle(
        "BodyCustom",
        parent=styles["BodyText"],
        fontSize=9.8,
        leading=14,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=7,
    )
    small = ParagraphStyle(
        "SmallCustom",
        parent=body,
        fontSize=8.7,
        leading=12,
        textColor=colors.HexColor("#475569"),
    )
    code = ParagraphStyle(
        "CodeCustom",
        parent=body,
        fontName="Courier",
        fontSize=8.7,
        leading=12,
        backColor=colors.HexColor("#F1F5F9"),
        borderColor=colors.HexColor("#CBD5E1"),
        borderWidth=0.5,
        borderPadding=5,
        spaceBefore=4,
        spaceAfter=8,
    )

    story = [
        paragraph("TaskApp Academica", title),
        paragraph(
            "Paso a paso del desarrollo de una aplicacion movil hibrida para gestionar tareas academicas con Ionic, Angular, dashboard visual, filtros y persistencia local.",
            subtitle,
        ),
        paragraph("1. Que pide la practica", h1),
        paragraph(
            "La practica pide construir una aplicacion movil donde un estudiante pueda ver, crear, marcar como completadas y eliminar tareas academicas. No pide login, servidor, API ni base de datos externa. Por eso el proyecto se resolvio como frontend Ionic/Angular con persistencia local.",
            body,
        ),
        bullets(
            [
                "Crear una pagina principal con componentes Ionic: ion-header, ion-title, ion-content e ion-footer.",
                "Mostrar tareas en una lista movil usando ion-list, ion-item e ion-label.",
                "Mostrar titulo, descripcion corta y registrar prioridad en el formulario.",
                "Usar un boton flotante ion-fab para abrir el formulario de nueva tarea.",
                "Definir una interfaz TypeScript llamada Tarea.",
                "Crear el formulario con ReactiveFormsModule y validaciones.",
                "Permitir marcar tareas como completadas con ion-checkbox y texto tachado.",
                "Permitir eliminar tareas con icono de papelera o deslizamiento.",
                "Como extra, centralizar la logica en un servicio Angular y guardar en localStorage.",
                "Mejorar la experiencia visual con resumen, barra de progreso y filtros por estado.",
            ],
            body,
        ),
        paragraph("2. Aclaracion: Ionic, Angular y TaskApp", h1),
        paragraph(
            "<b>Ionic</b> no es una base de datos. Ionic es un framework de componentes visuales para crear aplicaciones moviles hibridas con aspecto de app movil. Da componentes como barras, listas, botones flotantes, checkboxes y badges.",
            body,
        ),
        paragraph(
            "<b>Angular</b> es el framework que controla la logica de la aplicacion: componentes, formularios, validaciones, servicios, rutas y estado de los datos.",
            body,
        ),
        paragraph(
            "<b>TaskApp</b> es el nombre de la aplicacion que se debe crear. En este proyecto se llama TaskApp Academica porque esta enfocada en tareas escolares o academicas.",
            body,
        ),
        paragraph("3. Frontend, backend y base de datos", h1),
        paragraph(
            "Este proyecto solo tiene frontend. El frontend es la aplicacion visual creada con Ionic y Angular. No hay backend porque el enunciado no solicita API, servidor, autenticacion ni administracion centralizada de datos.",
            body,
        ),
        bullets(
            [
                "No hace falta MySQL, PostgreSQL, MongoDB ni Firebase.",
                "No hace falta crear backend o API.",
                "No existe un comando para encender backend porque no hay backend en esta practica.",
                "Si el profesor pidiera usuarios, login o sincronizacion entre celulares, ahi si haria falta backend y base de datos.",
                "Aqui basta con un servicio Angular que lea y escriba el arreglo de tareas en localStorage.",
            ],
            body,
        ),
        PageBreak(),
        paragraph("4. Estructura del proyecto", h1),
        paragraph(
            "El proyecto se organizo con una estructura clara para separar configuracion, modelo de datos, servicio y pagina principal.",
            body,
        ),
        Table(
            [
                ["Archivo o carpeta", "Funcion"],
                ["package.json", "Define dependencias y comandos como npm install, npm run start y npm run build."],
                ["angular.json", "Configura el proyecto Angular usado por Ionic."],
                ["ionic.config.json", "Indica a Ionic que el proyecto es de tipo Angular."],
                ["src/app/models/tarea.model.ts", "Define la interfaz Tarea y el tipo de prioridad."],
                ["src/app/services/tareas.service.ts", "Centraliza crear, eliminar, completar y guardar tareas en localStorage."],
                ["src/app/pages/tareas/tareas.page.ts", "Contiene la logica de pantalla, signals, filtros y navegacion al registro."],
                ["src/app/pages/tareas/tareas.page.html", "Contiene dashboard, metricas, filtros, lista, checkbox, contador y boton flotante."],
                ["src/app/pages/tareas/tareas.page.scss", "Define el diseno movil limpio, tarjetas, colores, estados y responsive."],
                ["src/app/pages/nueva-tarea/", "Contiene la pagina independiente con formulario reactivo para registrar tareas."],
                ["README.md", "Explica los comandos para instalar y ejecutar el proyecto."],
            ],
            colWidths=[2.25 * inch, 4.75 * inch],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1D4ED8")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 8.4),
                    ("LEADING", (0, 0), (-1, -1), 11),
                    ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CBD5E1")),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8FAFC")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]
            ),
        ),
        paragraph("5. Modelo de datos", h1),
        paragraph(
            "Se definio una interfaz TypeScript para asegurar que todas las tareas tengan la misma forma. Esto ayuda a evitar errores y cumple el requisito del modelo de datos.",
            body,
        ),
        paragraph(
            "export interface Tarea {<br/>  id: number;<br/>  titulo: string;<br/>  descripcion: string;<br/>  prioridad: 'Alta' | 'Media' | 'Baja';<br/>  completada: boolean;<br/>}",
            code,
        ),
        paragraph("6. Servicio de tareas", h1),
        paragraph(
            "El servicio TareasService es el lugar donde se maneja el arreglo de tareas. Tiene metodos para agregar, cambiar estado y eliminar. Ademas, guarda los cambios en localStorage.",
            body,
        ),
        bullets(
            [
                "agregarTarea crea una nueva tarea con id, titulo, descripcion, prioridad y completada en falso.",
                "cambiarEstado actualiza si una tarea esta completada o pendiente.",
                "eliminarTarea quita una tarea de la lista.",
                "actualizarTareas guarda el arreglo en localStorage.",
                "cargarTareas lee localStorage y carga datos iniciales si no hay informacion guardada.",
            ],
            body,
        ),
        PageBreak(),
        paragraph("7. Interfaz principal", h1),
        paragraph(
            "La pantalla principal se diseno como una app movil academica: cabecera limpia, hero con resumen del dia, barra de progreso, tarjetas de metricas, filtros por estado, lista de tareas y acceso a una pagina de registro.",
            body,
        ),
        bullets(
            [
                "ion-header e ion-title: parte superior de la app.",
                "ion-content: area principal donde vive el contenido.",
                "ion-progress-bar: muestra avance de tareas completadas.",
                "Botones de filtro: permiten ver todas, pendientes y completadas.",
                "ion-list e ion-item: lista movil de tareas.",
                "ion-checkbox: cambia el estado completada.",
                "ion-badge: muestra el contador de tareas filtradas.",
                "ion-button con ion-icon trash: elimina una tarea.",
                "ion-item-sliding: permite eliminar deslizando el elemento.",
                "ion-fab: boton flotante para abrir el formulario.",
                "ion-footer: pie de la pantalla.",
            ],
            body,
        ),
        paragraph("8. Formulario reactivo", h1),
        paragraph(
            "El formulario esta en una pagina independiente llamada nueva-tarea. Se usa ReactiveFormsModule para controlar campos y validaciones desde TypeScript.",
            body,
        ),
        bullets(
            [
                "titulo: obligatorio y minimo 5 caracteres.",
                "descripcion: obligatoria y limitada a 120 caracteres.",
                "prioridad: se guarda por defecto como Media para mantener el formulario simple.",
                "Si el formulario es invalido, se muestran mensajes de error y no se guarda la tarea.",
            ],
            body,
        ),
        paragraph("9. Paso a paso de desarrollo", h1),
        numbered(
            [
                "Crear la carpeta del proyecto y abrirla en Visual Studio Code.",
                "Crear la configuracion base de Angular e Ionic: package.json, angular.json e ionic.config.json.",
                "Instalar dependencias con npm install.",
                "Crear el modelo Tarea en src/app/models/tarea.model.ts.",
                "Crear el servicio TareasService para manejar los datos y localStorage.",
                "Crear la pagina TareasPage con componentes standalone de Ionic.",
                "Construir la plantilla HTML con dashboard, metricas, filtros, lista, pagina de registro, fab y footer.",
                "Agregar estilos SCSS para una presentacion limpia, compacta y movil.",
                "Probar la compilacion con npm run build.",
                "Ejecutar en desarrollo con ionic serve o npm run start.",
            ],
            body,
        ),
        paragraph("10. Comandos necesarios", h1),
        paragraph("Instalar dependencias:", body),
        paragraph("npm install", code),
        paragraph("Ejecutar en desarrollo:", body),
        paragraph("npm run start", code),
        paragraph("Ejecutar el frontend con nombre explicito:", body),
        paragraph("npm run start:frontend", code),
        paragraph("Backend:", body),
        paragraph("No hay backend que encender en esta practica.", code),
        paragraph("Tambien puede ejecutarse directamente si se usa Ionic CLI:", body),
        paragraph("ionic serve", code),
        paragraph("Generar build de produccion:", body),
        paragraph("npm run build", code),
        paragraph("Generar build del frontend con nombre explicito:", body),
        paragraph("npm run build:frontend", code),
        paragraph("11. Entrega recomendada", h1),
        bullets(
            [
                "Subir el proyecto a GitHub sin la carpeta node_modules.",
                "Verificar que .gitignore incluya node_modules, www, dist y .angular.",
                "Adjuntar README.md con instrucciones de instalacion y ejecucion.",
                "Adjuntar este PDF como paso a paso del desarrollo.",
            ],
            body,
        ),
        paragraph("12. Checklist final", h1),
        bullets(
            [
                "La app tiene interfaz Ionic completa.",
                "La app tiene dashboard, metricas, filtros y barra de progreso.",
                "La app permite crear tareas.",
                "La app valida el titulo obligatorio y minimo de 5 caracteres.",
                "La app permite marcar tareas como completadas.",
                "La app tacha el texto de tareas completadas.",
                "La app permite eliminar tareas.",
                "La app guarda datos en localStorage.",
                "El proyecto compila con npm run build.",
            ],
            body,
        ),
        paragraph("13. Como defender el proyecto", h1),
        bullets(
            [
                "Si preguntan por backend: explicar que no se implemento porque el enunciado no lo pide; la persistencia solicitada se resolvio con localStorage.",
                "Si preguntan por base de datos: explicar que localStorage funciona como almacenamiento local del navegador para esta practica.",
                "Si preguntan por Ionic: explicar que aporta los componentes moviles usados en la interfaz.",
                "Si preguntan por Angular: explicar que maneja la logica, formularios reactivos, validaciones, signals y servicios.",
                "Si preguntan por ejecucion: npm install instala dependencias y npm run start enciende el frontend.",
            ],
            body,
        ),
        Spacer(1, 10),
        paragraph(
            "Conclusion: el proyecto cumple lo pedido sin usar backend ni base de datos externa. La persistencia se resolvio con localStorage, y la interfaz se mejoro para que parezca una aplicacion movil academica terminada.",
            small,
        ),
    ]

    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT)
