# BOOTSTRAP — Adaptación del harness base al proyecto

> Este archivo es una instrucción ejecutable. Si eres Claude Code y el humano te pidió
> «ejecuta BOOTSTRAP.md», sigue las fases en orden. El harness **ya está armado** en este
> repositorio con reglas genéricas; tu trabajo es **descubrir el proyecto y adaptarlo** con
> evidencia, sin reglas heredadas de otro lenguaje ni de otro proyecto.

## 0. Uso (para el humano)

1. Descomprime el zip en la raíz del repositorio.
   - Si el repo **ya tiene** `CLAUDE.md`, `.claude/`, `docs/` u otros archivos con esos nombres, descomprime en una carpeta `_harness_base/` en la raíz: el modelo hará una fusión (§7) en vez de sobrescribir.
2. Abre Claude Code en la raíz y escribe: «Ejecuta BOOTSTRAP.md».
3. Responde, si las hay, las pocas preguntas bloqueantes (máximo 3, de una línea, con opciones).
4. Revisa lo adaptado con `git diff` / `git status`. Nada se commitea solo.

---

## 1. Qué hay ya armado y qué te toca

Ya existen con contenido genérico: `CLAUDE.md`, `CHECKPOINTS.md`, `backlog.json`, `.claude/agents/{leader,implementer,reviewer,explorer}.md`, `docs/{architecture,conventions,verification}.md` y `progress/{current,history}.md`.

Las **reglas genéricas** (roles separados, una unidad a la vez, estado en disco, Gate de aislamiento, verificación bajo demanda, anti teléfono descompuesto) ya están escritas. **No las reescribas ni las borres**: si algo no encaja con el proyecto (por ejemplo, no tiene pruebas), regístralo como brecha y pregunta al humano.

Lo que debes completar son los marcadores `[POR ADAPTAR: ...]`: contienen lo que depende del proyecto. Al terminar no debe quedar ninguno (§6).

### Reglas del bootstrap (obligatorias)

- **Evidencia primero.** Todo dato del proyecto (comando, convención, capa, política de dependencias) debe apoyarse en un archivo del repo que puedas citar. Sin evidencia: escribe `POR CONFIRMAR` y pregunta al humano. No rellenes huecos.
- **No importes convenciones de otro stack.** Si un ejemplo de aquí coincide con tu stack, igualmente verifícalo contra el repo.
- **Sin hooks, sin `init.sh`, sin `.claude/settings.json`.** Cuando el humano pide verificar, los agentes ejecutan lo que dice `docs/verification.md`. Límite conocido: sin hooks, que se verifique depende de que los agentes sigan las instrucciones, no de un mecanismo que lo fuerce.
- **No crees scripts ni instales dependencias.** La verificación se expresa con comandos que **ya existen** en el proyecto (manifiesto, task runner, CI o README). Si el proyecto no tiene ninguna forma de verificar, regístralo como brecha y pregunta; no la inventes.
- **Aislamiento antes que ejecución.** No se ejecuta ningún comando que corra pruebas, migraciones, seeds o builds con efectos, ni nada que se conecte a una base de datos, caché, cola, almacenamiento, correo o API externa, hasta superar el **Gate de aislamiento** (§2.1). Que un comando figure en el README o en la CI no prueba que sea seguro en esta máquina. Sin prueba de aislamiento, no se ejecuta y se registra `no ejecutado: aislamiento no verificado`.
- **Verificación bajo demanda.** Ningún agente ejecuta pruebas por iniciativa propia (ni al arrancar, ni tras implementar, ni al cerrar una unidad). Solo cuando el humano lo pide de forma explícita, por defecto con alcance dirigido; la suite completa requiere petición expresa. El detalle está en `docs/verification.md`.
- **No edites código fuente ni tests del proyecto** durante el bootstrap. Solo archivos del harness.
- **Preguntas al humano:** de una línea, con opciones para elegir, máximo 3 por ronda. Si dispones de una herramienta de preguntas interactivas, úsala.
- **Idioma** de los datos que escribas: el que el humano usa contigo, salvo que el repo documente otro.
- **Tamaño:** `CLAUDE.md` corto; el detalle va a `docs/`.

---

## 2. Fase 1 — Descubrimiento (solo lectura)

Objetivo: construir un perfil del proyecto con evidencia. Puedes leer, listar, buscar y ejecutar
comandos de solo lectura (historial de git, estado, listados). **No ejecutes tests, builds, migraciones ni
nada que se conecte a datos o servicios**: la ejecución solo puede ocurrir en la fase 4 y únicamente si
supera el Gate de aislamiento (§2.1). Puedes leer archivos de configuración de conexión **solo para
identificar el destino** (motor, nombre de la base de datos, host); no leas ni copies credenciales, claves
ni tokens, ni al chat ni a ningún archivo.

Si el estado de `CLAUDE.md` ya es `ADAPTADO`, entra en **modo actualización** (§7): léelo,
compáralo contra el estado actual del repo y propón un diff en vez de volver a adaptar.

Si el repo es grande (monorepo, muchos módulos), puedes lanzar 2-3 subagentes exploradores en
paralelo, cada uno con una pregunta acotada, que escriban en `progress/explore_<tema>.md` y
respondan solo `done -> progress/explore_<tema>.md`.

| Tema | Dónde mirar (pistas, no lista exhaustiva) |
|------|--------------------------------------------|
| Stack y lenguajes | Archivos de manifiesto y lockfiles (raíz y subcarpetas), extensiones predominantes |
| Entorno e instalación | README, CONTRIBUTING, definiciones de contenedores, versiones declaradas, ejemplos de variables de entorno |
| Cómo se ejecuta | Scripts/tareas declarados en el manifiesto o task runner, README |
| Cómo se verifica (tests, lint, tipos, build) | Manifiesto, task runner, configuración de CI, README |
| Estructura y capas | Árbol de directorios, nombres de módulos, dependencias entre carpetas |
| Convenciones | Configuración de formateadores/linters, `.editorconfig`, muestreo de 5-10 archivos representativos (nombres, estilo, errores, comentarios) |
| Tests | Ubicación, framework, patrón de nombres, cómo se aísla el estado (BD, filesystem, red) |
| Aislamiento de pruebas | Qué recursos tocan los tests (BD, caché, colas, archivos, correo, APIs); qué archivo de entorno o configuración cargan y si difiere del de desarrollo; si la preparación recrea, migra, vacía o siembra datos; servicios declarados en contenedores; variables de entorno que el comando hereda del entorno de desarrollo |
| Flujo de trabajo | Historial reciente (estilo de commits), plantillas de PR/issues, ramas, tracker referenciado |
| Zonas sensibles | Secretos, `.env`, migraciones, archivos generados, despliegue, bases de datos o servicios de desarrollo y producción, carpetas que no se tocan |
| Documentación y backlog existentes | `docs/` del proyecto, tracker, historias de usuario, roadmap (se referencian, no se duplican) |

**Salida:** un *perfil del proyecto* en el chat (todavía sin archivos) con columnas
`Dato | Valor | Evidencia (archivo) | Confianza (alta / media / baja / POR CONFIRMAR)`.

### 2.1 Gate de aislamiento (obligatorio antes de ejecutar cualquier comando de verificación)

Se aplica **por comando** y por cada recurso con estado que toque. Es un análisis de archivos, no una ejecución.

1. **Inventario de efectos.** ¿Qué toca el comando? Base de datos, caché, colas, almacenamiento, correo,
   APIs de terceros, filesystem fuera del repo, servicios compartidos. Incluye los efectos indirectos:
   arrancar la aplicación completa (puede cargar la configuración de desarrollo), la preparación de las
   pruebas (recrear esquema, migrar, sembrar, vaciar tablas) y los plugins o hooks del test runner.
2. **Prueba de destino distinto.** Para cada recurso con estado, cita evidencia (archivo y línea) de que,
   *mientras corre ese comando*, el destino es **distinto** del de desarrollo y producción. Evidencia válida:
   (a) la configuración de pruebas fija explícitamente el destino de pruebas (nombre de BD, host, ruta) en un
   archivo que el comando realmente carga; (b) el recurso es efímero (en memoria, archivo temporal,
   contenedor desechable levantado por el propio comando); (c) el recurso está simulado y no hay conexión real.
   **No son evidencia:** que exista una BD de pruebas «en algún sitio»; valores comentados, vacíos o
   heredados del entorno; documentación que lo afirme sin respaldo en configuración; que la CI lo haga así.
3. **Precedencia.** Averigua qué gana cuando hay varias fuentes (variables del shell o del archivo de
   desarrollo frente a la configuración de pruebas). Si una variable heredada puede imponerse sobre la
   configuración de pruebas y el comando no la fija, el aislamiento **no está probado**.
4. **Destructividad.** Si la preparación de las pruebas recrea, migra, vacía o siembra datos, el comando es
   destructivo: el aislamiento es obligatorio y solo una decisión explícita del humano (punto 6c) puede
   exceptuarlo.
5. **Veredicto por comando:** `AISLADO` (evidencia para todos los recursos con estado), `NO AISLADO`
   (hay evidencia de que apunta a desarrollo o producción) o `NO VERIFICADO` (falta evidencia). Solo un
   comando `AISLADO` puede ejecutarse, y el primero que toque estado requiere confirmación humana (§5).
6. **Si es `NO AISLADO` o `NO VERIFICADO`, no ejecutes.** Registra `no ejecutado: aislamiento <ausente|no
   verificado>` con el motivo y pregunta al humano con una sola pregunta de opciones:
   (a) él corrige la configuración de pruebas y tú vuelves a analizar; (b) él ejecuta el comando y te pega
   la salida; (c) él declara en el chat que el destino es desechable o tiene respaldo, y lo registras como
   `[decisión del humano]` (riesgo suyo). No modifiques configuración ni código para «arreglar» el
   aislamiento durante el bootstrap: propón el cambio.

---

## 3. Fase 2 — Decisiones (autónomas, con evidencia)

Con el perfil, decide tú; no esperes aprobación previa. Criterios por defecto:

1. **Unidad de trabajo.** Si el repo ya tiene backlog, tracker o documentación de historias, úsalo y refiérelo por su ID (no lo dupliques). Si no, `backlog.json` queda con `units` vacío.
2. **Comandos de verificación.** Elige los que ya corre la CI o documenta el README; si hay varios candidatos, prioriza los de la CI. Documenta además **cómo ejecutar un subconjunto** de pruebas (por archivo, por nombre o por etiqueta) con el patrón exacto, para poder hacer ejecuciones dirigidas.
3. **Versionado de `progress/`.** Por defecto, todo en git.

Marca cada decisión tuya como `[decisión del modelo: <motivo>]` y lístalas en el informe final, para que el humano pueda revertirlas. Pregunta al humano **solo** si un dato bloquea y no hay evidencia (una sola ronda, máximo 3 preguntas de una línea, con opciones).

---

## 4. Fase 3 — Adaptación de los archivos

Reglas: usa rutas y comandos **reales** del proyecto. Cada regla en `docs/` lleva su origen entre corchetes: `[observado: <archivo>]`, `[decisión del modelo: motivo]`, `[decisión del humano]` o `POR CONFIRMAR`. Sustituye cada marcador `[POR ADAPTAR: ...]` por contenido real; si no aplica, escribe `No aplica` con el motivo.

| Archivo | Qué completar |
|---|---|
| `CLAUDE.md` | *Rutas protegidas* (patrones reales de código y tests); fila de documentación del proyecto en el mapa. El estado se cambia al final (§5). |
| `.claude/agents/leader.md` | Terminología del escalado de esfuerzo (módulos, paquetes, servicios…). |
| `docs/architecture.md` | Stack, capas y dependencias reales, política de dependencias, manejo de errores, flujo de datos (diagrama ASCII breve) y «qué NO hacer» derivado de patrones o documentación. |
| `docs/conventions.md` | Estilo, nombres, estructura, organización de tests, errores, comentarios y commits, citando la configuración que lo respalda. |
| `docs/verification.md` | Niveles con su comando exacto y prerrequisitos, patrones de ejecución dirigida, tabla de **aislamiento** con el veredicto del Gate por comando, anti-patrones propios. Sin ejecutar nada. |
| `backlog.json` | Según la decisión 1. Si el backlog está en un tracker externo, documenta en `docs/` cómo leerlo y el mapeo de estados, y deja `units` vacío. No inventes trabajo. |
| `CHECKPOINTS.md` | C7 (específicos), solo con evidencia; si no hay, `Ninguno`. |
| `progress/history.md` | Primera entrada «Adaptación del harness base» con la fecha real del sistema y la lista de archivos tocados. |

Comprueba también que el `name` de cada agente coincide con el nombre de su archivo.

---

## 5. Fase 4 — Validación y entrega

1. **Sin ejecución de pruebas.** El bootstrap no ejecuta pruebas, suites ni builds (política bajo demanda).
   a. Clasifica cada comando de verificación con el Gate (§2.1) y escribe la tabla de aislamiento en `docs/verification.md`.
   b. Deja el *Registro de ejecuciones* con `no ejecutado: política bajo demanda`.
   c. Solo si el humano pidió explícitamente verificar en esta sesión: ejecuta únicamente comandos `AISLADO`, con alcance dirigido salvo petición expresa de la completa, de menor a mayor riesgo; antes del primer comando que toque estado muestra el comando exacto, los recursos y el destino (sin credenciales) y pregunta con opciones (ejecutar / no ejecutar / lo ejecuto yo); ejecuta `git status` antes y después y reporta cambios inesperados; si aparecen señales de destino equivocado, detente e informa de inmediato. Anota la ejecución en el *Registro de ejecuciones*.
2. **Consistencia.** Busca el marcador `[POR ADAPTAR:` en todo el repo, **excluyendo este archivo** (que lo cita como instrucción): no debe quedar ninguno. Toda ruta citada existe; todo comando citado tiene evidencia; como máximo una unidad `in_progress`; el mapa de `CLAUDE.md` coincide con los archivos reales.
3. **Auditoría.** Lanza el `reviewer` para evaluar C1 y C2 y contrastar las afirmaciones de `docs/` con el repo. Debe escribir `progress/review_bootstrap.md`. En esta auditoría el reviewer **no ejecuta** comandos de verificación: solo contrasta afirmaciones con archivos.
4. **Informe final al humano** (en chat, breve): archivos modificados, decisiones tomadas por ti (`[decisión del modelo]`), lista de `POR CONFIRMAR` pendientes, brechas detectadas (p. ej. ausencia de pruebas), que no se ejecutó ninguna prueba (política bajo demanda) y cómo pedirlas, y cómo probar el harness: pedir «implementa la siguiente tarea pendiente» con una unidad trivial que el humano añada al backlog.
5. **Cierre:** cambia en `CLAUDE.md` el estado a `ADAPTADO <fecha real>`, mueve este archivo a `docs/BOOTSTRAP.md` (para reutilizarlo en modo actualización) y registra el cierre en `progress/history.md`.
6. **No hagas commit.** Deja los cambios para revisión.

---

## 6. Criterios de finalización

- [ ] No queda ningún marcador `[POR ADAPTAR:` en el repo (este archivo se excluye).
- [ ] Cada dato del proyecto en `docs/` tiene origen citado o `POR CONFIRMAR`.
- [ ] Ningún archivo contiene convenciones que el repo no respalde.
- [ ] Cada comando está clasificado por el Gate y los patrones de ejecución dirigida están documentados (o registrados como brecha).
- [ ] Ningún comando se ejecutó sin veredicto `AISLADO`, sin confirmación humana previa ni sin petición explícita.
- [ ] No existe `.claude/settings.json` generado por este bootstrap.
- [ ] `progress/review_bootstrap.md` existe y fue leído por ti antes del informe final.
- [ ] `CLAUDE.md` indica `ADAPTADO <fecha>` y el humano recibió el informe final.

---

## 7. Modos especiales

**Fusión (si existe `_harness_base/`).** Esa carpeta es el harness base y la raíz ya tiene archivos propios.
1. No sobrescribas nada. Por cada archivo del base que ya exista en la raíz, propón al humano una fusión: conserva el contenido del proyecto y añade el del harness (en `CLAUDE.md`, entre `<!-- harness:start -->` y `<!-- harness:end -->`). Espera su aprobación.
2. Copia los archivos que no existan.
3. Si los archivos existentes vienen de una versión anterior de este harness (sin Gate de aislamiento ni política bajo demanda), trátalo como actualización: **conserva los datos del proyecto ya descubiertos** y reemplaza las reglas genéricas por las del base. No ejecutes ningún comando de verificación durante la fusión.
4. Continúa con las fases normales. Al final, pregunta al humano si borras `_harness_base/`; no la borres sin su aprobación.

**Actualización (si `CLAUDE.md` ya dice `ADAPTADO`).** Compara lo documentado con el estado actual del repo y con la versión del base si el humano la aporta; reporta diferencias y propón un diff. No regeneres ni sobrescribas.
