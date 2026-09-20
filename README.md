# Sonora

Landing de la propuesta de valor: una plataforma de streaming donde cada
reproducción le paga al artista en el momento, sin pozo común y sin meses
de espera.

Es material de promoción. No describe implementación, arquitectura ni
contratos: solo el problema, el flujo y el modelo de negocio.

## Estructura

    index.html        la landing publicada, sin dependencias ni build
    demo/             el sitio como quedará, generado — no se edita a mano
    demo/parts/       lo que solo existe en la demo
    tools/demo.py     regenera demo/ desde index.html

Se abre directamente en el navegador o se publica como sitio estático.
GitHub Pages despliega solo en cada push a `main`.

## Antes de publicar un cambio en la landing

    python3 tools/demo.py --check

Si falla, la demo quedó atrás: `python3 tools/demo.py` y se incluye en el
mismo commit.

## El formulario

No hay backend: el formulario avisa que el canal no está activo y no
guarda ni transmite nada. Para conectarlo, se le pone la URL a `ENDPOINT`
al tope del script en `index.html`; con eso hace un POST real y confirma
el envío.
