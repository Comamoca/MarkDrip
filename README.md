# Markdrip

MarkDrip is a simple HTML generator.
Mistletoe is used for rendering.

The site is [here](https://comamoca.github.io/markdrip.github.io/) even in the rendered result.

## How to use

`markdrip filename`

### Options

Run `markdrip --help`.

```
Usage: main.py [OPTIONS] TARGET

Options:
  --output TEXT  Output destination file path
  --theme TEXT   Applicable CSS file name. Does not include extension.
  --help         Show this message and exit.

```

## Custom CSS

CSS is stored under `~ / .markdrip`.
Note that when writing CSS, specify the tag name directly in the selector.

Ex.)
```
h1, h2, h3, h4, h5 {
	color: black
}
```
