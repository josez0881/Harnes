# BOOTSTRAP — Generador de harness para Claude Code

> Este archivo es una instrucción ejecutable. Si eres Claude Code y el humano te pidió
> «ejecuta BOOTSTRAP.md», sigue las fases en orden. Al terminar, el repositorio tendrá un
> harness adaptado a **su** proyecto (stack, comandos, convenciones y flujo reales),
> sin reglas heredadas de otro lenguaje ni de otro proyecto.

## 0. Uso (para el humano)

1. Copia este archivo a la raíz del repositorio.
2. Abre Claude Code en la raíz y escribe: «Ejecuta BOOTSTRAP.md».
3. Responde, si las hay, las pocas preguntas bloqueantes de la fase 2 (el resto lo decide el modelo y te lo informa).
4. Revisa lo generado con `git diff` / `git status`. Nada se commitea solo.
5. Cuando estés conforme, archiva o borra este archivo.

---

## 1. Qué es un harness (contexto para ti, el modelo)

Un harness es el conjunto de archivos y reglas que permite que un agente trabaje sobre un
repositorio de forma autónoma **y verificable**. Los principios que debes materializar:

1. **El repositorio es el sistema.** Lo que el agente necesita saber vive en archivos, no en el chat.
2. **Divulgación progresiva.** Un mapa corto que apunta a documentos; no una biblia de reglas.
3. **Una unidad de trabajo a la vez.**
4. **Estado en disco.** Sobrevive a reinicios y a contextos agotados.
5. **Verificación honesta y bajo demanda.** Las pruebas se ejecutan solo cuando el humano lo pide. Lo que no
   se ejecutó se declara «no verificado»; el agente no afirma que funciona.
6. **Separación de roles.** El líder no implementa, el implementador no se autoaprueba, el revisor no edita código.
7. **Anti teléfono descompuesto.** Los subagentes escriben sus resultados en archivos y devuelven una sola línea con la referencia.
8. **Se evalúa el estado final, no el camino.** Criterios objetivos en `CHECKPOINTS.md`.
9. **Seguridad antes que verificación.** Ejecutar pruebas puede modificar o destruir datos. Ningún comando
   se ejecuta sin haber demostrado, con evidencia del repo, que no toca datos ni servicios de desarrollo
   o producción (Gate de aislamiento, §3.1).

---

## 2. Reglas del bootstrap (obligatorias)

- **Evidencia primero.** Todo dato del proyecto (comando, convención, capa de arquitectura,
  política de dependencias) debe apoyarse en un archivo del repo que puedas citar. Sin evidencia:
  escribe `POR CONFIRMAR` y pregunta al humano. No rellenes huecos.
- **No importes convenciones de otro stack.** Este documento es neutro a propósito. Si un ejemplo
  de aquí coincide con tu stack, igualmente verifícalo contra el repo.
- **Sin hooks, sin `init.sh`, sin `.claude/settings.json`.** Cuando el humano pide verificar, los agentes
  ejecutan lo que dice `docs/verification.md`; no se automatiza con hooks. Límite conocido: sin hooks, que se
  verifique depende de que los agentes sigan las instrucciones, no de un mecanismo que lo fuerce.
- **No crees scripts ni instales dependencias.** La verificación se expresa con comandos que **ya
  existen** en el proyecto (los declara su manifiesto, task runner, CI o README) y se documenta en
  `docs/verification.md`. Si el proyecto no tiene ninguna forma de verificar, regístralo como
  brecha y pregunta al humano; no la inventes.
- **Aislamiento antes que ejecución (regla de seguridad).** No se ejecuta ningún comando que corra pruebas,
  migraciones, seeds o builds con efectos, ni nada que se conecte a una base de datos, caché, cola,
  almacenamiento, correo o API externa, hasta superar el **Gate de aislamiento** (§3.1). Que un comando
  figure en el README o en la CI no prueba que sea seguro en esta máquina: la CI suele tener su propio
  entorno. Sin prueba de aislamiento, no se ejecuta y se registra `no ejecutado: aislamiento no verificado`.
- **Verificación bajo demanda (regla de costo).** Ningún agente ejecuta pruebas por iniciativa propia: ni al
  arrancar, ni tras implementar, ni al cerrar una unidad. Solo se ejecutan cuando el humano lo pide de forma
  explícita, y por defecto con alcance **dirigido** (solo lo relacionado con lo implementado). La suite completa
  requiere que el humano la pida expresamente. Detalle en §5.5 (*Política de ejecución*).
- **No sobrescribas.** Si ya existen `CLAUDE.md`, `.claude/`, `docs/` u otros archivos del
  harness, léelos, propón un merge y espera aprobación.
- **No edites código fuente ni tests del proyecto** durante el bootstrap. Solo archivos del harness.
- **Preguntas al humano:** de una línea, con opciones para elegir, máximo 3 por ronda.
  Si dispones de una herramienta de preguntas interactivas, úsala.
- **Idioma** de los archivos generados: el que el humano usa contigo, salvo que el repo documente otro.
- **Tamaño:** `CLAUDE.md` corto; el detalle va a `docs/`.

---

## 3. Fase 1 — Descubrimiento (solo lectura)

Objetivo: construir un perfil del proyecto con evidencia. Puedes leer, listar, buscar y ejecutar
comandos de solo lectura (historial de git, estado, listados). **No ejecutes tests, builds, migraciones ni
nada que se conecte a datos o servicios**: la ejecución solo puede ocurrir en la fase 4 y únicamente si
supera el Gate de aislamiento (§3.1). Puedes leer archivos de configuración de conexión **solo para
identificar el destino** (motor, nombre de la base de datos, host); no leas ni copies credenciales, claves
ni tokens, ni al chat ni a ningún archivo.

Si ya existe un harness generado por este bootstrap, entra en **modo actualización**: léelo,
compáralo contra el estado actual del repo y propón un diff en vez de regenerar.

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
| Harness previo | `CLAUDE.md`, `AGENTS.md`, `.claude/`, `docs/` existentes |

**Salida:** un *perfil del proyecto* en el chat (todavía sin archivos) con columnas
`Dato | Valor | Evidencia (archivo) | Confianza (alta / media / baja / POR CONFIRMAR)`.

### 3.1 Gate de aislamiento (obligatorio antes de ejecutar cualquier comando de verificación)

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
   comando `AISLADO` puede ejecutarse, y el primero que toque estado requiere confirmación humana (§6).
6. **Si es `NO AISLADO` o `NO VERIFICADO`, no ejecutes.** Registra `no ejecutado: aislamiento <ausente|no
   verificado>` con el motivo y pregunta al humano con una sola pregunta de opciones:
   (a) él corrige la configuración de pruebas y tú vuelves a analizar; (b) él ejecuta el comando y te pega
   la salida; (c) él declara en el chat que el destino es desechable o tiene respaldo, y lo registras como
   `[decisión del humano]` (riesgo suyo). No modifiques configuración ni código para «arreglar» el
   aislamiento durante el bootstrap: propón el cambio.

---

## 4. Fase 2 — Decisiones (autónomas, con evidencia)

Con el perfil, decide tú; no esperes aprobación previa. Criterios por defecto:

1. **Unidad de trabajo.** Si el repo ya tiene backlog, tracker o documentación de historias, úsalo y
   refiérelo por su ID (no lo dupliques). Si no, `backlog.json` vacío.
2. **Comandos de verificación.** Elige los que ya corre la CI o documenta el README; si hay varios
   candidatos, prioriza los de la CI. Documenta además **cómo ejecutar un subconjunto** de pruebas (por
   archivo, por nombre o por etiqueta) con el patrón exacto, para poder hacer ejecuciones dirigidas.
3. **Versionado de `progress/`.** Por defecto, todo en git.

Marca cada decisión tuya como `[decisión del modelo: <motivo>]` y lístalas en el informe final, para
que el humano pueda revertirlas. Pregunta al humano **solo** si un dato bloquea y no hay evidencia
(una sola ronda, máximo 3 preguntas de una línea, con opciones para elegir).

---

## 5. Fase 3 — Generación de archivos

Reglas de generación:

- Cada archivo usa rutas y comandos **reales** del proyecto.
- Al terminar no puede quedar ningún marcador sin resolver (`<...>`, `{{...}}`), salvo `POR CONFIRMAR` explícito.
- Cada regla en `docs/` lleva su origen entre corchetes: `[observado: <archivo>]`,
  `[decisión del modelo: motivo]`, `[decisión del humano]` o `POR CONFIRMAR`.

Árbol objetivo:

```
CLAUDE.md
CHECKPOINTS.md
<backlog>                      # según la decisión 1
.claude/agents/leader.md
.claude/agents/implementer.md
.claude/agents/reviewer.md
.claude/agents/explorer.md
docs/architecture.md
docs/conventions.md
docs/verification.md
progress/current.md
progress/history.md
```

### 5.1 `CLAUDE.md` — punto de entrada único

Se carga en cada sesión. No generes `AGENTS.md`; si ya existe uno (por otra herramienta), no lo
toques y referéncialo desde aquí. Contenido:

- **Rol obligatorio: leader.** Coordina y no implementa.
- **Rutas protegidas para el líder:** lista explícita (con patrones) de las rutas de código y tests
  que descubriste. Y qué sí puede editar: docs, configuración del harness, `progress/`, backlog.
- **Reglas duras:** una unidad de trabajo a la vez; no marcar `done` sin un
  `progress/review_<id>.md` con veredicto APPROVED, y dejar siempre en el backlog el campo `verificacion`
  con lo realmente ejecutado; no ejecutar pruebas salvo petición explícita del humano (*Política de
  ejecución* de `docs/verification.md`); ante un fallo inesperado de herramienta,
  sin workaround: documentar el bloqueo en `progress/current.md` y parar; no ejecutar
  migraciones, seeds, reinicios de base de datos ni pruebas cuyo comando no esté marcado `AISLADO` en
  `docs/verification.md`; ante la duda, preguntar al humano.
- **Protocolo de arranque:** leer este mapa, el backlog y `progress/current.md`. **No ejecutar pruebas al
  arrancar.**
- **Mapa** (tabla `Archivo | Qué contiene | Cuándo leerlo`) hacia todo lo generado.
- **Cierre de sesión:** campo `verificacion` de cada unidad cerrada reflejando lo realmente ejecutado, estado correcto en el backlog, resumen de
  `current.md` movido al final de `history.md`, `current.md` vaciado a su plantilla, repo limpio
  (sin temporales ni restos de depuración según `docs/conventions.md`).
- **Anti teléfono descompuesto:** los subagentes devuelven una línea con referencia a archivo.
- **Cuándo NO aplica el rol:** preguntas de lectura/exploración (responde directamente) y cambios
  fuera de las rutas protegidas.
- **Mantenimiento:** si el agente tuvo que adivinar el mismo dato dos veces, o el revisor rechaza
  por una regla ambigua, se corrige `docs/` y se anota en `history.md`.

### 5.2 Agentes (`.claude/agents/*.md`)

Formato de cada archivo:

```
---
name: <igual al nombre del archivo, sin extensión>
description: <una línea: cuándo debe invocarse>
tools: <lista mínima necesaria>
---
```

| Agente | `tools` | Responsabilidad |
|--------|---------|-----------------|
| `leader` | Read, Write, Edit, Glob, Grep, Bash, Agent | Descompone y coordina; escribe solo en archivos del harness |
| `implementer` | Read, Write, Edit, Glob, Grep, Bash | Ejecuta **una** unidad de trabajo |
| `reviewer` | Read, Write, Glob, Grep, Bash | Aprueba o rechaza; solo escribe su informe, no edita código |
| `explorer` | Read, Write, Glob, Grep, Bash | Responde **una** pregunta acotada; solo escribe su informe |

**leader** — Protocolo de arranque (igual que en `CLAUDE.md`). Descomposición: identifica si la
tarea es una o varias unidades; lanza explorers en paralelo si hay que investigar; lanza un
implementer por unidad; al terminar, lanza un reviewer. Incluye una **tabla de escalado de
esfuerzo** (trivial / media / compleja / muy compleja → cuántos subagentes y de qué tipo) expresada
en la terminología del proyecto (módulos, paquetes, servicios). Incluye un ejemplo de instrucción
correcta a un subagente: pide escribir en archivo y responder solo con la referencia.
El líder marca `done` únicamente si existe `progress/review_<id>.md` con APPROVED. No edita rutas
protegidas y no acepta resultados por chat sin referencia a archivo.

**implementer** — Lee `CLAUDE.md` y los 3 docs. Toma una unidad `pending`, la pasa a `in_progress`,
anota el plan (3-5 viñetas) en `progress/current.md`. Implementa dentro del alcance de su
`acceptance`. Escribe o actualiza las pruebas según `docs/verification.md`, **sin ejecutarlas** salvo que el humano lo haya pedido
explícitamente; si lo pidió, ejecuta solo el alcance pedido (dirigido por defecto) y solo comandos marcados
`AISLADO` (si uno necesario no lo está, marca `blocked` y no lo ejecutes); si falla, vuelve a implementar. Si no
ejecutó nada, su informe dice «Verificación: no ejecutada» y deja listos los comandos dirigidos para que el
humano los pida o los pegue. Escribe su informe en `progress/impl_<id>.md` (archivos
tocados, decisiones, pruebas escritas y, si se ejecutó algo, su salida). **No marca `done` ni se autoaprueba.** Si descubre
que el cambio toca otra unidad, o una herramienta falla de forma inesperada: marca `blocked`,
documenta en `progress/current.md` y termina. Respuesta final en chat, una línea:
`done -> progress/impl_<id>.md` o `blocked -> ver progress/current.md`.

**reviewer** — Lee los 3 docs y `CHECKPOINTS.md`. Identifica los cambios (estado del repo + informe
del implementer). Por cada archivo cambiado evalúa arquitectura, convenciones y prueba
correspondiente. Revisa el código y las pruebas de forma estática; ejecuta pruebas solo si el humano lo pidió, con la misma política (alcance dirigido por defecto, solo comandos `AISLADO`). Recorre `CHECKPOINTS.md`.
Escribe `progress/review_<id>.md` con: veredicto `APPROVED | CHANGES_REQUESTED`, checkpoints
marcados con razón concreta (archivo y línea) y cambios requeridos numerados. Respuesta en chat, una
línea: `APPROVED -> ver progress/review_<id>.md` o `CHANGES_REQUESTED -> ver progress/review_<id>.md`.
Reglas duras: no aprueba con verificación en rojo cuando se ejecutó; si no se ejecutó, su informe lo declara («APPROVED sobre revisión estática, verificación no ejecutada») y no afirma que funciona; no edita código ajeno, no da feedback genérico.

**explorer** — Recibe una pregunta concreta. Escribe hallazgos con rutas citadas en
`progress/explore_<tema>.md`. Respuesta: `done -> progress/explore_<tema>.md`. No modifica nada más.

### 5.3 `docs/architecture.md` — qué significa «buen trabajo» aquí

Capas o módulos reales y sus reglas de dependencia; política observada sobre dependencias externas;
manejo de errores observado; flujo de datos (diagrama ASCII breve); «qué NO hacer» derivado de
patrones o documentación del repo. El revisor evaluará contra este archivo: **no declares un
requisito que el repo no evidencie**.

### 5.4 `docs/conventions.md`

Estilo, nombres, estructura de archivo, organización y nombrado de tests, manejo de errores,
comentarios, mensajes de commit. Cita la configuración que lo respalda. Si hay un formateador
automático, el formateador manda.

### 5.5 `docs/verification.md`

Regla de oro: el agente no dice «funciona» sin haberlo ejecutado; si no se ejecutó, dice «no verificado». Niveles:

1. **Dirigida** (solo las pruebas relacionadas con lo cambiado).
2. **Completa** (suite entera; solo si el humano la pide expresamente).
3. **Integración / extremo a extremo**, si aplica.
4. **Smoke manual**, opcional.

Por cada nivel: comando exacto hallado, dónde se declara, prerrequisitos (servicios, base de datos,
variables) y **tiempo observado** (`desconocido` hasta la primera ejecución bajo demanda; se actualiza después de
cada ejecución). Para el nivel dirigido, el patrón exacto para ejecutar (a) un archivo, (b) un nombre o filtro,
(c) una etiqueta o grupo; si el runner no lo permite, regístralo como brecha. Si falta un nivel, regístralo como brecha.

**Política de ejecución (bajo demanda).** Inclúyela en el documento con este contenido:

- Por defecto no se ejecuta nada. Implementar una unidad significa escribir o actualizar código y pruebas, sin correrlas.
- Cuenta como petición explícita lo que el humano dice con ese fin («corre las pruebas», «valida lo
  implementado», «ejecuta los tests de X», «verifica que funciona»). **No** cuentan «implementa», «termina la
  tarea» ni «cierra la unidad». La petición vale para la acción en curso; solo es permanente si el humano lo dice.
- Alcance: **dirigido** por defecto (pruebas relacionadas con lo tocado, con el patrón documentado). Suite
  **completa** solo si el humano dice «suite completa», «todas las pruebas» o equivalente. Si no puedes
  determinar un subconjunto dirigido, no caigas en la completa: pregunta con opciones (completa / indicar
  archivo o filtro / no ejecutar).
- Antes de ejecutar un nivel con tiempo observado largo, indica ese tiempo.
- Se aplica el Gate de aislamiento incluso bajo demanda.
- Si no se ejecutó nada, los informes dicen «Verificación: no ejecutada» y proponen los comandos dirigidos listos para pegar.
- Cada ejecución se anota en una sección **Registro de ejecuciones** (fecha, alcance, comando, resultado, duración).

Incluye una tabla de **aislamiento** con una fila por comando:

| Comando | Nivel | Recursos con estado que toca | Evidencia de destino distinto (archivo:línea) | Veredicto | Confirmación humana |
|---|---|---|---|---|---|
| `<comando>` | Completa | BD, caché… | `<archivo:línea>` | `AISLADO` / `NO AISLADO` / `NO VERIFICADO` | `<fecha>` / `no requerida` / `pendiente` |

Solo los comandos `AISLADO` pueden ser ejecutados por los agentes. Para el resto escribe qué falta para
poder clasificarlos como `AISLADO` (sin aplicarlo tú). Añade anti-patrones (afirmar sin evidencia ejecutable; pruebas que solo
comprueban que no hay excepción; declarar «funciona» sin haber ejecutado). El **Registro de ejecuciones** empieza
vacío con la nota `no ejecutado: política bajo demanda`.

### 5.6 Backlog

Según la decisión 1:

- **Archivo en el repo:** `backlog.json` (o el formato que el proyecto ya use) con, por unidad:
  `id`, `title`, `description`, `acceptance[]`, `status`, `verificacion`, `notes`. `verificacion`:
  `no_ejecutada` | `dirigida_ok` | `completa_ok` | `fallida`. Estados válidos: `pending`,
  `in_progress`, `done`, `blocked`. Reglas: máximo una `in_progress`, ids únicos. Sin script de
  validación: las comprueban el líder al arrancar y el revisor. **Empieza vacío; no inventes trabajo.**
- **Tracker externo:** no dupliques el backlog en archivo. Documenta en `docs/` cómo leerlo y
  actualizarlo (herramienta o conector disponible) y el mapeo de estados.

### 5.7 `progress/`

- `current.md`: plantilla con unidad en curso, inicio, agente, plan, bitácora y próximo paso.
  Se vacía al cerrar cada sesión.
- `history.md`: bitácora *append-only*. Primera entrada: «Bootstrap del harness», con fecha real
  (obtenla del sistema) y lista de archivos generados.
- Informes por rol: `impl_<id>.md`, `review_<id>.md`, `explore_<tema>.md`.

### 5.8 `CHECKPOINTS.md`

Criterios objetivos de estado final, cada uno con casillas `[ ]` que el revisor marca:

- **C1 — Arnés completo:** existen los archivos del árbol objetivo; cada comando de verificación está
  clasificado en `docs/verification.md` (`AISLADO` / `NO AISLADO` / `NO VERIFICADO`), lo que se
  ejecutó fue `AISLADO` y con confirmación humana, y lo demás consta como `no ejecutado` con su motivo (política
  bajo demanda o aislamiento).
- **C2 — Estado coherente:** como máximo una unidad `in_progress`; toda unidad `done` tiene
  `review_<id>.md` APPROVED y su campo `verificacion` refleja lo realmente ejecutado; `current.md` vacío o describiendo la sesión activa.
- **C3 — Código respeta la arquitectura:** cumple `docs/architecture.md`; sin dependencias nuevas
  sin aprobación; sin restos de depuración según `docs/conventions.md`.
- **C4 — Verificación honesta:** el código cambiado tiene pruebas escritas o actualizadas según
  `docs/verification.md`; el informe declara qué se ejecutó (o `no ejecutada`) y no afirma resultados que no se
  obtuvieron; si se ejecutó algo, hay resultados concretos.
- **C5 — Sesión cerrada:** repo limpio, entrada en `history.md`, estado correcto en el backlog.
- **C6 — Sin efectos colaterales ni costos no pedidos:** ningún comando ejecutado en la sesión tenía veredicto
  distinto de `AISLADO` y no se ejecutó ninguna prueba sin petición explícita del humano; los informes no muestran señales de datos o servicios de desarrollo/producción alterados.

Añade checkpoints específicos del proyecto **solo** si tienen evidencia (p. ej. una política
documentada de migraciones o de seguridad). El revisor rechaza el cierre si queda alguna casilla vacía.

---

## 6. Fase 4 — Validación y entrega

1. **Sin ejecución de pruebas.** El bootstrap no ejecuta pruebas, suites ni builds (política bajo demanda).
   a. Clasifica cada comando de verificación con el Gate (§3.1) y escribe la tabla de aislamiento y los patrones
      de ejecución dirigida en `docs/verification.md`.
   b. Deja el *Registro de ejecuciones* con `no ejecutado: política bajo demanda`.
   c. Solo si el humano pidió explícitamente verificar en esta sesión: ejecuta únicamente comandos `AISLADO`,
      con alcance dirigido salvo petición expresa de la completa, de menor a mayor riesgo; antes del primer
      comando que toque estado muestra el comando exacto, los recursos y el destino (sin credenciales) y
      pregunta con opciones (ejecutar / no ejecutar / lo ejecuto yo); ejecuta `git status` antes y después
      y reporta cambios inesperados; si aparecen señales de destino equivocado, detente e informa de inmediato.
      Anota la ejecución en el *Registro de ejecuciones*.
2. **Consistencia.** Sin marcadores sin resolver; toda ruta citada existe; todo comando citado
   tiene evidencia; como máximo una unidad `in_progress`; el mapa de `CLAUDE.md` coincide con los
   archivos reales; el `name` de cada agente coincide con su archivo.
3. **Auditoría.** Lanza el `reviewer` generado para evaluar C1 y C2 y contrastar las afirmaciones de
   `docs/` con el repo. Debe escribir `progress/review_bootstrap.md`. En esta auditoría el reviewer **no
   ejecuta** comandos de verificación: solo contrasta afirmaciones con archivos.
4. **Informe final al humano** (en chat, breve): archivos creados o modificados, lista de
   decisiones tomadas por ti (`[decisión del modelo]`), lista de `POR CONFIRMAR` pendientes, brechas detectadas (p. ej. ausencia de pruebas), que no se ejecutó ninguna prueba (política bajo demanda) y cómo pedirlas, y cómo probar el harness: pedir «implementa la siguiente tarea pendiente» con una unidad
   trivial que el humano añada al backlog.
5. **No hagas commit.** Deja los cambios para revisión.
6. Registra el cierre en `progress/history.md`.

---

## 7. Criterios de finalización del bootstrap

- [ ] Existen todos los archivos del árbol objetivo. No existe `.claude/settings.json` generado por este bootstrap.
- [ ] Cada dato del proyecto en `docs/` tiene origen citado o `POR CONFIRMAR`.
- [ ] Ningún archivo contiene convenciones que el repo no respalde.
- [ ] Cada comando está clasificado por el Gate y los patrones de ejecución dirigida están documentados (o registrados como brecha).
- [ ] Ningún comando se ejecutó sin veredicto `AISLADO`, sin confirmación humana previa ni sin petición explícita.
- [ ] `progress/review_bootstrap.md` existe y fue leído por ti antes del informe final.
- [ ] El humano recibió el informe final.

---

## 8. Modo parche de seguridad (harness ya generado con una versión anterior de este bootstrap)

Aplica si ya existen `CLAUDE.md` y `docs/verification.md` generados antes y no contienen el Gate de
aislamiento ni veredictos `AISLADO / NO AISLADO / NO VERIFICADO`.

1. **No ejecutes ningún comando de verificación** durante el parche.
2. Aplica el Gate (§3.1) a cada comando documentado y reescribe en `docs/verification.md` la tabla de
   aislamiento. Marca la *Línea base* anterior como «obtenida sin aislamiento comprobado»; no la uses como referencia.
3. Propón al humano un diff y espera su aprobación antes de editar: protocolo de arranque y reglas duras
   de `CLAUDE.md`, líneas de verificación de `implementer` y `reviewer`, y C1, C2, C4 y C6 de `CHECKPOINTS.md`. Añade la *Política de ejecución* y los patrones de ejecución dirigida a
   `docs/verification.md`, y el campo `verificacion` al backlog (`no_ejecutada` en las unidades ya cerradas sin evidencia).
   Conserva el resto.
4. Registra «Parche de aislamiento» en `progress/history.md`.
5. Dile al humano que no puedes saber si la ejecución anterior alteró datos y que conviene revisar la base
   de datos de desarrollo (por ejemplo, comparándola con un respaldo).
