import click

from markdrip.mods import generator as gen

@click.command()
@click.option("--output", default="./", help="Output destination file path")
@click.option("--theme", default="github", help="Applicable CSS file name. Does not include extension.")

@click.argument("target")
def main(target, theme, output):

    mkup, filename = gen.markup(target)
    css = gen.load_css(theme)
    if css != "\\[ERROR]/":
        if output == "./":
            output = filename + ".html"
        print(target, output, theme)
        gen.rendor(mkup, css, output)



if __name__ == "__main__":
    main()
