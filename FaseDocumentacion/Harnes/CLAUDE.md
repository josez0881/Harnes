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
Es el **harness de documentación**. Este repositorio es el sitio Docusaurus del sistema: aquí se escribe la documentación en Markdown, en dos instancias del plugin `docs` con rutas y sidebars independientes:

| Carpeta | Público | Contenido |
|---|---|---|
| `docs-tecnica/` | Equipo técnico y funcional | Actores, módulos, especificación de funcionalidades, permisos |
| `docs-usuario/` | Usuario final | Guías paso a paso y FAQs |

La información sale de dos fuentes: el **código del sistema** (solo lectura; su ruta está en `config-docs.md`) y las **respuestas del humano**. Nada más.

**Principio rector — prueba del lector sin contexto:** una página está lista cuando alguien que no conoce el sistema puede entender qué hace la funcionalidad (o usarla) leyendo solo esa página y sus enlaces, y cada dato de la página tiene una fuente que el revisor puede comprobar.

### Quién hace qué
| Rol | Archivo de instrucciones | Qué hace | Qué no hace |
|---|---|---|---|
| Documentador | `./.claude/agents/documentador.md` | Entrevista, redacta y mantiene las páginas; pide lecturas de código al explorador | No marca una página como revisada; no edita código del sistema; no inventa datos |
| Explorador | `./.claude/agents/explorer.md` | Lee el código del sistema y deja hallazgos con `archivo:línea` en `progress/explore_<tema>.md` | No modifica nada salvo su informe; no ejecuta código |
| Revisor de documentación | `./.claude/agents/revisor-documentacion.md` | Valida las páginas contra R1–R8; es el único que quita `draft: true` | No redacta ni corrige contenido |
| Commits | `./.claude/skills/conventional-commit/SKILL.md` | Commits con Conventional Commits, solo a petición | No hace push ni amend sin pedirlo |

Plantillas de todos los artefactos: `./.claude/templates/plantillas.md`.

### Reglas duras
1. **Sin fuente no hay dato.** Cada comportamiento, regla, mensaje, etiqueta de pantalla y permiso viene del código (con evidencia en `progress/explore_*.md`) o de una respuesta del humano. Lo demás es `[PENDIENTE]`, `[POR CONFIRMAR]` o `[Inferencia]`.
2. **Código del sistema: solo lectura.** No se edita, no se ejecuta, no se instalan dependencias, no se lanzan migraciones ni pruebas. No se leen `.env`, claves, tokens ni credenciales: si una lectura los toca, se detiene y se informa.
3. **Dónde se escribe:** `docs-tecnica/`, `docs-usuario/`, `progress/` y `config-docs.md`. **No se editan** `docusaurus.config.*`, `package.json`, `sidebars.*`, `static/` ni el resto del sitio salvo petición expresa; si algo de eso hace falta, se propone el cambio.
4. **No ejecutar `build`, `start` ni instalaciones** salvo petición expresa del humano.
5. **Contenido publicable.** Lo que se escribe en `docs-*/` puede acabar en un sitio visible. No se incluyen credenciales, hosts, IPs, rutas de archivos del código, nombres de tablas ni datos personales reales (ejemplos y capturas con datos de prueba). La evidencia `archivo:línea` vive en `progress/`, no en las páginas.
6. **Borrador por defecto.** Toda página nace con `draft: true` y solo el revisor lo pone en `false` (junto con `revisada`). Una página con `[PENDIENTE]` o `[POR CONFIRMAR]` siempre es `draft: true`. Si una página revisada cambia, vuelve a `draft: true`.
7. **Quien redacta no aprueba.** El revisor trabaja en una sesión distinta a la que redactó. Tras 2 rondas con `CAMBIOS REQUERIDOS` sobre lo mismo, se escala al humano en lugar de iterar.
8. **Una instancia no enlaza a la otra con rutas relativas.** Dentro de una instancia: enlaces relativos a archivos `.md`. Entre instancias: ruta del sitio con el `routeBasePath` de `config-docs.md`.
9. **Estado en disco:** al empezar una sesión lee `progress/current.md`; manténlo actualizado mientras trabajas (no al final); al cerrar, pasa su resumen a `progress/history.md` y vacía `current.md`. `current.md` es memoria de trabajo: el contenido vive solo en `docs-*/`.
10. **Alcance de Rule #2 en este proyecto:** redactar documentación a partir del código y de tus respuestas es la tarea pedida, por lo que reformular está permitido. Todo dato lleva fuente; lo que no sea literal ni confirmado se etiqueta `[Inferencia]` o `[PENDIENTE]`. Los mensajes de error y las etiquetas de pantalla se copian literales del código. Si no estás de acuerdo con esta excepción, se elimina esta regla.

### Arranque
Lee `progress/current.md` y `config-docs.md`. Si `config-docs.md` tiene `POR CONFIRMAR`, resuélvelos antes de documentar: lo que esté en `docusaurus.config.*` o `package.json` se lee (solo lectura, sin credenciales) y se anota con su origen; el resto se pregunta al humano (Rule #0, máximo 3 por ronda). Sin la ruta del código no hay exploración: se pide al humano y se explica que Claude Code necesita acceso de lectura a esa ruta (por ejemplo, abriendo la sesión con `--add-dir`).

### Flujo
```
Documentación (este repositorio)
├── 0. Configuración   → config-docs.md completo
├── A. Actores         → docs-tecnica/actores/actores-del-sistema.md
├── B. Módulo          → docs-tecnica/modulos/MOD-NN-*/index.md   (definición, casos de uso, funcionalidades)
├── C. Especificación  → docs-tecnica/especificaciones/MOD-NN-*/FUNC-MODNN-NN-*.md
├── D. Permisos        → docs-tecnica/permisos/PERM-MOD-NN-*.md
├── E. Guía y FAQs     → docs-usuario/guias/MOD-NN-*/FUNC-MODNN-NN-*.md, faqs.md
├── F. Revisión        → SESIÓN NUEVA: Revisor R1–R8 → quita draft o devuelve hallazgos
│        ▲                                   │
│        └──── progress/review_<ID>.md ◄─────┘   (bucle C–E ↔ F, máximo 2 rondas)
└── G. Publicación     → la haces tú (build y despliegue del sitio)
```
Antes de las fases B a E, el Documentador pide al Explorador lo que el código pueda responder (actores y permisos, pantallas y etiquetas, validaciones y mensajes, flujo). Cada fase termina con tu aprobación.

### Mapa de archivos
| Archivo | Contenido | Cuándo leerlo |
|---|---|---|
| `progress/current.md` | Estado de la sesión activa | Siempre, al empezar |
| `progress/history.md` | Bitácora de sesiones anteriores (solo se añade al final) | Si necesitas contexto histórico |
| `progress/explore_*.md` | Hallazgos del código con `archivo:línea` | Al redactar y al revisar |
| `progress/review_*.md` | Hallazgos del revisor por ID y ronda | Al corregir |
| `config-docs.md` | Ruta del código, `routeBasePath`, versión y datos del sitio | Siempre, al empezar |
| `docs-tecnica/`, `docs-usuario/` | Contenido publicable | Al trabajar un módulo |
| `.claude/templates/plantillas.md` | Plantilla de cada artefacto y patrones de diagramas | Antes de crear cualquier página |
