# Python Tools for Managing Virtual Environments

Este documento surge de la necesidad de entender mejor que son las ambientes virtuales,
necesarios para la creación de Toolbox y, probablemente, muy utiles en próximos
desarrollos.

## Que herramienta elegir

Hay varias herramientas para armar un entorno virtual, en base a [esta](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe) pregunta
en stack overflow arme el siguiente resumen:

En principio hay que arrancar con `virtualenv`. Este [video](https://www.youtube.com/watch?v=TNtrAvNNxTY)
es un buen resumen.

`pyenv` se usa para isolar distintas versiones de Python.

`pyenv-virtualenv` es un combinación de `pyenv` y `virtualenv`.

## Como usarlo

1. `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
2. `virutalenv -p python3 env`
3. `./env/Scripts/activate`

## Como se va a usar

La verdad es que no le encuentro mucha utilidad mas que tener un entorno separado para desarrollo.
