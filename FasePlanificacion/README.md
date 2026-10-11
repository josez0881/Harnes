# Harnes Planifiacción

## Vista general

```
CADA SESIÓN (Documentador)
├── Arranque: lee progress/current.md → retoma "Próximo paso" o abre sesión nueva
│
├── A. Capability      cuestionario → docs/00_capabilities.md, 04_, 05_
├── B. Épicas          desglose     → docs/epics/EPIC-NNN-*/00-EPIC-NNN.md
├── C. Historias       una por archivo → 01-US-NNN-*.md  (Borrador → En refinamiento)
│
├── D. Revisión DoR    SESIÓN NUEVA, Revisor → "Lista para desarrollo" o "En refinamiento"
│        ▲                                   │
│        └──── hallazgos como OBS ◄──────────┘   (bucle C ↔ D hasta que quede lista)
│
├── E. Cierre de épica → confirmas → apruebas el orden → entregas/ENT-NNN-*.md
│                                      → SESIÓN NUEVA: Revisor valida la entrega (E1–E6)
│
├── Cierre: OBS de lo abierto → entrada en history.md → current.md vaciado → commit
│
└──▶ Tú copias la ENT al harness de implementación (otro repo)
        │
        ▼
     F. Retorno: pegas su informe → estados, criterios y OBS actualizados
        └── si hay ambigüedad: la historia vuelve a "En refinamiento" → C/D → nueva ENT
```

## Fase por fase

| Fase | Quién | Qué ocurre | Sale con |
|---|---|---|---|
| **Arranque** | Documentador | Lee `progress/current.md`. Si hay sesión en curso, la retoma y te confirma. Lee `docs/` antes de escribir y actualiza, no regenera. | Contexto cargado |
| **A. Capability** | Documentador | Te entrevista con preguntas de una línea con opciones, máximo 3 por ronda. Tras cada ronda anota en `current.md` lo confirmado y lo pendiente, antes de redactar. | Capacidades, roles, reglas globales e integraciones. Lo que no sabes queda como `OBS`. |
| **B. Épicas** | Documentador | Desglosa en módulos lógicos. Cada épica lleva su tabla de historias. | `00-EPIC-NNN.md` |
| **C. Historias** | Documentador | Una historia por archivo, con contexto heredado, alcance, reglas, datos y criterios `CA-NN` en Dado/Cuando/Entonces. Al cerrar la pasada registra como `OBS` lo débil o ambiguo. | Historias en `En refinamiento` |
| **D. Revisión DoR** | Revisor | En sesión distinta, lee solo los documentos. Evalúa D1 a D7, incluida la prueba del desarrollador ciego. Registra hallazgos como `OBS` y concede o no `Lista para desarrollo`. | Veredicto y estado de la historia |
| **E. Cierre y entrega** | Documentador y Revisor | Con las historias listas, sin `OBS` bloqueantes y tu confirmación, propone el orden con el motivo de cada lugar. Tú lo apruebas. Genera la `ENT` y marca las historias como `Entregada`. Luego el Revisor valida la entrega. | `entregas/ENT-NNN-*.md` |
| **Implementación** | Tú | Das la `ENT` al otro harness: «Implementa las historias de este documento en el orden indicado». | Informe de retorno |
| **F. Retorno** | Documentador | Pegas el informe y dices «registra el retorno de ENT-NNN». Actualiza estados y criterios. Las dudas pasan a `OBS` con origen `Desarrollo`. Un supuesto del implementador no cambia un requisito hasta que lo confirmes. | Estados al día |

**Ciclo de estados de una historia:** `Borrador` → `En refinamiento` → `Lista para desarrollo` → `Entregada` → `En desarrollo` → `Implementada` → `Validada`. Solo el Revisor concede `Lista para desarrollo`. Solo tú confirmas `Validada`.

## Qué decides tú

- Aprobar cada fase antes de pasar a la siguiente.
- Confirmar que la épica está lista.
- Aprobar el orden de implementación.
- Abrir la sesión nueva para las revisiones.
- Copiar la entrega y pegar el retorno.
- Confirmar `Validada`.
- Confirmar cada commit.

## Cambios después de la entrega

Si cambia una historia ya entregada:
1. Se anota en su Registro de cambios y vuelve a `En refinamiento`.
2. Pasa otra vez por la revisión DoR.
3. Se genera una `ENT` nueva y la anterior queda `Reemplazada`.

## Críticas

1. **El ciclo tiene dos pasos manuales:** copiar la entrega y pegar el retorno. [Inferencia] Si omites el retorno, los estados de la planificación se desactualizan sin que nada lo avise.
2. **Las puertas son instrucciones, no mecanismos.** La independencia del Revisor depende de que abras una sesión nueva. [Inferencia] Si lo haces en la misma sesión que redactó, pierdes buena parte del valor de esa revisión.
3. **No hay camino corto.** Un cambio pequeño en una historia pasa por revisión DoR y por una `ENT` nueva. Si en la práctica te resulta pesado, conviene definir un flujo ligero para cambios menores.
4. **El contrato con el implementador vive solo en la entrega.** Como no tocamos el BOOTSTRAP de desarrollo, que lo siga depende de que ese harness lea las instrucciones y el formato de retorno. Pruébalo primero con una entrega pequeña.