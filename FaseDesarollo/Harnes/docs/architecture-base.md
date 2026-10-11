# Mapa del proyecto base (architecture-base)

> Se genera en el bootstrap siguiendo `docs/DescribeProject.md`. Describe el proyecto **existente**; no fija reglas para lo nuevo (eso es `docs/architecture.md`).
> Cada dato lleva su origen entre corchetes: `[observado: <archivo>]`, `[decisión del modelo: motivo]`, `[decisión del humano]` o `POR CONFIRMAR`. Sin evidencia, no se escribe: `POR CONFIRMAR`.
> Las convenciones de código observadas viven en `docs/conventions.md`; aquí solo se documentan las de base de datos (§4).
> Terminología: donde los documentos del humano dicen «plantilla institucional», se refieren al proyecto base que se describe aquí. Si el repositorio no parte de una plantilla, léase «código existente».

## 0. Resumen y estado
- ¿Proyecto completo o solo plantilla? [POR ADAPTAR]
- Estado de levantamiento: `levantado` / `no levantado` / `no verificado`, con el motivo [POR ADAPTAR]
- Resumen en tres líneas [POR ADAPTAR]

## 1. Qué se entregó
| Pregunta | Respuesta | Origen |
|---|---|---|
| Lenguaje y framework | [POR ADAPTAR] | |
| Versión del lenguaje y del framework | [POR ADAPTAR] | |
| Servidor requerido | [POR ADAPTAR] | |
| Base de datos utilizada | [POR ADAPTAR] | |
| Cómo se configura el acceso a BD (solo el mecanismo; sin credenciales) | [POR ADAPTAR] | |
| Dependencias externas | [POR ADAPTAR] | |
| Cómo se ejecuta localmente | [POR ADAPTAR] | |
| Sistema de autenticación | [POR ADAPTAR] | |
| Gestión de usuarios, roles y permisos | [POR ADAPTAR] | |
| Módulos ya desarrollados | [POR ADAPTAR] | |
| Documentación existente | [POR ADAPTAR] | |

**¿Qué hay que instalar y ejecutar para levantar exactamente el proyecto entregado?** [POR ADAPTAR]

## 2. Cómo se levanta
| Paso | Comando o acción | Origen | Estado (`ejecutado` / `no ejecutado: <motivo>` / `lo ejecutó el humano`) |
|---|---|---|---|
| Instalar dependencias | [POR ADAPTAR] | | |
| Configurar entorno | [POR ADAPTAR] | | |
| Configurar BD | [POR ADAPTAR] | | |
| Ejecutar | [POR ADAPTAR] | | |
| Aplicación funcionando | [POR ADAPTAR] | | |

## 3. Arquitectura real
Flujo descubierto (no asumido): [POR ADAPTAR: diagrama ASCII breve]

| Elemento | Dónde vive | Responsabilidad |
|---|---|---|
| Estructura de carpetas | [POR ADAPTAR] | |
| Punto de entrada, configuración, rutas | [POR ADAPTAR] | |
| Controladores, servicios, modelos, repositorios, componentes, vistas | [POR ADAPTAR: solo los que existen] | |
| Middleware, autenticación, autorización | [POR ADAPTAR] | |
| Utilidades, manejo de errores, logs | [POR ADAPTAR] | |
| Acceso a BD, migraciones, archivos de configuración | [POR ADAPTAR] | |

## 4. Base de datos
- **Tablas y relaciones** (usuarios, roles, permisos y el resto): [POR ADAPTAR]
- **Convenciones:** nombres de tablas y columnas, PK/FK, índices, `created_at`/`updated_at`, estados, catálogos, tablas históricas, auditoría: [POR ADAPTAR]
- **Qué pertenece al framework o base institucional y qué pertenece al negocio:** [POR ADAPTAR]
- Fuente del esquema: migraciones, modelos o scripts del repo. Una consulta directa a una BD viva solo con confirmación humana y solo de estructura, nunca de datos.

## 5. Caso de uso completo seguido
Funcionalidad elegida: [POR ADAPTAR]

| Capa | Elemento | Responsabilidad |
|---|---|---|
| [POR ADAPTAR] | | |

## 6. Módulos de negocio existentes
[POR ADAPTAR: lista con su ubicación y propósito]

## 7. Componentes del proyecto base reutilizables
Soporte que ya existe y **no debe duplicarse** al implementar algo nuevo.

| Capacidad | ¿Existe? | Dónde y cómo se usa |
|---|---|---|
| Autenticación | [POR ADAPTAR] | |
| Usuarios, roles y permisos | [POR ADAPTAR] | |
| Auditoría | [POR ADAPTAR] | |
| Logging | [POR ADAPTAR] | |
| Manejo de errores | [POR ADAPTAR] | |
| Conexión a base de datos | [POR ADAPTAR] | |
| Componentes visuales | [POR ADAPTAR] | |
| Configuración | [POR ADAPTAR] | |
| Utilidades comunes | [POR ADAPTAR] | |

## 8. Brechas y puntos por confirmar
[POR ADAPTAR: lo que no se pudo determinar o levantar, cada ítem con su motivo]
