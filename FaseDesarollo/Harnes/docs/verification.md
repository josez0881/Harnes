# Verificación

> Regla de oro: el agente no dice «funciona» sin haberlo ejecutado; si no se ejecutó, dice «no verificado». Se reportan solo comandos ejecutados y sus resultados observados.

## Niveles
| Nivel | Qué cubre | Comando exacto | Dónde se declara | Prerrequisitos | Tiempo observado |
|---|---|---|---|---|---|
| 1. Dirigida | Solo las pruebas que cubren la aceptación de la unidad | [POR ADAPTAR] | [POR ADAPTAR] | [POR ADAPTAR] | desconocido |
| 2. Completa | Suite entera; solo con petición expresa o si la unidad toca migraciones o fixtures de esquema | [POR ADAPTAR] | [POR ADAPTAR] | [POR ADAPTAR] | desconocido |
| 3. Integración / build | Si aplica | [POR ADAPTAR] | [POR ADAPTAR] | [POR ADAPTAR] | desconocido |
| 4. Extremo a extremo / smoke manual | Opcional | [POR ADAPTAR] | — | — | — |

Si falta un nivel, regístralo como brecha.

### Patrones de ejecución dirigida
- Un archivo: [POR ADAPTAR]
- Un nombre o filtro: [POR ADAPTAR]
- Una etiqueta o grupo: [POR ADAPTAR]

Si el runner no lo permite, regístralo aquí como brecha.

## Política de ejecución
- **Al arrancar:** no se ejecuta nada.
- **Dirigida (por defecto):** tras implementar, el implementer y el reviewer ejecutan solo las pruebas que cubren la aceptación, con el patrón documentado arriba y únicamente si el comando está marcado `AISLADO`.
- **Suite completa a petición:** solo si el humano dice «suite completa», «todas las pruebas» o equivalente. «Implementa», «termina» o «cierra la unidad» **no** cuentan. La petición vale para la acción en curso; solo es permanente si el humano lo dice. Antes de lanzarla se indica el tiempo observado.
- **Suite completa obligatoria por migraciones:** si la unidad añade o modifica migraciones o fixtures de esquema ([POR ADAPTAR: rutas reales, p. ej. `database/migrations/**`, `tests/Fixtures/**`; o «No aplica» si el proyecto no tiene]), el reviewer ejecuta además la suite completa antes de emitir veredicto. Un fallo nuevo respecto del último registro impide `APPROVED`. Motivo: un cambio de esquema puede romper pruebas lejanas que la verificación dirigida no cubre.
- **Fallos preexistentes:** se listan, no se corrigen dentro de otra unidad y se registran como unidad propia del backlog. Que no bloqueen la unidad actual requiere una excepción explícita registrada en su revisión; no hay excepción general a «verificación en verde».
- **Verificaciones obligatorias adicionales del proyecto:** [POR ADAPTAR: comprobaciones que las pruebas no cubren y que una unidad debe aportar como evidencia cuando aplique; p. ej. «si la unidad añade clases CSS de un framework de utilidades, ejecutar el build y comprobar que las clases están en el CSS generado». Solo con evidencia o decisión del humano; si no hay, «Ninguna»]
- Si no puedes determinar un subconjunto dirigido, no caigas en la completa: pregunta con opciones (completa / indicar archivo o filtro / no ejecutar).
- Si algo no se ejecutó, los informes dicen «no ejecutada», con el motivo, y dejan los comandos listos para pegar.
- Se aplica el Gate de aislamiento siempre, también a la verificación dirigida.
- Cada ejecución se anota en el *Registro de ejecuciones*.

## Aislamiento (Gate)
Solo los comandos `AISLADO` pueden ser ejecutados por los agentes, y el primero que toque estado requiere confirmación humana. Veredictos: `AISLADO` (evidencia de destino distinto de desarrollo y producción para todos los recursos con estado), `NO AISLADO` (hay evidencia de que apunta a desarrollo o producción), `NO VERIFICADO` (falta evidencia). Para los dos últimos, escribe qué falta para poder clasificarlos como `AISLADO`, sin aplicarlo tú; solo se ejecutan con autorización expresa del humano, que se registra.

| Comando | Nivel | Recursos con estado que toca | Evidencia de destino distinto (archivo:línea) | Veredicto | Confirmación humana |
|---|---|---|---|---|---|
| [POR ADAPTAR] | | | | | |

Incluye también, si existen, las migraciones y seeds contra la BD de desarrollo (`NO AISLADO`) y el navegador contra el entorno de desarrollo (`NO AISLADO`; ver «Pruebas de navegador» en `CLAUDE.md`).

### Gates específicos del proyecto
[POR ADAPTAR: comprobaciones obligatorias antes de comandos peligrosos propios del stack, con su motivo y su fuente; p. ej. una consulta de solo lectura antes de migrar una BD que no es la de pruebas, o la advertencia de que un modo «simulación» (`--pretend`, `--dry-run`) no prueba que la ejecución real sea segura. Si no hay, «Ninguno»]

## Línea base
[POR ADAPTAR: estado conocido de la suite antes de empezar a trabajar (fecha, comando, resultado, duración) o «no medida: <motivo>». Se actualiza cuando el humano pide la suite completa o una unidad la exige]

| Fecha | Comando | Resultado | Duración |
|---|---|---|---|

## Registro de ejecuciones
no ejecutado: sin ejecuciones todavía

| Fecha | Unidad | Alcance | Comando | Resultado | Duración |
|---|---|---|---|---|---|

## Anti-patrones
- Afirmar que algo funciona sin la salida de un comando ejecutado.
- Pruebas que solo comprueban que no hay excepción, como sustituto de criterios de comportamiento.
- Un `assertDontSee` (o equivalente) sobre un texto que ya no existe: pasa trivialmente y no prueba nada.
- Marcar `done` sin la verificación aplicable.
- Ejecutar un comando sin veredicto `AISLADO` en la tabla de aislamiento.
- [POR ADAPTAR: anti-patrones propios del proyecto, solo con evidencia]
