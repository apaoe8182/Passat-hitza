# Passat-hitza

Este repositorio contiene una versión modificada del software [Passat](https://github.com/HynekPetrak/Passat.git) para la generación de gráficos a partir de la información conseguida por la app.

## Installation

```
git clone https://github.com/apaoe8182/Passat-hitza.git
```
Tested with Python 3.10.12

### Requirements

With pip on any system:

```
pip install -r requirements.txt
```

## Usage 

```
# ./passat.py -h
usage: passat.py [-h] [-v] [-f] [--no-categories] [-c CATEGORIES] [input_file [input_file ...]]

Audit password quality v1.7

positional arguments:
  input_file            input file names, one password per line. If ommited, read from stdin

options:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -f, --freq            run frequency analysis for characters used
  --no-categories       don't perform fuzzy categorization, improves performance
  -c CATEGORIES, --categories CATEGORIES
                        json file with password categories for fuzzy matching, defaults to
                        categories.json
  -o OUTPUT, --output OUTPUT
                        output path for the charts. Default: ./images

```

## License

MIT
