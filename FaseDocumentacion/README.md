# Harness de documentación

Se ejecuta en el **repositorio del sitio Docusaurus**. Lee el código del sistema (solo lectura) y escribe la documentación en dos instancias del plugin `docs`: `docs-tecnica/` (equipo técnico y funcional) y `docs-usuario/` (usuario final).

## Vista general

```
CADA SESIÓN (Documentador)
├── Arranque: lee progress/current.md y config-docs.md → resuelve POR CONFIRMAR
│
├── A. Actores         → docs-tecnica/actores/actores-del-sistema.md
├── B. Módulo          → docs-tecnica/modulos/MOD-NN-*/index.md
├── C. Especificación  → docs-tecnica/especificaciones/MOD-NN-*/FUNC-MODNN-NN-*.md
├── D. Permisos        → docs-tecnica/permisos/PERM-MOD-NN-*.md
├── E. Guía y FAQs     → docs-usuario/guias/MOD-NN-*/FUNC-MODNN-NN-*.md
│        ▲  (antes de B–E: Explorador lee el código → progress/explore_*.md)
│        │
├── F. Revisión        SESIÓN NUEVA, Revisor R1–R8 → draft: false  o  progress/review_<ID>.md
│        └──── bucle C–E ↔ F (máximo 2 rondas, luego decides tú)
│
└── G. Publicación     tú: build y despliegue del sitio
```

## Fase por fase

| Fase | Quién | Qué ocurre | Sale con |
|---|---|---|---|
| **Arranque** | Documentador | Lee el estado y la configuración. Lo que está en `docusaurus.config.*` o `package.json` lo lee; el resto te lo pregunta | `config-docs.md` completo |
| **Exploración** | Explorador | Una pregunta acotada por tema (permisos, pantallas, validaciones, flujo). Solo lectura, con `archivo:línea`, sin credenciales | `progress/explore_<tema>.md` |
| **A–E** | Documentador | Redacta con plantillas. Cada dato con fuente; lo demás `[PENDIENTE]`, `[POR CONFIRMAR]` o `[Inferencia]`. Toda página nace con `draft: true` | Páginas en borrador |
| **F. Revisión** | Revisor | En sesión distinta, contrasta con el código y evalúa R1–R8. Solo él cambia `draft` a `false` | `LISTA` o hallazgos |
| **G. Publicación** | Tú | Build y despliegue. El harness no ejecuta `build` salvo petición expresa | Sitio actualizado |

## Convenciones

| Tema | Decisión |
|---|---|
| IDs | `ACT-NN`, `MOD-NN`, `FUNC-MODNN-NN`, con ceros a la izquierda |
| Trazabilidad entre instancias | Por `FUNC-MODNN-NN` en nombre de archivo y frontmatter, más enlaces cruzados por `routeBasePath` |
| Orden del sidebar | Autogenerado. `position` solo en `_category_.json` de primer nivel; `sidebar_position` solo en `intro.md` y `faqs.md` |
| Diagramas | Mermaid. Casos de uso aproximados con `flowchart` (frontera y herencia) |
| Permisos | Matriz de funcionalidad × rol, con evidencia en el código. Sustituye a la RACI de la plantilla original |
| Capturas | Las pones tú, con datos de prueba, en `img/` junto a la guía. Mientras tanto, aviso `:::caution` |
| Borradores | `draft: true` hasta que el Revisor concede `draft: false` + `revisada` |
| Publicable | Sin credenciales, hosts, rutas de código, tablas ni datos personales reales |

## Qué decides tú

- La ruta del código del sistema, y dar a Claude Code acceso de lectura a ella (por ejemplo, abriendo la sesión con `--add-dir`).
- Confirmar o cambiar los IDs que el Documentador cree (`ACT-NN`, `MOD-NN`, `FUNC-MODNN-NN`).
- Aprobar cada fase antes de pasar a la siguiente.
- Abrir la sesión nueva para la revisión.
- Aportar las capturas de pantalla.
- Qué hacer cuando el código y lo que tú sabes no coinciden.
- Build, despliegue y cambios en la configuración del sitio.

## Decisiones tomadas por el modelo (revertibles)

1. **Evidencia fuera de las páginas.** El `archivo:línea` vive en `progress/`, no en las páginas publicadas, para no exponer rutas del código en un sitio que puede ser público.
2. **Imágenes junto a la guía** (`img/`), no en `static/`.
3. **`PERM-` como nombre de archivo**, no como ID nuevo.
4. **Máximo de 2 rondas** de `CAMBIOS REQUERIDOS` antes de escalar al humano.
5. **Commits solo a petición**, con la skill, sin identificador de IA.

## Críticas

1. **[Inferencia] El código dice qué hace el sistema, no qué debería hacer.** Documentar desde el código puede fijar defectos como si fueran reglas. El Documentador debe avisarte de lo que parezca un error y esperar tu respuesta; depende de que lo cumpla.
2. **Sin hooks, todo es instrucción.** Que no se ejecute código del sistema ni se lean credenciales depende de que los agentes sigan las reglas, no de un mecanismo. El permiso de lectura que concedas a la ruta del código es la barrera real: ábrela de solo lectura si puedes.
3. **[No verificado] Varias afirmaciones sobre Docusaurus** (Mermaid con `@docusaurus/theme-mermaid`, `draft` excluido en producción, enlaces entre instancias por ruta del sitio, campos de frontmatter propios) están escritas de memoria. Compruébalas con la documentación vigente o con un `build` antes de fiarte.
4. **Los casos de uso en Mermaid son una aproximación.** Si necesitas UML formal, hace falta otra herramienta.
5. **La revisión R4 depende de poder leer el código.** Si la sesión del Revisor no tiene acceso a la ruta, no podrá dar `LISTA`.
