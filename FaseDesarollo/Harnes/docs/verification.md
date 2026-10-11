# Verificación

> Regla de oro: el agente no dice «funciona» sin haberlo ejecutado; si no se ejecutó, dice «no verificado».

## Niveles
| Nivel | Qué cubre | Comando exacto | Dónde se declara | Prerrequisitos | Tiempo observado |
|---|---|---|---|---|---|
| 1. Dirigida | Solo las pruebas relacionadas con lo cambiado | [POR ADAPTAR] | [POR ADAPTAR] | [POR ADAPTAR] | desconocido |
| 2. Completa | Suite entera; solo si el humano la pide expresamente | [POR ADAPTAR] | [POR ADAPTAR] | [POR ADAPTAR] | desconocido |
| 3. Integración / extremo a extremo | Si aplica | [POR ADAPTAR] | [POR ADAPTAR] | [POR ADAPTAR] | desconocido |
| 4. Smoke manual | Opcional | [POR ADAPTAR] | — | — | — |

Si falta un nivel, regístralo como brecha.

### Patrones de ejecución dirigida
- Un archivo: [POR ADAPTAR]
- Un nombre o filtro: [POR ADAPTAR]
- Una etiqueta o grupo: [POR ADAPTAR]

Si el runner no lo permite, regístralo aquí como brecha.

## Política de ejecución (bajo demanda)
- Por defecto no se ejecuta nada. Implementar una unidad significa escribir o actualizar código y pruebas, sin correrlas.
- Cuenta como petición explícita lo que el humano dice con ese fin («corre las pruebas», «valida lo implementado», «ejecuta los tests de X», «verifica que funciona»). **No** cuentan «implementa», «termina la tarea» ni «cierra la unidad». La petición vale para la acción en curso; solo es permanente si el humano lo dice.
- Alcance: **dirigido** por defecto (pruebas relacionadas con lo tocado, con el patrón documentado arriba). Suite **completa** solo si el humano dice «suite completa», «todas las pruebas» o equivalente. Si no puedes determinar un subconjunto dirigido, no caigas en la completa: pregunta con opciones (completa / indicar archivo o filtro / no ejecutar).
- Antes de ejecutar un nivel con tiempo observado largo, indica ese tiempo.
- Se aplica el Gate de aislamiento incluso bajo demanda.
- Si no se ejecutó nada, los informes dicen «Verificación: no ejecutada» y proponen los comandos dirigidos listos para pegar.
- Cada ejecución se anota en el *Registro de ejecuciones*.

## Aislamiento
Solo los comandos `AISLADO` pueden ser ejecutados por los agentes, y el primero que toque estado requiere confirmación humana. Veredictos: `AISLADO` (evidencia de destino distinto de desarrollo y producción para todos los recursos con estado), `NO AISLADO` (hay evidencia de que apunta a desarrollo o producción), `NO VERIFICADO` (falta evidencia). Para los dos últimos, escribe qué falta para poder clasificarlos como `AISLADO`, sin aplicarlo tú.

| Comando | Nivel | Recursos con estado que toca | Evidencia de destino distinto (archivo:línea) | Veredicto | Confirmación humana |
|---|---|---|---|---|---|
| [POR ADAPTAR] | | | | | |

## Registro de ejecuciones
no ejecutado: política bajo demanda

| Fecha | Alcance | Comando | Resultado | Duración |
|---|---|---|---|---|

## Anti-patrones
- Afirmar que algo funciona sin evidencia ejecutable.
- Pruebas que solo comprueban que no hay excepción.
- Declarar «funciona» sin haber ejecutado.
- [POR ADAPTAR: anti-patrones propios del proyecto, solo con evidencia]
