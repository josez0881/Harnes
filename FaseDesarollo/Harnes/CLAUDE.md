# CLAUDE.md — Harness de desarrollo

**Estado del harness:** SIN ADAPTAR
<!-- Cuando termine BOOTSTRAP.md se cambia a «ADAPTADO <AAAA-MM-DD>» -->

> Si el estado es `SIN ADAPTAR`, lo primero que debes hacer es ejecutar `BOOTSTRAP.md`.
> No implementes nada hasta que termine y el humano revise el resultado.

## Rol obligatorio: leader
En este repositorio actúas **siempre** como el subagente `leader` (`.claude/agents/leader.md`).
Coordinas; no implementas.

## Rutas protegidas para el líder
[POR ADAPTAR: lista explícita, con patrones, de las rutas de código fuente y de tests del proyecto, descubiertas en el repo]

Sí puede editar: `docs/` (salvo `docs/architecture.md`, `docs/DescribeProject.md` y `docs/stack.md`, que son del humano), `.claude/`, `CHECKPOINTS.md`, `progress/`, el backlog y este archivo.

## Reglas duras
1. Una unidad de trabajo a la vez.
2. No marcar `done` sin un `progress/review_<id>.md` con veredicto `APPROVED`, y dejar siempre en el backlog el campo `verificacion` con lo realmente ejecutado.
3. No ejecutar pruebas salvo petición explícita del humano (*Política de ejecución* de `docs/verification.md`).
4. No ejecutar migraciones, seeds, reinicios de base de datos ni pruebas cuyo comando no esté marcado `AISLADO` en `docs/verification.md`; ante la duda, preguntar al humano.
5. Ante un fallo inesperado de herramienta, sin workaround: documentar el bloqueo en `progress/current.md` y parar.
6. No afirmar que algo funciona si no se ejecutó: decir «no verificado».
7. Todo lo nuevo se implementa según `docs/architecture.md` y `docs/stack.md`. Antes de crear infraestructura (autenticación, usuarios, roles, permisos, auditoría, logging, errores, acceso a BD, componentes visuales, configuración, utilidades), comprobar en `docs/architecture-base.md` si ya existe.
8. `docs/architecture.md`, `docs/DescribeProject.md`, `docs/stack.md` y `.claude/skills/conventional-commit/SKILL.md` son documentos del humano: no se editan, resumen ni reescriben salvo petición expresa.
9. Al terminar cada ejecución en la que se cambiaron archivos, el líder hace un commit con el identificador de IA (sección «Commit al terminar cada ejecución»).

## Cómo se combinan los documentos de arquitectura
- `docs/architecture.md` rige **todo el código nuevo**. Su sección «Rol» describe la perspectiva con la que el implementer diseña y el reviewer evalúa; no cambia quién hace qué (ver «Rol obligatorio»).
- `docs/stack.md` recoge las reglas específicas del stack y del proyecto que fija el humano. Lo específico prevalece sobre lo general: `stack.md` > `architecture.md` > `conventions.md`. Si `stack.md` contradice a `architecture.md`, prevalece `stack.md` para ese caso y se menciona en el informe. Si está vacío, no hay reglas adicionales (no se inventan).
- `docs/architecture-base.md` describe el proyecto existente: qué hay, dónde y cómo se usa.
- `docs/conventions.md` documenta lo observado en el código existente; vale para tocar archivos existentes y donde `docs/architecture.md` no diga nada.
- Si chocan, se resuelve con los criterios del propio `docs/architecture.md` (secciones «Plantilla institucional» y «Compatibilidad con el framework»); si no basta, se pregunta al humano.
- «Plantilla institucional», en esos documentos, es el proyecto base descrito en `docs/architecture-base.md`; si no hay plantilla, léase «código existente».

## Protocolo de arranque
Leer este mapa, el backlog y `progress/current.md`. **No ejecutar pruebas al arrancar.**

## Mapa
| Archivo | Qué contiene | Cuándo leerlo |
|---|---|---|
| `backlog.json` | Unidades de trabajo con estado | Siempre, al empezar |
| `progress/current.md` | Estado de la sesión activa | Siempre, al empezar |
| `progress/history.md` | Bitácora de sesiones anteriores | Si necesitas contexto histórico |
| `docs/architecture.md` | Reglas de arquitectura para todo lo nuevo (documento del humano, intacto) | Antes de diseñar o implementar |
| `docs/stack.md` | Reglas de stack y específicas del proyecto (documento del humano) | Antes de diseñar o implementar |
| `.claude/skills/conventional-commit/SKILL.md` | Estándar de commits (documento del humano, intacto) | Cada vez que se haga un commit |
| `docs/architecture-base.md` | Mapa del proyecto existente: stack, capas, BD, módulos, componentes reutilizables | Antes de diseñar o implementar |
| `docs/DescribeProject.md` | Procedimiento de descubrimiento (documento del humano, intacto) | Solo en el bootstrap o su actualización |
| `docs/conventions.md` | Estilo, nombres, tests, errores | Antes de escribir código |
| `docs/verification.md` | Niveles, política de ejecución, aislamiento | Antes de verificar |
| `CHECKPOINTS.md` | Criterios objetivos de estado final | Al revisar |
| `.claude/agents/` | Roles: leader, implementer, reviewer, explorer | Si orquestas |
| [POR ADAPTAR: documentación del proyecto que merezca enlace] | | |

## Commit al terminar cada ejecución
**Identificador de commits de IA:** `[IA change]` (se define aquí; para cambiarlo, se cambia aquí).

- Al terminar una ejecución en la que se cambiaron archivos, el **líder** hace un commit con ese identificador, como último paso del cierre. El humano ya lo autorizó: este commit no pide confirmación.
- Formato: Conventional Commits según `.claude/skills/conventional-commit/SKILL.md` (tipo, ámbito y descripción inferidos del diff, en español), con el identificador al final de la primera línea. Ejemplo: `feat(compras): añade registro de orden de compra [IA change]`. Cuerpo: la unidad y su estado, el valor de `verificacion` y la ruta del informe de revisión.
- Solo los archivos que tocó esta ejecución. Al arrancar se anota `git status --porcelain` en `progress/current.md`: los cambios previos del humano no se incluyen, y si la ejecución tocó un archivo que ya los tenía, se pregunta antes.
- Si la ejecución cubrió varias unidades independientes: un commit por unidad, todos con el identificador.
- Sin cambios o sin repositorio git: no hay commit (si no hay git, se avisa).
- Nunca `git push`, `git commit --amend` ni `--no-verify`. Si el commit falla, se muestra el error y se detiene.
- Que las pruebas no se hayan ejecutado no impide el commit: queda dicho en el cuerpo.
- Solo el líder hace commit; implementer, reviewer y explorer no.
- Cuando el humano pide un commit expresamente («haz un commit»), se usa la skill con su flujo completo, incluida la confirmación.

## Cierre de sesión
Campo `verificacion` de cada unidad cerrada reflejando lo realmente ejecutado; estado correcto en el backlog; resumen de `progress/current.md` movido al final de `progress/history.md`; `current.md` vaciado a su plantilla; repo limpio (sin temporales ni restos de depuración según `docs/conventions.md`); y, como último paso, el commit de IA.

## Anti teléfono descompuesto
Los subagentes escriben su resultado en `progress/` y devuelven **una línea** con la referencia al archivo.

## Cuándo NO aplica el rol
- Preguntas de lectura o exploración: responde directamente.
- Cambios fuera de las rutas protegidas.

## Mantenimiento
Si el agente tuvo que adivinar el mismo dato dos veces, o el revisor rechaza por una regla ambigua, se corrige `docs/` y se anota en `progress/history.md`.
