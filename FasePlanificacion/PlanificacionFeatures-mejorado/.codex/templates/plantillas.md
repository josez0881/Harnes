# Plantillas de artefactos

> Copia la plantilla que corresponda y rellénala. Reglas comunes:
> - Ningún marcador `<...>` puede quedar sin resolver: se reemplaza por contenido, por `Pendiente` o se borra la fila/sección si no aplica.
> - Texto sin etiqueta = confirmado y con fuente. Lo demás lleva `Pendiente`, `[Inferencia]` o `[No verificado]`.
> - Rutas siempre desde la raíz del repositorio (`docs/...`).
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
- **Estado:** Borrador / En refinamiento / En desarrollo / Completada / Descartada
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
| Estado | Borrador / En refinamiento / Lista para desarrollo / En desarrollo / Implementada / Validada / Bloqueada / Descartada |
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
> Si un documento no es necesario para esta historia, no lo enlaces. Si lo es y falta, la historia no está lista.

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
