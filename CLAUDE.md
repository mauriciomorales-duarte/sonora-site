# sonora-site

Landing pública de la propuesta de valor de Sonora.

## Qué es y qué no es

Es promoción dirigida a artistas, oyentes y posibles socios. Habla del
problema, del flujo y de cómo se sostiene el negocio.

**Deliberadamente no menciona contratos, tokens, billeteras, redes ni nada
técnico.** Esa parte se analiza aparte y en privado; mezclarla aquí
confunde al lector al que este sitio le habla y expone decisiones que
todavía no están tomadas. Si una edición futura quiere agregar esa capa,
es un cambio de alcance, no un detalle.

## Forma

Un solo `index.html` sin dependencias ni build. Los colores son tokens en
`:root` con su variante clara bajo `prefers-color-scheme`. Se publica como
sitio estático.

El único JavaScript es el del formulario de contacto, y solo para
interceptar el envío.

## El formulario no envía, y lo dice

No hay backend ni dirección de correo publicada. Al enviar, el formulario
le avisa a la persona que el canal todavía no está activo y que no se
guardó nada — porque es cierto: no se almacena ni se transmite nada.

Esa honestidad no es un placeholder que se borra: un formulario que recoge
datos y los tira sin avisar quema el contacto de alguien que quiso
escribir. Cuando haya dominio y buzón, se conecta el envío y el aviso se
reemplaza por una confirmación real.

## Cifras

Las que aparecen son referenciales y provienen de reportes públicos de
artistas, y el pie del sitio lo dice. Cualquier cifra nueva entra con la
misma regla: verificable o no entra.
