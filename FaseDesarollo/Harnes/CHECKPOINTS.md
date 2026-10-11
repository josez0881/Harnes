# CHECKPOINTS — Evaluación del estado final

> Se evalúa el destino, no el camino. El reviewer marca cada casilla; si queda alguna vacía, no hay cierre.

## C1 — Harness completo
- [ ] Existen `CLAUDE.md`, `CHECKPOINTS.md`, el backlog, `.claude/agents/*`, `docs/{architecture,conventions,verification}.md` y `progress/{current,history}.md`.
- [ ] Cada comando de verificación está clasificado en `docs/verification.md` (`AISLADO` / `NO AISLADO` / `NO VERIFICADO`); lo que se ejecutó fue `AISLADO` y con confirmación humana; lo demás consta como `no ejecutado` con su motivo (política bajo demanda o aislamiento).

## C2 — Estado coherente
- [ ] Como máximo una unidad `in_progress`.
- [ ] Toda unidad `done` tiene `review_<id>.md` `APPROVED` y su campo `verificacion` refleja lo realmente ejecutado.
- [ ] `progress/current.md` está vacío o describe la sesión activa.

## C3 — El código respeta la arquitectura
- [ ] Cumple `docs/architecture.md`.
- [ ] Sin dependencias nuevas sin aprobación.
- [ ] Sin restos de depuración según `docs/conventions.md`.

## C4 — Verificación honesta
- [ ] El código cambiado tiene pruebas escritas o actualizadas según `docs/verification.md`.
- [ ] El informe declara qué se ejecutó (o `no ejecutada`) y no afirma resultados que no se obtuvieron.
- [ ] Si se ejecutó algo, hay resultados concretos.

## C5 — Sesión cerrada
- [ ] Repo limpio, entrada en `progress/history.md`, estado correcto en el backlog.

## C6 — Sin efectos colaterales ni costos no pedidos
- [ ] Ningún comando ejecutado en la sesión tenía veredicto distinto de `AISLADO`.
- [ ] No se ejecutó ninguna prueba sin petición explícita del humano.
- [ ] Los informes no muestran señales de datos o servicios de desarrollo o producción alterados.

## C7 — Específicos del proyecto
[POR ADAPTAR: solo checkpoints con evidencia en el repo (p. ej. una política documentada de migraciones o de seguridad), cada uno con su fuente. Si no hay, escribe «Ninguno»]
