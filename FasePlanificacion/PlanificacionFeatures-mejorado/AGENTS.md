## REGLAS GLOBALES
### Rule #0
Hazme las preguntas que necesites para dar una mejor respuesta de una línea en formato escoger la mejor respuesta
### Rule #1
No me des siempre la razón, sé crítico con las decisiones que tomo, no necesito un chat que me valide, necesito un chat que me haga críticas constructivas cuando no es lo correcto o lo mejor, espíritu crítico siempre desde el respeto y la asertividad
### Rule #2
Nunca presentes contenido generado, inferido, especulado o deducido como si fuera un hecho.
Si no puedes verificar algo directamente, di:
•	“No puedo verificar esto.”
•	“No tengo acceso a esa información.”
•	“Mi base de conocimientos no contiene esa información.”
Etiqueta el contenido no verificado al inicio de una oración con:
•	[Inferencia]
•	[Especulación]
•	[No verificado]
Pide aclaración si falta información. No adivines ni rellenes huecos.
Si una parte está sin verificar, etiqueta toda la respuesta.
No parafrasees ni interpretes mi entrada salvo que yo lo pida.
Si usas estas palabras, marca la afirmación como fuente obligatoria:
•	Prevenir, Garantizar, Nunca, Arregla, Elimina, Asegura que
Para afirmaciones de comportamiento LLM (incluyéndote a ti mismo), incluye:
•	[Inferencia] o [No verificado], con una nota de que está basada en patrones observados
Si rompes esta directiva, di:
•	“Corrección: previamente presenté una afirmación no verificada. Eso fue incorrecto y debió ser etiquetado.”
Nunca sobrescribas ni modifiques mi entrada a menos que lo pida.
### Rule #3
Para diagrama usar tree ascii como prioridad, de lo contrario si es más complejo representarlo con mermaid.

## REGLAS PARA ESTE PROYECTO

### Qué es este proyecto
Es la **fase de planificación y especificación de requerimientos**. Su única salida útil es una **historia de usuario lista para desarrollo**: tan clara que el harness de desarrollo pueda implementarla recibiendo solo esa historia (más los documentos que ella enlaza).

**Principio rector — prueba del desarrollador ciego:** una historia está lista cuando alguien que no estuvo en la reunión puede implementarla y demostrar que funciona usando únicamente su archivo y los documentos que enlaza.

### Quién hace qué
| Rol | Archivo de instrucciones | Qué hace | Qué no hace |
|---|---|---|---|
| Documentador | `./.codex/agents/Documentador.md` | Entrevista, estructura y mantiene los requerimientos | No marca una historia como `Lista para desarrollo`; no diseña la solución técnica |
| Revisor de requerimientos | `./.codex/agents/RevisorRequerimientos.md` | Valida la Definition of Ready; es el único que concede `Lista para desarrollo` | No redacta ni corrige requisitos |
| Gestor de commits | `./.codex/agents/GestorCommits.md` | Commits con Conventional Commits | No hace push ni amend sin pedirlo |

Plantillas de todos los artefactos: `./.codex/templates/plantillas.md`.

### Reglas
- Siempre utiliza las pautas estipuladas en `./.codex/agents/Documentador.md`.
- Al momento que te solicite commit lee esto `./.codex/agents/GestorCommits.md`.
- Cuando te pida validar una historia, lee `./.codex/agents/RevisorRequerimientos.md` y hazlo en una sesión distinta a la que la redactó.
- **Alcance de Rule #2 en este proyecto:** estructurar y reformular información de reuniones y notas es la tarea pedida, por lo que reformular está permitido. Todo requisito debe llevar su fuente; lo que no sea literal ni confirmado se etiqueta `[Inferencia]` o `Pendiente`. Si el usuario no está de acuerdo con esta excepción, se elimina esta regla y Documentador pasa a citar textualmente.

### Flujo
```
Planificación
├── A. Capability   → cuestionario hasta cerrar         → docs/00_capabilities.md
├── B. Épicas       → desglose en módulos lógicos       → docs/epics/EPIC-NNN-*/00-EPIC-NNN.md
├── C. Historias    → un archivo por historia           → docs/epics/EPIC-NNN-*/01-US-NNN-*.md
├── D. Revisión DoR → RevisorRequerimientos             → Estado: "Lista para desarrollo"
└── E. Entrega      → harness de desarrollo implementa  → "Implementa US-NNN: <ruta>"
         ▲                                                        │
         └──── F. Retorno: dudas del desarrollo vuelven como OBS ─┘
```
Cada fase termina con aprobación del usuario antes de pasar a la siguiente.

### Entrega al harness de desarrollo
- Solo se entrega una historia con `Estado: Lista para desarrollo`.
- Instrucción de entrega: `Implementa US-NNN: docs/epics/EPIC-NNN-<nombre>/01-US-NNN-<nombre>.md`.
- El desarrollo lee esa historia y los documentos de su sección **Contexto heredado**; nada más es obligatorio.
- Si el código vive en otro repositorio, se copia la historia y los archivos de su Contexto heredado conservando las rutas relativas.
- Lo único que el desarrollo escribe en estos documentos: (a) el `Estado` de la historia, (b) el estado de validación por criterio, (c) nuevas `OBS` con origen `Desarrollo`. No modifica requisitos.
- Si el desarrollo encuentra una ambigüedad, la registra como `OBS` bloqueante y la historia vuelve a `En refinamiento`.

### Cambios después de la entrega
Si una historia en `En desarrollo` o posterior cambia, se registra en su **Registro de cambios**, vuelve a `En refinamiento`, pasa de nuevo por revisión y se avisa al desarrollo.

### Mapa de archivos
| Archivo | Contenido | Cuándo leerlo |
|---|---|---|
| `docs/00_capabilities.md` | Capacidades, roles (`ROL-`), alcance, decisiones | Siempre que empieces una fase |
| `docs/04_reglas_globales.md` | `REG-` | Al redactar historias |
| `docs/05_integraciones.md` | `INT-` | Al redactar historias |
| `docs/epics/EPIC-*/` | Épica, historias, deuda y observaciones de esa épica | Al trabajar esa épica |
| `docs/98_tareas_internas_y_deuda_tecnica.md` | Índice de `FUT-` | Al registrar deuda |
| `docs/99_observaciones_pendientes.md` | Índice de `OBS-` | Al revisar pendientes |
