# Plantillas de artefactos

> Copia la plantilla que corresponda y rellénala. Reglas comunes:
> - Ningún marcador `<...>` puede quedar sin resolver: se reemplaza por contenido, por `Pendiente` o se borra la fila/sección si no aplica.
> - Texto sin etiqueta = confirmado y con fuente. Lo demás lleva `Pendiente`, `[Inferencia]` o `[No verificado]`.
> - **Enlaces entre archivos de `docs/`:** son relativos al archivo que los contiene (como los de los ejemplos de esta plantilla) y deben resolver. Antes de dar un enlace por bueno, comprueba que el destino existe y que la ancla (`#...`) coincide con un encabezado real. No conviertas a rutas desde la raíz enlaces relativos que ya funcionan.
> - **Rutas escritas en texto** (no como enlace), en `OBS`, informes y mensajes: desde la raíz del repositorio (`docs/...`).
> - `NNN` = número del ID con tres dígitos (`US-003` → `01-US-003-<slug>.md`). `<slug>` = minúsculas, sin tildes, con guiones.

---

## 1. `docs/00_capabilities.md`

```markdown
# Capabilities

## Propósito
<para qué existe este documento>

## Fuente
- Reunión / documento: <nombre> · Fecha: <AAAA-MM-DD> · Participantes: <nombres> · Sistema o módulo afectado: <...>

## Capacidades
| ID | Capacidad | Descripción breve | Prioridad | Estado | Notas |
|---|---|---|---|---|---|
| CAP-001 | <...> | <...> | Alta/Media/Baja | Pendiente de validar / Confirmado / Descartado | <...> |

## Roles del negocio
| ID | Rol | Descripción | Notas |
|---|---|---|---|
| ROL-001 | <...> | <...> | <...> |

## Necesidades del negocio
## Problemas o limitaciones actuales
## Alcance inicial
- **Incluido:**
- **Fuera de alcance:**
## Riesgos, dudas o dependencias
## Decisiones tomadas
| Decisión | Fecha | Quién decidió | Fuente |
|---|---|---|---|
```

## 2. `docs/04_reglas_globales.md`

```markdown
# Reglas globales
## Propósito
Reglas del sistema que aplican a más de una épica. Son distintas de las reglas de negocio (`RN-`), que viven en cada historia.
| ID | Regla | Descripción | Épicas/módulos afectados | Estado | Notas |
|---|---|---|---|---|---|
| REG-001 | <...> | <...> | EPIC-001, EPIC-002 | Pendiente de validar / Confirmado | <...> |
```

## 3. `docs/05_integraciones.md`

```markdown
# Integraciones
## Propósito
Sistemas externos con los que el sistema se relaciona. Transversal a las épicas.
| ID | Sistema externo | Descripción (qué dato/acción, dirección, frecuencia) | Épicas/módulos afectados | Estado | Notas |
|---|---|---|---|---|---|
| INT-001 | <...> | <...> | <...> | Pendiente de validar / Confirmado | <...> |
```

## 4. `docs/epics/EPIC-NNN-<slug>/00-EPIC-NNN.md`

```markdown
# EPIC-NNN — <nombre>

- **Capacidad relacionada:** [CAP-XXX](../../00_capabilities.md)
- **Estado:** Borrador / En refinamiento / Lista para desarrollo / En desarrollo / Completada / Descartada
- **Prioridad:** Alta / Media / Baja

## Objetivo
## Descripción
## Valor esperado
## Criterios de aceptación de alto nivel
-

## Historias relacionadas
| ID | Historia (resumen) | Prioridad | Estado | Depende de | Archivo |
|---|---|---|---|---|---|
| US-001 | <...> | Alta | Borrador | — | [01-US-001-<slug>.md](01-US-001-<slug>.md) |

## Orden de implementación
> Se completa en la Fase E, cuando la épica se confirma como lista. Lo propone el Documentador y lo aprueba el usuario.
| Orden | Historia | Depende de | Motivo del lugar |
|---|---|---|---|
| 1 | US-001 | — | <...> |

## Entregas
| ID | Alcance | Fecha | Estado |
|---|---|---|---|
| [ENT-001](../../../entregas/ENT-001-EPIC-NNN-<slug>.md) | Épica completa / selección | <AAAA-MM-DD> | Generada / Retornada / Reemplazada |

## Dependencias o restricciones
## Notas
```

## 5. `docs/epics/EPIC-NNN-<slug>/01-US-NNN-<slug>.md`  (contrato con el harness de desarrollo)

```markdown
# US-NNN — <título>

| Campo | Valor |
|---|---|
| Épica | [EPIC-NNN](00-EPIC-NNN.md) |
| Capacidad | [CAP-XXX](../../00_capabilities.md) |
| Estado | Borrador / En refinamiento / Lista para desarrollo / Entregada / En desarrollo / Implementada / Validada / Bloqueada / Descartada |
| Prioridad | Alta / Media / Baja |
| Responsable | <nombre o Pendiente> |
| Estimación | <solo si fue dada por alguien; si no, Pendiente> |
| Fuente | <reunión/documento, fecha> |

## Propósito
<una o dos frases>

## Historia de usuario
Como **[ROL-XXX · <rol>]**, quiero **<acción>**, para **<beneficio>**.

## Contexto heredado (lectura obligatoria para el desarrollo)
- Capacidad: [CAP-XXX](../../00_capabilities.md)
- Reglas globales aplicables: [REG-XXX](../../04_reglas_globales.md)
- Integraciones: [INT-XXX](../../05_integraciones.md)
- Historias previas de las que depende: [US-XXX](01-US-XXX-<slug>.md)
- Otros documentos que contienen requisitos confirmados que esta historia usa (épica, `OBS` resuelta, entrevista, datos tabulares/CSV): <enlace + qué hecho concreto se toma de allí>
> Si un documento no es necesario para esta historia, no lo enlaces. Si lo es y falta, la historia no está lista.
> Si un hecho confirmado vive solo en un documento que no es CAP/ROL/REG/INT/US (p. ej. una épica o una `OBS`), indícalo en la última fila: al generar la entrega ese hecho se copia al paquete (ver Contexto adicional y Anexos).

## Alcance
- **Incluye:** <...>
- **No incluye (fuera de esta historia):** <...>

## Flujo
- **Principal:** 1. ... 2. ...
- **Alternos:** <...>
- **Excepciones/errores:** <...>

## Reglas de negocio
| ID | Regla | Fuente |
|---|---|---|
| RN-001 | <...> | <reunión/fecha o documento> |

## Datos requeridos
| Dato | Descripción de negocio | Obligatorio | Formato / validación | Origen |
|---|---|---|---|---|
| <...> | <...> | Sí/No | <ej. 8 dígitos numéricos> | <usuario / sistema X> |
> Solo datos de negocio. El diseño de tablas, campos técnicos o endpoints corresponde al desarrollo.

## Criterios de aceptación / Definition of Done
| ID | Dado | Cuando | Entonces | Validación |
|---|---|---|---|---|
| CA-01 | <contexto con datos concretos> | <acción> | <resultado observable> | Pendiente |
| CA-02 (error) | ... | ... | ... | Pendiente |
| CA-03 (permisos) | ... | ... | ... | Pendiente |
> Se citan como `US-NNN.CA-01`. Validación: `Pendiente` / `Validado manualmente` / `Validado con test automatizado`.

## Requisitos no funcionales (solo si aplican)
Permisos, auditoría, volumen, rendimiento percibido, trazabilidad, retención de datos.

## Dependencias
- Historias: <...> · Integraciones: <...> · Decisiones: <...>

## Decisiones pendientes que bloquean
| OBS | Qué hay que decidir | Quién decide | Bloquea |
|---|---|---|---|
| [OBS-XXX](99-OBS-Observaciones.md) | <...> | <...> | Esta historia |
> Debe estar vacío para pasar a `Lista para desarrollo`.

## Notas de validación

## Definition of Ready (la completa solo el Revisor de requerimientos)
- [ ] D1 Estructura completa, sin marcadores ni campos vacíos
- [ ] D2 Trazabilidad: épica, capacidad, rol, REG/INT existen y se enlazan de vuelta
- [ ] D3 Criterios verificables y con cobertura (camino feliz, error y permisos si hay rol restringido)
- [ ] D4 Sin `Pendiente`/`[No verificado]` en campos obligatorios ni OBS bloqueantes abiertas
- [ ] D5 Sin solución técnica impuesta sin confirmar
- [ ] D6 Tamaño razonable y dependencias resueltas
- [ ] D7 Prueba del desarrollador ciego superada
- **Revisión:** <fecha> · <LISTA / CAMBIOS REQUERIDOS>

## Registro de cambios
| Fecha | Cambio | Motivo | Estado previo → nuevo |
|---|---|---|---|
```

## 6. `docs/epics/EPIC-NNN-<slug>/98-FUT-DeudasTecnicas.md`

```markdown
# Deuda técnica — EPIC-NNN
| ID | Tema | Descripción | Prioridad | Estado | Notas |
|---|---|---|---|---|---|
| FUT-001 | <...> | <...> | Media | Pendiente / Planificada / Hecha / Descartada | <...> |
```

## 7. `docs/epics/EPIC-NNN-<slug>/99-OBS-Observaciones.md`

```markdown
# Observaciones — EPIC-NNN
| ID | Tipo | Observación | Origen | Bloquea | Resolución o nota | Estado |
|---|---|---|---|---|---|---|
| OBS-001 | Decisión / Ambigüedad / Riesgo / Criterio débil | <...> | Reunión <fecha> / Documentador / Revisión DoR / Desarrollo | US-XXX o — | <recomendación concreta> | Abierta / Resuelta / Descartada |
```

## 8. `docs/98_tareas_internas_y_deuda_tecnica.md` (índice)

```markdown
# Tareas internas y deuda técnica (ÍNDICE)
## Propósito
Índice. El detalle vive en cada épica; aquí solo hay detalle de ítems transversales.
| ID | Épica de origen o "Transversal" | Resumen (una línea) | Estado | Detalle |
|---|---|---|---|---|
## Detalle de ítems transversales
```

## 9. `docs/99_observaciones_pendientes.md` (índice)

```markdown
# Observaciones pendientes (ÍNDICE)
## Propósito
Índice. El detalle vive en cada épica; aquí solo hay detalle de ítems transversales.
| ID | Épica de origen o "Transversal" | Tipo | Resumen (una línea) | Bloquea | Estado | Detalle |
|---|---|---|---|---|---|---|
## Detalle de ítems transversales
```

---

## 10. `progress/`

### `current.md`
```markdown
# Sesión actual (planificación)
> Estado vivo. Se actualiza mientras se trabaja y se vacía al cerrar la sesión (su resumen pasa a `history.md`).
> No es fuente de verdad: los requisitos viven solo en `docs/`.

- **Fase:** A Capability / B Épicas / C Historias / D Preparación / Actualización / —
- **Foco:** <CAP / EPIC / US en trabajo, o —>
- **Inicio:** <AAAA-MM-DD>
- **Fuente de la sesión:** <reunión, documento o conversación + fecha>

## Confirmado en esta sesión
| Tema | Lo confirmado (lo más cercano posible a lo dicho) | Quién | Destino |
|---|---|---|---|
| <...> | <...> | <nombre> | `por incorporar` / <archivo o ID> |

## Preguntas abiertas
| # | Pregunta (una línea) | Opciones propuestas | Bloquea |
|---|---|---|---|

## Artefactos tocados
| Archivo | Acción | IDs |
|---|---|---|

## Próximo paso
<lo primero que debe hacerse si la sesión se interrumpe>
```

### `history.md`
```markdown
# Bitácora de planificación (solo se añade al final)
> Al cerrar cada sesión se añade su entrada. No se editan entradas anteriores.
---
## <AAAA-MM-DD> — <fase> — <foco>
- **Resumen:** <3-5 viñetas con lo que se decidió o produjo>
- **Artefactos:** <rutas creadas o modificadas>
- **Estados cambiados:** <US-NNN: En refinamiento → Lista para desarrollo>
- **Pendiente:** <OBS abiertas que quedaron>
- AAAA-MM-DD · Revisión DoR · US-NNN · LISTA|CAMBIOS REQUERIDOS   <!-- líneas añadidas por el Revisor -->
```

---

## 11. `entregas/ENT-NNN-EPIC-NNN-<slug>.md`  (paquete para el harness de implementación)

````markdown
# ENT-NNN — Entrega de EPIC-NNN <nombre>

> Paquete autocontenido para el harness de implementación. Copia generada de `docs/`: no se edita a mano. La fuente de verdad es el repositorio de planificación.

| Campo | Valor |
|---|---|
| Épica | EPIC-NNN — <nombre> |
| Alcance | Épica completa / Selección: US-NNN, US-NNN |
| Generada el | <AAAA-MM-DD> |
| Estado | Generada / Retornada / Reemplazada |
| Reemplaza a | <ENT-NNN o —> |
| Adjuntos | <archivos que el usuario debe entregar junto con este paquete, o «Ninguno»> |
| Revisión de la entrega | <fecha> · ENTREGA LISTA / CAMBIOS REQUERIDOS |

## Instrucciones para el implementador
1. Implementa las historias **en el orden indicado**, una a la vez.
2. Cada historia es la especificación: su alcance, reglas y criterios (`CA-NN`) mandan. No amplíes el alcance ni cambies requisitos.
3. Los criterios de aceptación son lo que debe demostrarse. Si una historia o un criterio es ambiguo, contradictorio o le falta un dato: no lo asumas en silencio; registra la duda, marca esa historia como bloqueada y continúa con otra que no dependa de ella.
4. Si algo no se ejecutó o no se verificó, dilo; no afirmes que funciona.
5. Este documento no incluye diseño técnico: las decisiones de implementación son tuyas y siguen la arquitectura del proyecto donde implementas.
6. Al terminar (o al bloquearte) entrega el **informe de retorno** con el formato del final.

## Orden de implementación
| Orden | Historia | Título | Depende de | Motivo del lugar |
|---|---|---|---|---|
| 1 | US-NNN | <...> | — | <...> |

### Prerrequisitos fuera de esta entrega
<historias de otras épicas o integraciones que ya deben existir; o «Ninguno»>

## Contexto compartido
> Solo lo que las historias referencian. Texto completo, sin duplicados.
### CAP-NNN — <nombre>
### ROL-NNN — <nombre>
### REG-NNN — <nombre>
### INT-NNN — <nombre>

## Contexto adicional
> Hechos confirmados que las historias usan y que en `docs/` viven fuera de CAP/ROL/REG/INT/US (épicas, `OBS` resueltas, entrevistas). Copia fiel de la parte confirmada, cada ítem con su fuente (`docs/...`, sección) y el `US-NNN` que lo usa. No incluyas deliberaciones, `OBS` abiertas ni historial de revisiones. Si no aplica: «Ninguno».
### CTX-01 — <tema> (fuente: <ruta y sección>; usado por: US-NNN)

## Anexos
> Archivos de datos que las historias referencian (CSV, tablas de catálogo, ejemplos). Cada anexo con identificador, fuente y las historias que lo usan. Si es pequeño, se incluye completo en un bloque de código; si es grande, se indica y el usuario lo adjunta junto con la entrega (campo *Adjuntos*). Si no aplica: «Ninguno».
### ANX-01 — <nombre> (fuente: <ruta>; usado por: US-NNN)
```text
<contenido o «Adjunto: <nombre de archivo>»>
```

## Historias
### US-NNN — <título>
<contenido fiel de la historia, sin *Definition of Ready* ni *Registro de cambios*; los enlaces a `docs/` se sustituyen por una referencia interna: «ver Contexto compartido: REG-NNN», «ver Contexto adicional: CTX-01» o «ver Anexo: ANX-01»>

## Cambios respecto a la entrega anterior
<solo si reemplaza a otra: qué historias cambiaron y por qué>

## Formato del informe de retorno
```text
RETORNO ENT-NNN
US-NNN: Implementada | Bloqueada | Parcial
  CA-01: Validado con test automatizado | Validado manualmente | No validado | No cumplido — <evidencia o motivo>
  Dudas o ambigüedades: <...> (o «ninguna»)
  Supuestos tomados: <...> (o «ninguno»)
  Verificación ejecutada: <qué se ejecutó> | no ejecutada
```
````
