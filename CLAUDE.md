# sonora-site

Landing pública de la propuesta de valor de Sonora, más una demo privada
del sitio tal como quedará cuando el contacto esté conectado.

## Qué es y qué no es

Es promoción dirigida a artistas, oyentes y posibles socios. Habla del
problema, del flujo y de cómo se sostiene el negocio.

**Deliberadamente no menciona contratos, tokens, billeteras, redes ni nada
técnico.** Esa parte se analiza aparte y en privado; mezclarla aquí
confunde al lector al que este sitio le habla y expone decisiones que
todavía no están tomadas. Si una edición futura quiere agregar esa capa,
es un cambio de alcance, no un detalle.

## Quién decide

El fundador es el dueño del proyecto y responde por su continuidad: el
contenido, las cifras, el dominio y qué se publica son decisiones suyas.
El desarrollo lo hace hoy un asesor externo, que no forma parte del equipo
y no participa del negocio.

Ese asesor custodia temporalmente los accesos — cuenta de GitHub, llave de
deploy y dominio — y **se rotan al momento de la entrega**, no después. Ni
esas credenciales ni ninguna otra se escriben aquí: este archivo viaja a
GitHub en cada push.

## Forma

`index.html` es la landing entera, sin dependencias ni build. Los colores
son tokens en `:root` con su variante clara bajo `prefers-color-scheme`.
Se publica como sitio estático en GitHub Pages, que despliega solo en cada
push a `main`; el repositorio no tiene workflows propios.

El único JavaScript es el del formulario de contacto.

## El formulario no envía, y lo dice

No hay backend ni dirección de correo publicada. El formulario valida
nombre y correo, marca el campo que falta y, al enviar, avisa que el canal
todavía no está activo y que no se guardó nada — porque es cierto: no se
almacena ni se transmite nada.

Esa honestidad no es un placeholder que se borra: un formulario que recoge
datos y los tira sin avisar quema el contacto de alguien que quiso
escribir.

**Conectarlo es una línea.** `ENDPOINT`, al tope del script, está vacío;
mientras lo esté, `enviar()` rechaza con `sin-canal` y la página dice la
verdad. Con una URL adentro, el formulario hace un POST real y el éxito
pasa a ser una confirmación honesta. No hay nada más que tocar.

## La demo vive aparte, y por eso está duplicada

`demo/` es el sitio como quedará: el formulario recorre el envío completo
hasta "Enviado exitosamente" sin red, con `ENDPOINT` en `"demo"`. Es
material para enseñar, lleva `noindex` y no se enlaza desde la landing.

**Está separada a propósito.** Unificarlas detrás de un parámetro pondría
el camino de éxito simulado dentro de la página pública, donde bastaría un
query para que un visitante real viera una confirmación falsa. El archivo
aparte es lo que garantiza que eso no pueda pasar.

Pero no se edita a mano: **`demo/index.html` se genera.**

    python3 tools/demo.py            # regenera la demo desde la landing
    python3 tools/demo.py --check    # falla si quedó desincronizada

La fuente es `index.html`. Lo propio de la demo vive en `demo/parts/`
(`equipo.css`, `equipo.html`) y el generador lo inyecta junto con el
`noindex` y el envío simulado. Un cambio en la landing se propaga
corriendo el script; una edición directa sobre `demo/index.html` se pierde
en la siguiente corrida. Si una ancla del generador desaparece de
`index.html`, falla en vez de escribir una demo rota.

## La foto del equipo es de referencia

El retrato de la sección Equipo es una imagen de archivo y está ahí para
mostrar el diseño, no a la persona. **Por eso la sección existe solo en la
demo.** Pasa a la landing cuando haya foto real, y en el mismo cambio —
publicar la cara de un modelo de archivo como fundador de un proyecto que
busca socios es exactamente lo que este sitio no puede hacer.

Los enlaces a redes no existen todavía y no se inventan.

## Cifras

Las que aparecen son referenciales y provienen de reportes públicos de
artistas, y el pie del sitio lo dice. Cualquier cifra nueva entra con la
misma regla: verificable o no entra.
