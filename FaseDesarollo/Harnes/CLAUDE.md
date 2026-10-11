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

Sí puede editar: `docs/`, `.claude/`, `CHECKPOINTS.md`, `progress/`, el backlog y este archivo.

## Reglas duras
1. Una unidad de trabajo a la vez.
2. No marcar `done` sin un `progress/review_<id>.md` con veredicto `APPROVED`, y dejar siempre en el backlog el campo `verificacion` con lo realmente ejecutado.
3. No ejecutar pruebas salvo petición explícita del humano (*Política de ejecución* de `docs/verification.md`).
4. No ejecutar migraciones, seeds, reinicios de base de datos ni pruebas cuyo comando no esté marcado `AISLADO` en `docs/verification.md`; ante la duda, preguntar al humano.
5. Ante un fallo inesperado de herramienta, sin workaround: documentar el bloqueo en `progress/current.md` y parar.
6. No afirmar que algo funciona si no se ejecutó: decir «no verificado».

## Protocolo de arranque
Leer este mapa, el backlog y `progress/current.md`. **No ejecutar pruebas al arrancar.**

## Mapa
| Archivo | Qué contiene | Cuándo leerlo |
|---|---|---|
| `backlog.json` | Unidades de trabajo con estado | Siempre, al empezar |
| `progress/current.md` | Estado de la sesión activa | Siempre, al empezar |
| `progress/history.md` | Bitácora de sesiones anteriores | Si necesitas contexto histórico |
| `docs/architecture.md` | Capas, dependencias, qué NO hacer | Antes de implementar |
| `docs/conventions.md` | Estilo, nombres, tests, errores | Antes de escribir código |
| `docs/verification.md` | Niveles, política de ejecución, aislamiento | Antes de verificar |
| `CHECKPOINTS.md` | Criterios objetivos de estado final | Al revisar |
| `.claude/agents/` | Roles: leader, implementer, reviewer, explorer | Si orquestas |
| [POR ADAPTAR: documentación del proyecto que merezca enlace] | | |

## Cierre de sesión
Campo `verificacion` de cada unidad cerrada reflejando lo realmente ejecutado; estado correcto en el backlog; resumen de `progress/current.md` movido al final de `progress/history.md`; `current.md` vaciado a su plantilla; repo limpio (sin temporales ni restos de depuración según `docs/conventions.md`).

## Anti teléfono descompuesto
Los subagentes escriben su resultado en `progress/` y devuelven **una línea** con la referencia al archivo.

## Cuándo NO aplica el rol
- Preguntas de lectura o exploración: responde directamente.
- Cambios fuera de las rutas protegidas.

## Mantenimiento
Si el agente tuvo que adivinar el mismo dato dos veces, o el revisor rechaza por una regla ambigua, se corrige `docs/` y se anota en `progress/history.md`.
