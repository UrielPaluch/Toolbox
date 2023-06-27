# Bienvenido a la documentacion de Toolbox

## Status

[![Testing-Toolbox](https://github.com/UrielPaluch/Toolbox/actions/workflows/github-actions-testing.yml/badge.svg)](https://github.com/UrielPaluch/Toolbox/actions/workflows/github-actions-testing.yml)

## Overview

*Toolbox* es una libreria creada con el objetivo de interactuar con los algoritmos
desarrollados.

Esta diseñada para evitar la repetición de código bajo el lema DRY (Don't Repeat
Yourself).

## Instalacion

*Toolbox* es un repositorio privado y solo se puede instalar teniendo acceso al
mismo.

```Python
pip install git+https://github.com/UrielPaluch/Toolbox.git
```

## Dependencias

## Features

Esta seccion describe las funcionalidades y los componentes de la librería

### Functions

#### Toolbox

* **get_feriados_byma** : devuelve una lista con todos los feriados de Byma.
* **calculo_plazo_liquidacion_24hs** : devuelve el proximo plazo de liquidacion para 24hs.
* **calculo_plazo_liquidacion_48hs** : devuelve el proximo plazo de liquidacion para 48hs.
* **hay_mercado** : devuelve si hay mercado.
* **extract_price_size_values** : del dict con informacion del mercado extrae
el precio y la cantidad.
* **extract_market_ticker_values** : del dict con informacion del mercado extrae
el ticker y el mercado (CI, 24hs o 48hs).

#### logging_module

Modulo de logging.

* **my_logger** : inicializa el logger.
* **logging** : expone todas las funcionalidades del modulo de logging de Python.

### Author/Mainteiner

[Uriel Paluch](https://github.com/UrielPaluch)
