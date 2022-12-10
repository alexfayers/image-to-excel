# image-to-excel

An epic projected called image_to_excel, by alexfayers!

## Installation

To install the project you only need to clone the repo and run pip install within the repo folder:

```bash
pip install .
```

If you like using virtual environments, you can easily install the project within one using [pipx](https://pypa.github.io/pipx/):

```bash
pipx install .
```

## Usage

You can use image-to-excel as an importable module:

```py
from image_to_excel import BaseClass

app = BaseClass("config.yml")

app.logger.info(
    f"Hi, welcome to {app.config.INFO.NAME} by {app.config.INFO.AUTHOR}!"
)
```

Or as a command line interface:

```bash
$ python3 -m image_to_excel
# or
$ image_to_excel
```

## Documentation

Documentation for image-to-excel can be found within the docs folder.
