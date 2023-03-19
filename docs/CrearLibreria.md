# Como crear una libreria

El objetivo de este documento es dejar por sentado como se crea la libreria.

Lo hice basandome en este [post](https://towardsdatascience.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893)
de Towards Data Science y en la librería [pyRofex](https://github.com/matbarofex/pyRofex).

## Crear un ambiente virtual

El primer paso es crear un virtual enviroment con

```Python
python3 -m venv venv
```

El ambiente virtual sirve para manejar multiples dependencias. Lo correcto sería
que yo trabaje con entornos virtuales en todos mis desarrollos.

Esto crea una carpeta `venv/` que hay que agregar al `.gitignore`.

## Setup.py

Cada vez que yo modifico la versión (entiendase modificar como subir o bajar la
versión), es decir, cada vez que la versión instalada es distinta a la que esta en
GitHub, esta se instala.

```Python
pip install git+https://github.com/UrielPaluch/Toolbox.git
```
