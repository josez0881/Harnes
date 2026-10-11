---
name: conventional-commit
description: Genera y ejecuta commits de Git usando el estándar Conventional Commits (feat, fix, docs, style, refactor, test, chore, perf, build, ci). Úsalo cada vez que el usuario pida "haz un commit", "commitea esto", "genera el mensaje de commit", "sube estos cambios" o cualquier instrucción para registrar cambios en Git, incluso si no menciona explícitamente "conventional commits". Infiere tipo y ámbito a partir del `git diff`, propone el mensaje en español, y solo ejecuta `git commit` tras confirmación del usuario.
---

# Conventional Commit

Genera mensajes de commit siguiendo el estándar [Conventional Commits](https://www.conventionalcommits.org/) y ejecuta el commit en el repositorio del usuario.

## Formato del mensaje

```
<tipo>[ámbito opcional]: <descripción>

[cuerpo opcional]

[notas de pie opcionales]
```

- **Descripción**: en español, en minúscula, modo imperativo/infinitivo ("añade", "corrige", "actualiza"), sin punto final, idealmente ≤ 72 caracteres.
- **Cuerpo**: en español, explica el *qué* y el *por qué* (no el *cómo*), solo si aporta contexto que la descripción no cubre.
- **BREAKING CHANGE**: si el cambio rompe compatibilidad, añade una nota de pie `BREAKING CHANGE: <explicación>`.

### Tipos válidos

| Tipo       | Cuándo usarlo                                                   |
|------------|-------------------------------------------------------------------|
| `feat`     | Nueva funcionalidad para el usuario final                        |
| `fix`      | Corrección de un bug                                              |
| `docs`     | Cambios solo en documentación                                     |
| `style`    | Formato, espacios, indentación (sin cambio de lógica)             |
| `refactor` | Cambio de código que no añade funcionalidad ni corrige un bug     |
| `perf`     | Cambio que mejora el rendimiento                                  |
| `test`     | Añade o corrige tests                                             |
| `build`    | Cambios en el sistema de build o dependencias externas            |
| `ci`       | Cambios en configuración/scripts de integración continua          |
| `chore`    | Otras tareas de mantenimiento (no afectan src ni tests)           |

## Flujo de trabajo

Sigue estos pasos en orden. No te saltes la confirmación del paso 4: el commit **nunca** se ejecuta sin que el usuario apruebe el mensaje final.

### 1. Verificar el repositorio y los cambios

```bash
git status --porcelain
git diff --staged
git diff
```

- Si no hay cambios (ni staged ni sin stage), avísalo y detente.
- Si hay cambios sin stage y el usuario no especificó cuáles commitear, pregunta si debes hacer `git add -A` (o cuáles archivos específicos) antes de continuar, salvo que el usuario ya haya dado esa instrucción explícitamente en su mensaje.

### 2. Inferir tipo y ámbito a partir del diff

Analiza `git diff --staged` (o `git diff` si nada está en stage) para inferir:

- **Tipo**: según la tabla de arriba. Reglas rápidas:
  - Archivos nuevos en `src/`, componentes o rutas nuevas → probablemente `feat`.
  - Cambios que corrigen un comportamiento erróneo (condicionales, validaciones, manejo de errores) → probablemente `fix`.
  - Solo archivos `.md`, `README`, comentarios → `docs`.
  - Solo archivos de test (`*.test.*`, `*.spec.*`, carpeta `tests/`) → `test`.
  - `package.json`, `composer.json`, lockfiles, configuración de build → `build`.
  - `.gitlab-ci.yml`, `.github/workflows/*` → `ci`.
  - Cambios de formato/linting sin lógica nueva → `style`.
  - Reestructuración sin cambio de comportamiento → `refactor`.
  - Si no encaja claramente en ninguno → `chore`.
- **Ámbito**: usa el nombre del módulo/carpeta/componente principal afectado (ej. `auth`, `api`, `dashboardMultas`). Si los cambios tocan múltiples áreas sin un ámbito claro, omítelo.

Esta inferencia es un punto de partida, no una decisión final — el paso 3 la corrige con el usuario.

### 3. Proponer el mensaje y permitir corrección

Muestra al usuario el mensaje propuesto completo (tipo, ámbito, descripción y cuerpo si aplica) **antes** de ejecutar nada, y pregúntale explícitamente si quiere ajustar el tipo, el ámbito, la descripción o el cuerpo. No asumas que el primer borrador es el final: espera confirmación o correcciones.

### 4. Ejecutar el commit

Una vez el usuario confirma (o corrige y luego confirma):

```bash
git add -A   # solo si aplica según el paso 1
git commit -m "<tipo>[ámbito]: <descripción>" -m "<cuerpo opcional>"
```

- Si hay `BREAKING CHANGE`, añade un `-m "BREAKING CHANGE: <explicación>"` adicional.
- Después de ejecutar, muestra la salida de `git log -1 --stat` para confirmar que el commit se creó correctamente.
- Si `git commit` falla (por ejemplo, hooks de pre-commit), muestra el error tal cual y no reintentes con `--no-verify` sin que el usuario lo pida explícitamente.

## Reglas importantes

- **Nunca** ejecutes `git push` a menos que el usuario lo pida explícitamente en la misma instrucción o en una instrucción posterior.
- **Nunca** hagas `git commit --amend` ni reescribas historial sin que el usuario lo pida de forma explícita.
- Si el usuario ya te da el tipo/ámbito/descripción en su instrucción, respeta eso en vez de inferirlo del diff, pero igual muéstraselo para confirmar antes de ejecutar el commit.
- Si el repositorio tiene múltiples cambios que claramente pertenecen a commits distintos (por ejemplo, una corrección de bug y una nueva funcionalidad no relacionada), sugiere dividirlos en commits separados en vez de forzarlos en uno solo.

## Convenciones para este repositorio de requerimientos

Este repositorio contiene documentación, así que casi todos los commits serán `docs`. Las reglas de inferencia de tipo del paso 2 que hablan de `src/`, `package.json` o tests aplican solo si el repositorio también contiene código.

- **Tipo**: `docs` para cualquier cambio en `docs/` o en estos archivos de instrucciones. `chore` solo para cambios en la configuración del repositorio.
- **Ámbito**: el ID principal afectado (`EPIC-001`, `US-003`, `CAP-001`, `REG-002`). Si el cambio toca varias épicas, omítelo.
- **Un commit por unidad lógica**: una historia nueva o modificada, o una épica. No mezcles historias de épicas distintas ni cambios de requisitos con cambios de estado de otra historia.
- **Cambios de estado** (por ejemplo, una historia pasa a `Lista para desarrollo`): commit propio, para poder ver en el historial cuándo se entregó al desarrollo.
- **Cuerpo**: cuando cambie un requisito de una historia que ya estaba en `En desarrollo` o posterior, indica el motivo del cambio.
- **Staging**: prefiere añadir los archivos concretos de la unidad lógica en lugar de `git add -A`.

Ejemplos:

```
docs(EPIC-001): añade épica de gestión de depósitos
docs(US-003): define criterios de aceptación de validación de duplicados
docs(US-003): marca la historia como lista para desarrollo
docs(OBS): registra decisión pendiente sobre depósitos anulados
```
