"""Banco de preguntas del taller. Índices correctos: 0=A, 1=B, 2=C."""

def pregunta_1():
    """Devuelve la pregunta 1."""
    return {'titulo': 'Entornos de desarrollo', 'enunciado': 'Estás trabajando en dos proyectos de Python que requieren versiones diferentes de una misma biblioteca. ¿Cuál es la forma más adecuada de evitar conflictos entre sus dependencias?', 'opciones': ['Instalar todas las versiones de la biblioteca en el entorno `base`.', 'Crear un entorno de Conda independiente para cada proyecto.', 'Guardar cada proyecto en una carpeta diferente, utilizando el mismo entorno de Python.'], 'correcta': 1}

def pregunta_2():
    """Devuelve la pregunta 2."""
    return {'titulo': 'Reproducibilidad con `environment.yml`', 'enunciado': 'Un compañero necesita ejecutar tu proyecto utilizando las mismas dependencias. Le proporcionas el archivo `environment.yml`.\n\n¿Qué comando debe utilizar para crear el entorno descrito en ese archivo?', 'opciones': ['`conda env create -f environment.yml`', '`conda activate environment.yml`', '`conda install environment.yml`'], 'correcta': 0}

def pregunta_3():
    """Devuelve la pregunta 3."""
    return {'titulo': 'Jupyter Notebooks y kernels', 'enunciado': 'Tienes un notebook abierto en VS Code y necesitas ejecutarlo utilizando un entorno de Conda que contiene las bibliotecas del proyecto.\n\n¿Qué debes hacer antes de ejecutar las celdas?', 'opciones': ['Cambiar el nombre del notebook para que coincida con el entorno.', 'Copiar el notebook dentro de la carpeta de instalación de Conda.', 'Seleccionar como kernel el entorno de Python correspondiente.'], 'correcta': 2}

def pregunta_4():
    """Devuelve la pregunta 4."""
    return {'titulo': 'Directorio de trabajo y rutas', 'enunciado': 'Considera la siguiente estructura:\n\n```text\nproyecto/\n├── data/\n│   └── imagen.png\n└── notebooks/\n    └── analisis.ipynb\n```\n\nSi el directorio de trabajo actual es `proyecto/notebooks/`, ¿qué ruta relativa permite acceder a `imagen.png`?', 'opciones': ['`./data/imagen.png`', '`../data/imagen.png`', '`../../data/imagen.png`'], 'correcta': 1}

def pregunta_5():
    """Devuelve la pregunta 5."""
    return {'titulo': 'Manejo de archivos con `pathlib`', 'enunciado': 'Observa el siguiente código:\n\n```python\nfrom pathlib import Path\n\nruta = Path("..") / "data" / "imagen.png"\n```\n\n¿Qué representa el operador `/` cuando se utiliza entre objetos `Path` y componentes de una ruta?', 'opciones': ['Construye una ruta combinando sus componentes.', 'Realiza una división matemática entre directorios.', 'Comprueba automáticamente si el archivo existe.'], 'correcta': 0}

def pregunta_6():
    """Devuelve la pregunta 6."""
    return {'titulo': 'Control de versiones con Git', 'enunciado': 'Modificaste un archivo y quieres registrar su nueva versión en el historial del repositorio.\n\n¿Cuál es la secuencia correcta?', 'opciones': ['`git commit` → `git add` → `git status`', '`git push` → `git commit` → `git add`', '`git add` → `git commit`'], 'correcta': 2}

def pregunta_7():
    """Devuelve la pregunta 7."""
    return {'titulo': 'Uso de `.gitignore`', 'enunciado': 'En un repositorio creaste un archivo llamado `archivo_no_versionable.txt` que todavía no ha sido versionado. Después agregaste su nombre a `.gitignore`.\n\n¿Qué comportamiento debes esperar al ejecutar `git status`?', 'opciones': ['Git elimina automáticamente el archivo de tu computadora.', 'Git deja de mostrar el archivo ignorado como pendiente de versionar.', 'Git publica el archivo en GitHub, pero oculta su contenido.'], 'correcta': 1}

def pregunta_8():
    """Devuelve la pregunta 8."""
    return {'titulo': 'Autenticación SSH con GitHub', 'enunciado': 'Durante la configuración SSH generaste dos archivos:\n\n```text\nid_ed25519_github\nid_ed25519_github.pub\n```\n\n¿Cuál de las siguientes acciones es correcta?', 'opciones': ['Agregar `id_ed25519_github.pub` a GitHub y mantener la clave privada protegida en tu computadora.', 'Agregar ambos archivos a GitHub para completar la autenticación.', 'Compartir `id_ed25519_github` y conservar únicamente el archivo `.pub` en tu computadora.'], 'correcta': 0}

def pregunta_9():
    """Devuelve la pregunta 9."""
    return {'titulo': 'Google Colab desde VS Code', 'enunciado': 'Abres un notebook en VS Code y seleccionas un runtime de Google Colab como kernel.\n\n¿Dónde se ejecutan las instrucciones de Python?', 'opciones': ['Siempre en el entorno `base` de Conda de tu computadora.', 'En GitHub, porque ahí se almacenan los repositorios.', 'En el runtime remoto proporcionado por Google Colab.'], 'correcta': 2}

def pregunta_10():
    """Devuelve la pregunta 10."""
    return {'titulo': 'Integración entre Colab, GitHub y Google Drive', 'enunciado': 'Clonaste un repositorio de GitHub dentro de `/content` en Google Colab, procesaste una imagen y necesitas conservar el resultado después de que termine la sesión.\n\n¿Cuál es la estrategia más adecuada?', 'opciones': ['Guardar el resultado únicamente dentro de `/content`, porque su contenido permanece disponible después de finalizar el runtime.', 'Montar Google Drive y guardar el resultado dentro de `MyDrive`.', 'Mantener abierta la pestaña de VS Code para que Colab conserve indefinidamente todos los archivos del runtime.'], 'correcta': 1}

PREGUNTAS = {
    1: pregunta_1,
    2: pregunta_2,
    3: pregunta_3,
    4: pregunta_4,
    5: pregunta_5,
    6: pregunta_6,
    7: pregunta_7,
    8: pregunta_8,
    9: pregunta_9,
    10: pregunta_10,
}
