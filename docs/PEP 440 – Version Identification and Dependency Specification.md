# PEP 440 – Version Identification and Dependency Specification

El documento es un resumen de [PEP 440](https://peps.python.org/pep-0440/)

## Definitions

"Projects" son componentes de software disponibles para la integracion. Esto incluye
librerias, frameworks, scripts, pluguins, aplicaciones y las distintas combinaciones
que puedan surgir de estos se registran tipicamente en Python Package Index (pypi).

"Releases" son únicos identificadores de un snapshot de un proyecto.

"Distributions" son los archivos del paquete que se publican y distribuyen un release.

"Build Tools" son herramientas automatizadas para correr en el CI produciendo el
código necesario para que sea distribuido como un sdists (Source Distribution).

"Index Servers" are active distribution registries which publish version and
dependency metadata and place constraints on the permitted metadata.

"Publication tools" son herramientas automaticas para subir los sdists a los index
servers.

"Installation tools" son herramientas de integración destinadas al deploy del usuario

"Automated tools" es un termino abarcativo que incluye build tools, index servers,
publication tools, integration tools y cualquier otro software para la distribucion
del paquete.

## Version scheme

Las distributions se identifican con un public version identifier. Este también
se utiliza para poder determinar las dependencias relacionadas con esa versión.

### Public version identifiers

Los identificadores canonicos DEBEN cumplir con el siguiente esquema

```Python
[N!]N(.N)*[{a|b|rc}N][.postN][.devN]
```

Los identificadores públicos de version NO DEBEN incluir espacios.

Los identificadores públic de versión DEBEN ser únicos.

Las herramientas de instalación DEBEN ignorar cualquier versión pública que no
cumpla con el esquema previamente mencionado pero DEBE incluir las normalizaciones
especificadas debajo. Las herramientas de instalación DEBEN alertar al usuario
cuando hay versiones ambiguas detectadas o no se completo la instalación exitosamente.

Ver Appendix B : Parsing version strings with regular expressions

Los identificadores públicos de versión se separan en 5 segmentos:

- Epoch segment: `N!`
- Release segment: `N(.N)*`
- Pre-release segment: `{a|b|rc}N`
- Post-release segment: `.postN`
- Development release segment: `.devN`

Cualquier release debe ser “final release”, “pre-release”, “post-release” o
“developmental release”, según como se define en la siguiente sección.

Todos los componentes numéricos DEBEN ser enteros no negativos.

Todos los componentes DEBEN ser intepretados y ordenados de acuerdo a su valor
numérico, no como texto.

Todos los componentes numéricos PUEDEN ser zero. Excepto como se describe debajo
para las release, un cero no tiene significado especial ademas de ser el número
mas bajo posible en el versionado.

### Local version identifiers

Local version identifiers DEBEN cumplir con el siguiente esquema

```Python
<public version identifier>[+<local version label>]
```

Consiste de un public version identifier normal (como se definió en la sección
anterior), sumado con un "local versionm label" arbitrario, separado del public
version identifier con un mas. Los local version labels no tienen una especificacion
semantica pero tienen algunas restricciones semanticas.

Se utilizan para marcar los cambios-

Para asegurar la consistencia del formato solo esta permitido los siguientes
caracteres:

- ASCII letters ([a-zA-Z])
- ASCII digits ([0-9])
- periods (.)

Yo voy a seguir con el esquema de "issue/xx".

Las versiones locales deben empezar y terminar con un número o letra ASCII.

Para comparar y ordenar las versiones locales, considera cada segmento de la version
local (dividida por `.`) por separado. Si un segmento solo consiste de numeros
entonces esa seccion debe ser considerada un número (sin los .) para motivos de
comapración y si contiene letras el segmento se comapra lexicograficamente con
case sensitive.
Cuando se comparan un segmento numérico y otro lexicografico, el numérico siempre
es mayor.
Adicionalmente, una local version con un gran número de segmentos siempre va a ser
mayor que una local con menos segmentos siempre que sean la misma version.

Un "upstream project" es un proyecto que define sus propias versiones publicas.
Un "downstream project" es uno que trackea y redistribuye un upstream project,
potencialmente haciendo checks de seguridad y arreglo de bugs de la última versión
del upstream project.

Local version identifiers NO DEBEN utilizarse cuando se publica un upstream project
a un public server index, pero PUEDEN ser utilizados para identificar builds privados
creados directamente del source del proyecto.

### Final releases

Una versión que solo consiste de un release y, opcionalmente, un epoch es llamada
"final release".

Un release consiste en uno o mas enteros no negativos separados por puntos:

```Python
N(.N)*
```

Las final release de un proyecto DEBEN ser numeradas en forma consistente de manera
ascendete, de esta forma las herramientas automatizadas van a poder upgredear
corrctamente.

Mientras que cualquier variante es aceptada, es recomendable usar alguna de estas
dos variables “major.minor” o “major.minor.micro”. Por ejemplo:

```Python
0.9
0.9.1
0.9.2
...
0.9.10
0.9.11
1.0
1.0.1
1.1
2.0
2.0.1
...
```

Una serie de release es cualquier set de final release que comienzan con el mismo
prefijo. Por ejemplo, `3.3.1,` `3.3.5` y `3.3.9.45` son todas partes del release
`3.3`

Nota: `X.Y` y `X.Y.0` no son consideradas releases distintos, porque la herramienta
que compara los release expande `X.Y` a `X.Y.0` y luego las compara.

Los date based realase segments tambien están permitidos. Un ejemplo es usando el
año y el mes.

```Python
2012.4
2012.7
2012.10
2013.1
2013.6
...
```

### Pre-release

Algunos proyectos utilizan "alpha, beta, release candidate" pre-release cycle para
que los usuarios lo testeen antes de tener un final release. Ejemplo:

```Python
X.YaN   # Alpha release
X.YbN   # Beta release
X.YrcN  # Release Candidate
X.Y     # Final release
```

El pre-release consiste de un identificador alfanumérico (fase) junto con un entero
no negativo. Primero se ordenan por fase y luego por el componente numérico.

Utilizar `c` o `rc` es equivalente para indicar una version de release. Las herramientas
de instalación DEBEN interpretarlo así.

Las build tools DEBEN desabilitar la creación de dos versiones una con `c` y otra
con `rc`.

### Post-releases

Algunos proyectos utilizan post-releases para corregir errores menores en la final
release que no afectan el software (por ejemplo, corregir un error en las release
notes).

Estas post release se indican agregando un post-release segment en el version
identifier:

```Python
X.Y.postN    # Post-release
```

Nota: El uso de pust-release para solucionar bugs esta fuertemente desaconsejado.

Los post-release también estan permitidos en las pre-releases:

```Python
X.YaN.postM   # Post-release of an alpha release
X.YbN.postM   # Post-release of a beta release
X.YrcN.postM  # Post-release of a release candidate
```

Pero esto esta fuertemente desaconsejado.

### Developmental releases

Estos se indican con un devN

```Python
X.Y.devN    # Developmental release
```

Se pueden integrar con los mencionados anteriormente pero esta fuertemente desaconsejado.

### Version epochs

Si esta incluido en un version identifier, el epoch aparece antes que todos los
otros componentes, seperado por un signo de admiración.

```Python
E!X.Y  # Version identifier with epoch
```

Si no se aclara ninguno, por default es `0`.

Esto se utiliza cuando se cambia la forma en que se indentifican las versiones.

Supongamos que cambiamos de una identificación basada en fechas a una semántica
(como `10.0`), las nuevas release se van a identificar como mas antiguas ya que
seria el año 10. El esquema quedaría de la siguiente manera:

```Python
1.0
1.1
2.0
2013.10
2014.04
```

Pero si especificamos un epoch, se pueden ordenar apropiadamente.

```Python
2013.10
2014.04
1!1.0
1!1.1
1!2.0
```

## Version Specifiers

Una especificación de versión consiste en una serie de clausulas separadas por comas,
por ejemplo:

```Python
~= 0.9, >= 1.0, != 1.3.4.*, < 2.0
```

El operador utilizado para comparar determina el tipo de versión para la clausula:

- `~=`: Compatible release
- `==`: Version matching
- `!=`: Version exclusion
- `<=`, `>=`: Inclusive ordered comparison
- `<`, `>`: Exclusive ordered comparison
- `===`: Arbitrary equality

La coma `,` es como tener un operador lógico **and**.

Hay explicaciones de cada una pero no me parece relevante.
