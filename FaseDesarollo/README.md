## Parte 1: ejecución del bootstrap (una vez por repo)

```
«Ejecuta BOOTSTRAP.md»
├── Fase 1  Descubrimiento (solo lectura) → perfil del proyecto en el chat
├── Fase 2  Decisiones autónomas, cada una marcada [decisión del modelo]
├── Fase 3  Generación de archivos
└── Fase 4  Validación y entrega (sin ejecutar pruebas, sin commit)
```

| Fase | Qué hace | Qué sale | Tu intervención |
|---|---|---|---|
| **1. Descubrimiento** | Lee manifiestos, CI, README, estructura y muestras de código. Lee la configuración de conexión solo para identificar el destino, sin credenciales. | Perfil con `Dato \| Valor \| Evidencia \| Confianza` | Ninguna |
| **Gate de aislamiento (§3.1)** | Se aplica en las fases 1 y 4. Por cada comando de verificación comprueba, con archivo y línea, que el destino es distinto de desarrollo y producción. Considera la precedencia de variables y si la preparación de pruebas es destructiva. | Veredicto: `AISLADO`, `NO AISLADO` o `NO VERIFICADO` | Si no hay aislamiento probado, eliges: corrijo la config, lo ejecuto yo, o declaro el destino desechable |
| **2. Decisiones** | Elige backlog, comandos de verificación y el patrón de ejecución dirigida. | Lista de decisiones revertibles | Máximo 3 preguntas de una línea, solo si algo bloquea |
| **3. Generación** | Crea `AGENTS.md`, `CHECKPOINTS.md`, backlog, 4 agentes (leader, implementer, reviewer, explorer), `docs/` (architecture, conventions, verification) y `progress/` (current, history). Cada dato lleva su origen o `POR CONFIRMAR`. | Archivos del harness | Ninguna |
| **4. Validación** | Clasifica los comandos sin ejecutarlos. Comprueba consistencia. El reviewer audita C1 y C2 y escribe `progress/review_bootstrap.md`. | Informe final en el chat | Revisas `git diff`. El bootstrap no hace commit. |

Si ya hay un harness generado, entra en **modo actualización**: compara y propone un diff. Si es de una versión anterior sin el gate, aplica la §8 (modo parche), que no ejecuta nada.

## Parte 2: ciclo de trabajo diario

```
Tú: «implementa X»
└── leader (rol fijado por CLAUDE.md; no edita código)
    ├── Arranque: lee CLAUDE.md, backlog y progress/current.md. No ejecuta pruebas.
    ├── Descompone en una o varias unidades (de a una)
    ├── explorers en paralelo, solo si el área es desconocida → progress/explore_<tema>.md
    ├── implementer: código + pruebas escritas, sin ejecutarlas → progress/impl_<id>.md
    ├── reviewer: revisión estática contra docs/ y CHECKPOINTS → progress/review_<id>.md
    │      ├── APPROVED → el leader marca done y el campo verificacion
    │      └── CHANGES_REQUESTED → vuelve al implementer
    └── Cierre: resumen de current.md a history.md, current.md vaciado, repo limpio

Cuando TÚ lo pides: «corre las pruebas de lo implementado»
└── gate → alcance dirigido → confirmación si toca estado → ejecución → Registro de ejecuciones
```

**Reglas del ciclo**
- Una unidad `in_progress` a la vez.
- Los subagentes escriben en archivos y responden con una línea y la ruta.
- Nadie se autoaprueba: el implementer no marca `done` y el reviewer no edita código.
- `done` exige un `review_<id>.md` con `APPROVED`.
- El campo `verificacion` de cada unidad refleja lo realmente ejecutado: `no_ejecutada`, `dirigida_ok`, `completa_ok` o `fallida`.

**Verificación bajo demanda**
- Cuentan como petición frases como «corre las pruebas», «valida lo implementado» o «ejecuta los tests de X». «Implementa» y «cierra la unidad» no cuentan.
- Por defecto el alcance es dirigido. La suite completa solo si dices «suite completa» o «todas las pruebas».
- Si no puede acotar un subconjunto, te pregunta en vez de caer en la completa.
- Antes de un nivel lento te indica el tiempo observado, y cada ejecución queda registrada con fecha, alcance y duración.

## Parte 3: cómo encaja con una entrega del harness de planificación

1. Le das la `ENT-NNN` y pides implementar las historias en el orden indicado.
2. El leader trata cada historia como una unidad, de a una.
3. Al terminar, el informe de retorno que pegas en planificación sale de esa misma entrega.

## Qué decides tú

- Responder las preguntas bloqueantes de la fase 2.
- Elegir qué hacer cuando el gate no puede probar el aislamiento.
- Revisar `git diff` y hacer el commit.
- Pedir explícitamente las pruebas, y si son dirigidas o completas.
- Confirmar el primer comando que toque estado.

## Críticas

1. **El bucle `CHANGES_REQUESTED` no está definido.** Lo verifiqué leyendo el archivo: el reviewer devuelve ese veredicto, pero no hay un máximo de rondas ni dice qué hace el leader después. [Inferencia] Sin ese límite, el comportamiento queda a criterio del modelo y puede iterar de más o parar sin avisar. Conviene añadir un máximo de 2 rondas y luego `blocked`.
2. **El enlace con la entrega es informal.** El BOOTSTRAP no dice que `US-NNN` sea el id de la unidad ni que los `CA-NN` sean su `acceptance[]`, ni genera el informe de retorno. Eso depende de que el leader lea las instrucciones de la `ENT`. [Inferencia] Es el punto con más riesgo de improvisación; basta una línea en el BOOTSTRAP para cerrarlo.
3. **Sin hooks, todo es instrucción.** Como las barreras no se hacen cumplir por mecanismo, la confirmación humana antes del primer comando que toque estado es la protección real.
4. **`done` sin ejecutar pruebas es posible.** El campo `verificacion` lo hace visible, pero no lo evita. [Inferencia] Si pasan varias unidades sin ejecución, los fallos aparecerán juntos. Pide al menos una ejecución dirigida antes de integrar cada unidad.