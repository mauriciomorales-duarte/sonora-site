#!/usr/bin/env python3
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "index.html"
SALIDA = RAIZ / "demo" / "index.html"
PARTES = RAIZ / "demo" / "parts"


def inserta(html, ancla, bloque, despues):
    if ancla not in html:
        sys.exit(f"ancla ausente en index.html: {ancla!r}")
    return html.replace(ancla, ancla + bloque if despues else bloque + ancla, 1)


def sustituye(html, viejo, nuevo):
    if viejo not in html:
        sys.exit(f"ancla ausente en index.html: {viejo!r}")
    return html.replace(viejo, nuevo, 1)


def genera():
    html = FUENTE.read_text()

    html = sustituye(
        html,
        "<title>Sonora</title>",
        '<meta name="robots" content="noindex, nofollow">\n<title>Sonora · demo</title>',
    )
    html = inserta(
        html,
        "\nfooter{border-top",
        "\n" + (PARTES / "equipo.css").read_text(),
        despues=False,
    )
    html = inserta(
        html,
        '    <a href="#riesgos">Riesgos</a>\n',
        '    <a href="#equipo">Equipo</a>\n',
        despues=True,
    )
    html = inserta(
        html,
        '<section id="contacto">',
        (PARTES / "equipo.html").read_text() + "\n",
        despues=False,
    )
    html = sustituye(html, 'var ENDPOINT = "";', 'var ENDPOINT = "demo";')
    html = inserta(
        html,
        '    if (!ENDPOINT) return Promise.reject(new Error("sin-canal"));\n',
        '    if (ENDPOINT === "demo") {\n'
        "      return new Promise(function (listo) { setTimeout(listo, 900); });\n"
        "    }\n",
        despues=True,
    )
    return html


if __name__ == "__main__":
    nuevo = genera()
    if "--check" in sys.argv:
        actual = SALIDA.read_text() if SALIDA.exists() else ""
        if actual != nuevo:
            sys.exit("demo/index.html no coincide con index.html: corre tools/demo.py")
        print("demo al dia")
    else:
        SALIDA.write_text(nuevo)
        print(f"escrito {SALIDA.relative_to(RAIZ)}")
