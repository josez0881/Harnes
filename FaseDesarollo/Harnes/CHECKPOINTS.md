# CHECKPOINTS — Evaluación del estado final

> Se evalúa el destino, no el camino. El reviewer marca cada casilla; si queda alguna vacía, no hay cierre.

## C1 — Harness completo
- [ ] Existen `CLAUDE.md`, `CHECKPOINTS.md`, el backlog, `.claude/agents/*`, `.claude/hooks/proteger-ramas.py`, `.claude/settings.json`, `docs/{architecture,architecture-base,stack,conventions,verification}.md`, `.claude/skills/conventional-commit/SKILL.md` y `progress/{current,history}.md`.
- [ ] Cada comando de verificación está clasificado en `docs/verification.md` (`AISLADO` / `NO AISLADO` / `NO VERIFICADO`); lo que se ejecutó fue `AISLADO` (o `NO AISLADO` con autorización expresa del humano registrada); lo demás consta como `no ejecutado` con su motivo (suite completa sin petición expresa ni migraciones, o aislamiento).

## C2 — Estado coherente
- [ ] Como máximo una unidad `in_progress`.
- [ ] Toda unidad `done` tiene `review_<id>.md` `APPROVED` y su campo `verificacion` refleja lo realmente ejecutado.
- [ ] `progress/current.md` está vacío o describe la sesión activa, e incluye el plan del implementer de la unidad en curso.

## C3 — El código respeta la arquitectura
- [ ] Cumple las reglas de `docs/stack.md`, si las hay.
- [ ] Cumple `docs/architecture.md` (estructura orientada al negocio, sin capas innecesarias, reglas de base de datos y seguridad aplicables).
- [ ] Reutiliza lo que `docs/architecture-base.md` indica que ya existe; no duplica funcionalidad del proyecto base.
- [ ] Cumple las decisiones del humano de `docs/conventions.md` (cada una dice qué es un hallazgo al revisar).
- [ ] El informe del implementer documenta dominio, componentes reutilizados y elementos nuevos justificados.
- [ ] Sin dependencias nuevas sin aprobación.
- [ ] Sin restos de depuración según `docs/conventions.md`.

## C4 — Verificación honesta
- [ ] El código cambiado tiene pruebas escritas o actualizadas según `docs/verification.md`.
- [ ] La verificación dirigida se ejecutó y está en verde; si la unidad tocó migraciones o fixtures de esquema, también la suite completa, sin fallos nuevos respecto del último registro.
- [ ] Se cumplieron las verificaciones obligatorias adicionales del proyecto que apliquen (`docs/verification.md`).
- [ ] El informe declara qué se ejecutó (comando y resultado) y qué no, y no afirma resultados que no se obtuvieron.
- [ ] Los fallos preexistentes se listan y no se corrigen dentro de la unidad.

## C5 — Sesión cerrada
- [ ] Repo limpio, entrada en `progress/history.md`, estado correcto en el backlog.
- [ ] La ejecución con cambios terminó en un commit con el identificador de IA, solo con los archivos de esa ejecución, en formato Conventional Commits, fuera de las ramas de integración y sin push.

## C6 — Sin efectos colaterales ni costos no pedidos
- [ ] Ningún comando ejecutado en la sesión tenía veredicto distinto de `AISLADO`, salvo autorización expresa del humano registrada en el informe.
- [ ] Solo se ejecutó verificación dirigida, salvo que el humano pidiera expresamente la suite completa (con evidencia de esa petición en el informe) o que la unidad tocara migraciones o fixtures de esquema.
- [ ] Ninguna escritura ni commit en una rama de integración; ningún tag creado ni movido por el agente.
- [ ] Los informes no muestran señales de datos o servicios de desarrollo o producción alterados.

## C7 — Específicos del proyecto
[POR ADAPTAR: solo checkpoints con evidencia en el repo (p. ej. una política documentada de migraciones o de seguridad), cada uno con su fuente. Si no hay, escribe «Ninguno»]

## Aceptación integrada pendiente
Si una unidad cumple todo lo verificable de forma aislada y algún criterio de aceptación depende de otra unidad aún no implementada, el reviewer puede emitir `APPROVED` siempre que ese criterio esté documentado como no verificado y no se simule. El líder la cierra como `blocked` con `verificacion: dirigida_ok` (nunca `done`) y anota la dependencia en `notes`.
- Se aplica igual a una **limitación de diseño** que solo puede resolverse con otra unidad aún no implementada (p. ej. un identificador que todavía no existe), siempre que esté documentada en el informe, tenga dueño (la unidad que la resuelve) y no se simule. Esa unidad debe incluirla en su verificación.
- Una dependencia **externa** (otro sistema, una integración) solo se acepta con este criterio si existe en el backlog una unidad explícita que la reúna; la nota de la unidad bloqueada debe referenciarla.
