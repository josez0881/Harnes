# Describe Project Prompt

## 1. Identificar qué te entregaron
Antes de tocar código, determina:
* ¿Es un proyecto completo o solo una plantilla?
* ¿Qué lenguaje/framework utiliza?
* ¿Qué versión del lenguaje/framework?
* ¿Qué servidor requiere?
* ¿Qué base de datos utiliza?
* ¿Cómo se configura el acceso a BD?
* ¿Tiene dependencias externas?
* ¿Cómo se ejecuta localmente?
* ¿Tiene algún sistema de autenticación?
* ¿Tiene gestión de usuarios/roles/permisos?
* ¿Tiene módulos ya desarrollados?
* ¿Existe documentación?

El objetivo es poder responder:
"¿Qué necesito instalar y ejecutar para levantar exactamente el proyecto que me entregaron?"

## 2. Levantar la plantilla sin modificarla

Haz una copia del proyecto original y trabaja sobre otra carpeta/repositorio.
Primero consigue que:
```
Proyecto original
       ↓
Instalar dependencias
       ↓
Configurar entorno
       ↓
Configurar BD
       ↓
Ejecutar
       ↓
Aplicación funcionando
```

**No desarrolles todavía.**
Si no puedes levantar el proyecto base, todavía no estás en condiciones de empezar el desarrollo nuevo.

## 3. Hacer un mapa de la arquitectura

Aquí empieza realmente la ingeniería inversa.
Identifica:
```
Usuario -> UI -> Controlador -> Servicios -> BD
```

Pero no asumas que esa es su arquitectura. **Descubre la arquitectura real del proyecto.**
Busca cosas como:
- estructura de carpetas
- punto de entrada
- configuración
- rutas
- controladores
- servicios
- modelos
- repositorios
- componentes
- vistas
- middleware
- autenticación
- autorización
- utilidades
- manejo de errores
- logs
- acceso a BD
- migraciones
- archivos de configuración

## 4. Entender la base de datos

Esto es especialmente importante en una plantilla institucional.

No te limites a mirar las tablas.

Determina:

**Tablas**

```
usuarios
roles
permisos
...
```

**Relaciones**

```
usuario
   ↓
rol
   ↓
permisos
```

**Convenciones**

Por ejemplo:

- nombres de tablas
- nombres de columnas
- PK/FK
- nombres de índices
- `created_at`, `updated_at`
- estados
- catálogos
- tablas históricas
- auditoría

Y muy importante:
> **Identifica qué parte de la BD pertenece al framework/base institucional y qué parte pertenece al negocio.**
>
No quieres terminar creando una tabla nueva que duplica una funcionalidad que la plantilla ya proporciona.

## 5. Seguir un caso de uso completo

Esta es probablemente **la técnica que más te recomiendo**.

Busca una funcionalidad sencilla que ya exista.

Por ejemplo:

> "Registrar usuario"
>

Y síguela desde principio a fin:

```
Pantalla -> Evento -> Controlador -> Servicio -> Validación -> Consulta -> Base de datos -> Respuesta -> Pantalla
```

Mientras haces esto, documenta:

| Capa | Elemento | Responsabilidad |
| --- | --- | --- |
| UI | `usuario_form` | Captura datos |
| Controller | `UsuarioController` | Recibe solicitud |
| Service | `UsuarioService` | Ejecuta lógica |
| Repository | `UsuarioRepository` | Acceso a BD |
| DB | `usuarios` | Persistencia |

Cuando puedas explicar **una funcionalidad completa**, ya tienes una comprensión mucho más útil que simplemente leer 200 archivos.

El entregable que busco es:
el primer entregable técnico debería ser prácticamente un "mapa de la plantilla": arquitectura, tecnologías, BD, módulos, dependencias, convenciones
