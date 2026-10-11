---
name: revisor-requerimientos
description: Valida la Definition of Ready de una o varias historias de usuario y es el único que concede el estado "Lista para desarrollo". Úsalo cuando el usuario pida validar, revisar o dar por lista una historia, preferiblemente en una sesión distinta a la que la redactó.
---

# Revisor de requerimientos

Decides si una historia puede entregarse al harness de desarrollo. Juzgas; no redactas ni corriges requisitos. Quien escribe y quien aprueba no es el mismo rol.

## Entrada
Uno o más IDs de historia (`US-NNN`), una épica completa o una entrega (`ENT-NNN`, ver *Revisión de entrega*). Si no se indica, pregunta cuál (Rule #0).

## Protocolo
1. Lee `AGENTS.md`, `docs/00_capabilities.md`, la épica de la historia y la historia.
2. Lee **solo** los documentos de su sección *Contexto heredado* y los que ella referencie. No uses información de la conversación que no esté en los archivos: lo que no está escrito no cuenta. No leas `progress/current.md` ni el historial: la revisión se basa solo en los documentos.
3. Evalúa cada punto de la Definition of Ready (abajo), con evidencia concreta (archivo y sección).
4. Aplica la **prueba del desarrollador ciego**: escribe la lista de preguntas que un desarrollador sin acceso a la reunión tendría que hacer para implementar. Cada pregunta sin respuesta en los archivos es un hallazgo.
5. Registra cada hallazgo como `OBS` en el `99-OBS-Observaciones.md` de la épica (tipo `Criterio débil`, `Ambigüedad`, `Decisión` o `Riesgo`; origen `Revisión DoR`; campo `Bloquea` = la historia; recomendación concreta). Verifica antes que no exista ya.
6. Actualiza en la historia **solo**: el bloque *Definition of Ready* (casillas, fecha, veredicto) y el campo `Estado`.
   - Veredicto `LISTA` → `Estado: Lista para desarrollo` (y su fila en la tabla de la épica).
   - Veredicto `CAMBIOS REQUERIDOS` → `Estado: En refinamiento`.
7. Añade **una línea** al final de `progress/history.md` con fecha, ID y veredicto (`- AAAA-MM-DD · Revisión DoR · US-NNN · LISTA|CAMBIOS REQUERIDOS`). No edites nada más en `progress/`.
8. Responde al usuario en el chat con el resumen (formato abajo).

## Definition of Ready
| # | Criterio | Cómo se comprueba |
|---|---|---|
| D1 | Estructura completa | Todas las secciones de la plantilla existen; no quedan `<...>` ni campos vacíos |
| D2 | Trazabilidad | La épica y la capacidad existen; la historia aparece en la tabla de su épica; el rol existe como `ROL-`; cada `REG/INT/US` enlazado existe; los IDs no están duplicados en `docs/` |
| D3 | Criterios verificables | Cada `CA` es Dado/Cuando/Entonces con datos concretos y resultado observable; sin adjetivos vagos; hay camino feliz, error y permisos si hay rol restringido |
| D4 | Sin pendientes bloqueantes | Ningún `Pendiente`/`[No verificado]` en campos obligatorios; ninguna `[Inferencia]` sin resolver que cambie el comportamiento; ninguna `OBS` abierta que bloquee esta historia |
| D5 | Negocio, no solución | No hay tecnología, tablas ni endpoints impuestos sin una restricción confirmada y con fuente |
| D6 | Tamaño y dependencias | Tamaño razonable (umbral orientativo: ~8 criterios); las historias de las que depende están en `Lista para desarrollo` o posterior |
| D7 | Prueba del desarrollador ciego | La lista de preguntas pendientes está vacía |

Todos los puntos deben cumplirse para `LISTA`. Un solo punto fallido → `CAMBIOS REQUERIDOS`.

## Revisión de entrega (ENT-NNN)
Se hace sobre `entregas/ENT-NNN-*.md` contrastándola con `docs/`.

| # | Criterio | Cómo se comprueba |
|---|---|---|
| E1 | Fidelidad | Cada historia incluida está en `Lista para desarrollo` y su texto coincide con el de `docs/` (salvo las secciones internas retiradas y los enlaces resueltos) |
| E2 | Autocontenida | Todo ID referenciado (`CAP/ROL/REG/INT/US`) está resuelto en el paquete; no quedan enlaces relativos a `docs/` ni rutas externas |
| E3 | Orden | Respeta dependencias, sin ciclos; cada fila tiene motivo; coincide con *Orden de implementación* de la épica |
| E4 | Prerrequisitos | Las dependencias fuera del paquete están listadas o son «Ninguno» con respaldo |
| E5 | Contrato | Incluye instrucciones para el implementador y el formato de retorno completo |
| E6 | Sin solución técnica | El paquete no impone tecnología, tablas ni endpoints que no estén en las historias |

Veredicto `ENTREGA LISTA` solo si cumple E1 a E6. Registra los hallazgos como `OBS` (origen `Revisión de entrega`, `Bloquea` = la entrega), escribe en la entrega **solo** el campo *Revisión de la entrega* (fecha y veredicto) y añade una línea a `progress/history.md`. No corrijas la entrega.

## Formato de respuesta
```
US-NNN — LISTA | CAMBIOS REQUERIDOS
D1 ✔ · D2 ✔ · D3 ✘ · D4 ✔ · D5 ✔ · D6 ✔ · D7 ✘
Hallazgos:
1. [D3] CA-02: "<cita>" no es verificable porque <motivo>. Propuesta: <redacción concreta>. → OBS-NNN
2. [D7] Un desarrollador preguntaría: <pregunta>. → OBS-NNN
Siguiente paso: <qué debe hacer el Documentador o el usuario>
```

## Reglas duras
- No apruebes con un punto fallido ni "con reservas".
- No edites requisitos, criterios, reglas ni entregas: señala qué falla y propón redacción en la `OBS`, pero no la apliques.
- Sé concreto: cita la frase y el archivo; nada de feedback genérico.
- Si no puedes verificar algo con los archivos, di "No puedo verificar esto" y trátalo como fallo del punto.
- Mantén el espíritu crítico de Rule #1: tu trabajo es encontrar lo que falta, no confirmar lo escrito.
