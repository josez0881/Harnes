#!/usr/bin/env python3
"""PreToolUse (Edit|Write|NotebookEdit): bloquea escrituras en las ramas de integración.

Solo actúa sobre archivos versionables de este repositorio (o de sus worktrees).
Permite rutas externas (scratchpad, memoria) y archivos ignorados por git.
Regla completa: «Gate de rama» (regla 10) en CLAUDE.md. No cubre escrituras hechas por Bash.
"""
import json
import os
import subprocess
import sys

# [POR ADAPTAR: ramas de integración del proyecto; deben coincidir con la regla 10 de CLAUDE.md]
RAMAS_PROTEGIDAS = {"develop", "main"}


def git(directorio, *args):
    r = subprocess.run(["git", "-C", directorio, *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def main():
    datos = json.load(sys.stdin)
    entrada = datos.get("tool_input", {})
    ruta = entrada.get("file_path") or entrada.get("notebook_path")
    proyecto = os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd")
    if not ruta or not proyecto:
        return 0

    ruta = os.path.realpath(os.path.join(datos.get("cwd") or proyecto, ruta))
    directorio = os.path.dirname(ruta)
    while not os.path.isdir(directorio):  # el archivo o su carpeta pueden ser nuevos
        directorio = os.path.dirname(directorio)

    comun = ("rev-parse", "--path-format=absolute", "--git-common-dir")
    repo_archivo = git(directorio, *comun)
    if repo_archivo is None or repo_archivo != git(proyecto, *comun):
        return 0  # fuera de este repositorio

    rama = git(directorio, "symbolic-ref", "--short", "-q", "HEAD")
    if rama not in RAMAS_PROTEGIDAS:
        return 0

    ignorado = subprocess.run(
        ["git", "-C", directorio, "check-ignore", "-q", "--no-index", ruta],
        capture_output=True,
    )
    if ignorado.returncode == 0:
        return 0

    print(
        f"Rama protegida: no se escribe directamente en '{rama}'. Aplica el "
        "«Gate de rama» de CLAUDE.md: crea una rama desde la rama base antes de escribir.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
