# Python Packages

Es un resumen de este [libro](https://py-pkgs.org/)

## 1. Introduction

Como mínimo, un paquete junta clases, variables, funciones y otros scripts para
facilitar el uso a través de varios proyectos. Tambien, los paquetes tienen
contenido extra como documentación y tests que se vuelven muy importantes si la
intención es compartir el paquete.

Aunque la intención no sea compartir el código con otras personas, los paquetes
ahorran tiempo. Los paquetes hacen significativamente mas fácil reusar y mantener
el código en un mismo proyecto y entre diferentes proyectos también. Despues de
programar por un tiempo, la mayoría de las personas llegan a un punto donde quieren
reusar el código. Para los principiantes, esto es algo que se logra haciendo
copy-paste del código. Además de ser ineficiente, esta práctica dificulta la mejora
y el mantenimiento del código. Crear un paquete resuelve todos estos problemas.

## 2. System setup

Hay algunas recomendaciones de extensiones para el vsc, pero no instale nada la
verdad.

## 3. How to package a Python

### 3.2 Package structure

#### 3.2.1 A brief introduction

Para desarrollar el módulo de ejemplo en el libro, llamado *pycounts*, se da como
ejemplo la siguiente estrcutura del directorio a modo de ejemplo.

- Un root directory. */pycounts*
- Uno o mas módulos de Python (archivos con extension .py) in a subdirectroy
*src/pycounts/*
- Instrucciones sobre como buildear el paquete *pyproject.toml*
- La documentación importante va en el root, en el archivo *README*, y el resto
en un subdirectorio en */docs*.
- Test van en */test*

#### 3.2.2. Creating a package structure

En esta sección dice que use *cookiecutter* con un template que armaron para el
libro pero no me anda el template y las otras que use no son nada que ver con esta
y parecen un quilombo.

Ejemplo:

pycounts  
├── .readthedocs.yml  
├── CHANGELOG.md  
├── CONDUCT.md  
├── CONTRIBUTING.md  
├── docs  
│   └── ...  
├── LICENSE  
├── pyproject.toml  
├── README.md  
├── src  
│   └── pycounts  
│       ├── __init__.py  
│       └── pycounts.py  
└── tests  
    └── ...  

#### 3.5.2 Installing your package

Como escribir los commits se basan en [Angular.js](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines)

La parte que mas me gusto es esta:

__Type__
Must be one of the following:

- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- refactor: A code change that neither fixes a bug nor adds a feature
- perf: A code change that improves performance
- test: Adding missing or correcting existing tests
- chore: Changes to the build process or auxiliary tools and libraries such as documentation generation

#### 3.6.1 Dependency version constraints

#### 3.7.3 Code coverage

Code coverage = lines executed / total lines * 100

Con  `pytest-cov` podemos medir el code coverage.

Con `pytest --cov` en consola se corre

Con `pytest --cov --cov-report html` se genera un reporte en HTML que te marca
las lineas que no estan cubiertas.

### 3.8. Package documentation

Documentation:

README, /docs, Changelog y Docstrings. El resto no viene al caso.

Si usas `help()` te tira el Docstring.

### 3.9 Tagging a package release with version control

Taggear un release signfica fijar un punto específico en la historia del repositorio,
para luego crear un descargable de ese release.

Se crea el tag usando el comando `git tag`.

```Python
git tag v0.1.0
git push --tags
```

En GitHub se crea un .zip o .tar.gz basado en el tag. De Esta forma los usuarios
pueden descargar este paquete con el tag que fue creado.

## 4 Package structure and distribution

### 4.2.1. Packaging fundamentals

El `__init__.py` le dice a Python que trate al directorio como un paquete, es común
que se inicialicen vacios.

Nosotros estamos creando un *regular package*, existe otro tipo llamado *namespace package*,
no es un tópico que nos competa en este momento.

#### 4.2.2. Package and module names

En  [Python Enhancement Proposal (PEP) 8](https://peps.python.org/pep-0008/) se
habla de la nomenclatura. Esto son las guías fundamentales:

- Paquetes y módulos deben tener single, short, all-lowercase names.
- Se pueden usar guiones bajos si mejora la lectura pero es desaconsejado.

Hay una regla para elegir nombres, la triple M:

1. Meaningful.
2. Memorable.
3. Manegable. Que no sean interminables.

#### 4.2.3. Intra-package references

Cuando creamos un paquete con múltiples módulos es común querer usar código de un
módulo en otro. Por ejemplo, consideremos la siguiente estructura de un paquete:

```Python
src
└── package
    ├── __init__.py
    ├── moduleA.py
    ├── moduleB.py
    └── subpackage
        ├── __init__.py
        └── moduleC.py
```

Esto se llama "intra-package" reference" y se puede realizar de manera absoluta
o relativa.

Los imports de manera absoluta usan el nombre completo del paquete. Los imports
de manera relativa usan puntos para indiar donde deben comenzar. Un solo punto
indica que es del package (o subpackage) y se le seguimos agregando puntos vamos
subiendo en la escala.

Ejemplos:

Import from moduleA in moduleB:

- Absolute: from package.moduleA import XXX
- Relative: from .moduleA import XXX

Import from moduleA in moduleC

- Absolute: from package.moduleA import XXX
- Relative: from ..moduleA import XXX

Import from moduleC in moduleA

- Absolute: from package.subpackage.moduleC import XXX
- Relative: from .subpackage.moduleC import XXX

PEP 8 recomienda el absoluto porque es explicito.

### 4.2.4. The init file

Antes discutimos como el archivo `__init__.py` le indica a python que el directorio
es un paquete. Este archivo se puede dejar vacio y usarlo con el único proposito
de que el interprete entienda que ese directorio es un paquete. Pero tambien, se
puede utilizar para agregar objetos, proveer documentación e inicilizar código.

Se define la versión del paquete en dos lugares:

1. `pyproject.toml`
2. En `__init__.py` usando el atributo `__version__`.

Algunas veces podemos encontrar la version harcodeada en el `__init__.py` pero
eso implica que debemos actualizar manualmente ambos lugares cada vez que cambiamos
la versión, en el `__init__.py` y en `pyproject.toml`. Es mejor tener definida la
versión del proyecto solo en el `pyproject.toml` y tomarla automáticamente en el
`__init__.py` usando `importlib.metadata.version()`.

```Python
# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts")
```

#### 4.2.7. The source layout

En este libro se estuvo guardando el código dentro de la carpeta `src/`, como en
el ejemplo que esta abajo.

```Python
pkg
├── ...
├── src
│   └── pkg
│       ├── __init__.py
│       ├── module1.py
│       └── subpkg
│           ├── __init__.py
│           └── module2.py
└── ...
```

Pero guardar el código en la carpeta `src/` no es necesario para crear un paquete,
es común ver paquetes que tengan su repositorio asi:

```Python
pkg
├── ...
├── pkg
│   ├── __init__.py
│   ├── module1.py
│   └── subpkg
│       ├── __init__.py
│       └── module2.py
└── ...
```

En general, se recomuenda usar el source layout (y así lo hace el [Python Packaging Authority](https://packaging.python.org/en/latest/tutorials/packaging-projects/))

1. Para los devs que usan testing puede surgir el error deque se testea código que
no esta instalado.
2. Es mas prolijo.

#### 4.3.1. Package installation

Para que un paquete sea instalado necesita dos directorios:

1. `{package}`: un directorio con los source files del paquete (modulos, etc.).
2. `{package}-{version}.dist-info`: Un directorio que contiene información del
paquete, como metadata, licencias, un instalador, etc. Estos archivos se describen
en detalle en [PEP 427](https://peps.python.org/pep-0427/#the-dist-info-directory)

Cuando se instala un paquete utilizando `pip` los directorios que mencionamos arriba
se copian dentro de `site-packages/` en la instalación de la librería, es el lugar
por default que Python los va a buscar. La ubicación exacta de `site-packages/`
depende del sistema operativo, de como instalamos python y si estamos usando un
ambiente virtual. Podemos chequear el path usando `sys.path`.

Hay dos formas de hacer un *standar distribution (sdist)* una es comprimiendo el
archivo en la máquina del dev y el usuario solo lo tiene que descomprimir e instalar
y el otro es una manera mucho mas compleja que se utiliza cuando se quieren agregar
extensiones en otros lenguajes (normalmente C o C++). Un ejemplo de este segundo
tipo es numpy.

#### 4.3.3. Packaging tools

`poetry` es una versión simplificada de `setuptools`.

#### 4.3.4. Package repositories

El repositorio de PyPi solo hostea código de Python, el repositorio de conda
(yo nunca instale nada con `conda`) tambien puede guardar código que no sea de
Python. Normalmente voy a escribir código en Python nada mas.

`pip install` permite instalar paquetes directamente de un repo privado de GitHub
al que tenga acceso. Se puede instalar de un branch, commit o tag específcos.

`pip install git+https://github.com/TomasBeuzen/pycounts.git@v0.1.0`

## 5. Testing

### 5.5 Code coverage

#### 5.3.1. Unit tests

Hay limitaciones a la hora de comparar floats en unit tests.

`assert 0.1 + 0.2 == 0.3, "Numbers are not equal!"`

`AssertionError: Numbers are not equal!`

Cuando se trabaja con aproximaciones en lugar de valores exactos hay que usar
`pytest.approx()`.

```Python
import pytest
assert 0.1 + 0.2 == pytest.approx(0.3), "Numbers are not equal!"
```

Se puede aproximar el error con los parametros de la función `abs` y `rel`.

#### 5.3.4. Regression tests

Son test que se basan en que el resultado sea consistente y no en un resultado
específico. Esto es de especial utilidad cuando hay demasiados casos para hacer
un output esperado a mano, no le encuentro caso de uso específico para Tito pero
siento que puede ser de gran utilidad.

#### 5.5.2. Branch coverage

Mide la cantidad de branches, que se define a partir de la cantidad de caminos que
puede tomar el código (medido en condicionales).

coverage = branches executed / total branches * 100

[Documentation](https://coverage.readthedocs.io/en/latest/)

Hay otra medida mas que es

coverage = [lines executed + branches executed] / [total lines + total branches] * 100

## 6. Documentation

### 6.2 Writing documentation

#### 6.2.4 Changelog

Es un archivo que contiene el orden cronológico de los cambios hechos en el paquete.

Ejemplo

```Markdown
# Changelog

<!--next-version-placeholder-->

## v0.2.1 (12/09/2021)

### Fix

- Changed confusing error message in plotting.plot_words()

## v0.2.0 (10/09/2021)

### Feature

- Added a "stop_words" argument to pycounts.count_words()

### Documentation

- Added new usage examples
- Now hosting documentation on Read the Docs

## v0.1.0 (24/08/2021)

- First release of `pycounts`
```

## 7. Releasing and versioning

### 7.1. Version numbering

El versionamiento es el proceso de adjuntar identificadores unicos a cada versión
del paquete. EN la mayoría de los paquetes de Python se usa el semantic versioning.
Este tipo de versionado consiste de tres enteros A.B.C, donde A es el "major",
B es el "minor" y C es el "patch". La primer versión de un software normalmente
es la 0.1.0 e incrementa de ahí. Un incremento es un "bump" y consiste de sumar
1 a alguno de los 3 elementos:

- __patch__ release (0.1.0 -> 0.1.__1__): este tipo de realease son normalmente
fix de bugs retrocompatibles. La retrocompatibilidad implica que es compatible con
versiones previas. Por ejemplo, si paso de la 0.1.0 a la 0.1.1 no tendría que
reescribir nada del código porque todo debería seguir andando. Se puede tener todos
los que quiera, inclusive poner dos digitos (ejemplo: 0.1.27).
- __minor__ release (0.1.0 -> 0.__1__.0): un minor release incluye bug fixes grandes
o nuevas features que sean retrocompatibles, por ejemplo, agregar una nueva función.
Se puede tener todos
los que quiera, inclusive poner dos digitos (ejemplo: 0.13.27).
- __minor__ release (0.1.0 -> __1__.0.0): release 1.0.0 se utiliza para el primer
release estable del paquete. Despues de eso, las major realease se utilizan para
realizar cambios que no son retrocompatibles y pueden afectar a varios usuarios.
Los cambios que no son retorcompatibles se llaman "breaking changes". Por ejemplo:
cambiar el nombre de uno de los módulos en el paquete.

A pesar de las normativas expuestas el versionamiento del paquete puede ser un poco
subjetivo y requiere de juicio propio.

### 7.2 Version bumping

Esto es como incrementar la versión del paquete cuando estas preparando un nuevo
release. Este cambio puede ser manual o automático.

#### 7.2.1. Manual version bumping

Con `poetry` le tiramos un comando y se actualiza solo. Ejemplo:

`poetry version patch`

#### 7.2.2. Automatic version bumping

[Python Semantic Release (PSR)](https://python-semantic-release.readthedocs.io/en/latest/)
es una herramienta que te actualiza la versión de la librería según como escribas
el commit, basado en [Angular commit style](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commit-message-format),
te incrementa la versión de la librería automaticamente.

Ejemplo:

```git
<type>(optional scope): short summary in present tense

(optional body: explains motivation for the change)

(optional footer: note BREAKING CHANGES here, and issues to be closed)
```

Type se refiere a uno de estos:

- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- refactor: A code change that neither fixes a bug nor adds a feature
- perf: A code change that improves performance
- test: Adding missing or correcting existing tests
- chore: Changes to the build process or auxiliary tools and libraries such as documentation generation

Adicionalemnte hay un keyword `scope` que permite añadir contexto sobre el cambio.

Para usar PSR hay que instalarlo y configurarlo en el proyecto. Esto esta explicado
en el libro.

Cuando corremos `semantic-release version -v DEBUG` actualiza el numero de version
según los commits realizados e imprime información extra.

### 7.3. Checklist for releasing a new package version

#### 7.3.1. Step 1: make changes to package source files

Cuando haces esto normalmente trabajas con un branch y cuando estan okey todos los
cambios y pasaron los test mergeas el branch.

#### 7.3.2. Step 2: document your changes

Antes de largar los cambios tenemos que documentar todo en el changelog.

Si estamos usando git + psr tenemos que hacer el respectivo commit para que estos
cambios también impacten.

```git
git add CHANGELOG.md
git commit -m "build: preparing for release v0.2.0"
git push
```

#### 7.3.3. Step 3: bump version number

Una vez que los cambios para el nuevo release estan hechos hay que hacer un bump
a la versión del paquete con PSR.

Hacemos los commits según el formato especificado y luego:

```git
git add pyproject.toml poetry.lock
git commit -m "build: add PSR as dev dependency"
git push
```

Por último:

`semantic-release version`

Este paso automaticamente actualiza la version en pyproject.toml y crea un nuevo
tag para nuestro paquete, que lo podemos ver usando `git tag --list`

#### 7.3.4. Step 4: run tests and build documentation

No vamos a estar poniendo documentación online así que este paso no es necesario

#### 7.3.5. Step 5: tag a release with version control

Como ya discutimos anteriorimente, este proceso se basa en dos puntos:

1. Crear un tag especificando un punto en la historia del repositorio, usando el
comando `git tag`.
2. En GitHub, crear un release basado en el tag

Usando PSR para aumentar la version del paquete el paso 1 se hace automaticamente.

#### 7.3.6. Step 6: build and release package to PyPI

Como no publicamos en PyPI este paso lo saltemos.

### 7.4. Automating releases

Se vwe en el capítulo 8.

### 7.5. Breaking changes and deprecating package functionality

Podemos agregar un deprecation warning usando el `warning` module de Python.

Algunas consideraciones antes de hacer breaking changes:

- Si se cambia una versión significativamente, esta bueno dejar ambas por un tiempo
(con un deprecation warning) para hacer una mejor transición.
- Si voy a deprecar un montón de código, hacerlo en pequeños releases.
- Si el breaking change es por una dependencia que cambia, es mejor primero largar
un warning para avisar que inmediatamente hacerlo una dependencia.

### 7.6. Updating dependency versions

El comando `poetry update` se puede usar para updatear las dependencias instaladas
en el ambiente virtual (pyproject.toml). Esto es útil para testear que las nuevas
versiones funcionan como es esperable.

`poetry update matplotlib`

Pero, `poetry update` no va a cambiar lo definicido como versiones requeridas en
`pyproject.toml`, para hacerlo hay dos opciones:

1. Modificar manualmente `pyproject.toml`
2. Usar `poetry add`. `poetry add "matplotlib>=3.5.0"`.
