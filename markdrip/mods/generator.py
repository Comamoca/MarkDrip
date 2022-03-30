import os
import pathlib

import mistletoe
from jinja2 import Template
base = os.path.dirname(os.path.abspath(__file__))

CSS_DIR = os.path.normpath(os.path.join(base, '../css/'))
CUSTOM_CSS_DIR = pathlib.Path().home() / pathlib.Path(".markdrip")
BASE_DIR = os.path.normpath(os.path.join(base, '../templete/'))

def markup(filepath):
    filepath = pathlib.Path(filepath)
    filename = filepath.stem
    with open(filepath) as f:
        text = f.read()

    mkup = mistletoe.markdown(text)
    return (mkup, filename)


def load_css(css_name):

    load_path = CSS_DIR / pathlib.Path(css_name).with_suffix(".css")
    if load_path.exists() == True:
        print("load_path(CSS) ==> " + str(load_path))
        with open(load_path) as css_file:
            css = css_file.read()
        return css

    load_path = (CUSTOM_CSS_DIR / pathlib.Path(css_name).with_suffix(".css"))
    if load_path.exists() == True:
        print("load_path ==> " + str(load_path.resolve()))
        with open(load_path) as css_file:
            css = css_file.read()
        return css
    print("EROOR")
    print("Not Found Theme")
    print("Theme Name ==> " + css_name + "(.css)")
    return "\\[ERROR]/"



def rendor(html, css, filename=None, basename="base.html"):
    #print(filename)
    if (BASE_DIR / pathlib.Path(basename)).exists() == True:
        print("Base Template ==> " + str(BASE_DIR / pathlib.Path(basename)))
        with open(BASE_DIR / pathlib.Path(basename)) as tmpl:
            templete = tmpl.read()

        templete = Template(templete)
        data = {"content": html, "style": css, "filename": filename}
        result = templete.render(data)

        path = pathlib.Path(filename).resolve()

        with open(path, "w") as f:
            print("write ==> " + str(path))
            f.write(result)
    else:
        print("EROOR")
        print("Not Found Templete")
        print("Theme Templete ==> " + basename + "(.html)")
