# Fonts

The live site uses:

1. **Libre Baskerville** — Google Fonts (loaded in `typography.css`)
2. **freight-text-pro** — Adobe Fonts via the site owner’s Typekit kit

For HTML previews that match annahellmuth.com, include the Typekit loader in your page `<head>` (same as the live site):

```html
<link rel="preconnect" href="https://use.typekit.net" crossorigin />
<script src="https://use.typekit.net/ik/r0p1MYsmR1L75nvVsqVUB5iMYX6V0yf3aSvQ_zx_uSGfe7SIfFHN4UJLFRbh52jhWDjDwRbtwewoFc9DZRj3FQStwQsqwRsRwy79MkG0jAFu-WsoShFGZAsude80ZkoRdhXCHKoyjamTiY8Djhy8ZYmC-Ao1Oco8if37OcBDOcu8OfG0ZcUzihmkOANRZAUzifXkZRJkO1FUiABkZWF3jAF8OcFzdP37O1FUiABkZWF3jAF8ShFGZAsude80ZkoRdhXCjAFu-WsoShFGZAsude80ZkoRdhXCjAFu-WsoShFGZAsude80Zko0ZWbCjAo0jAy8deUliWsGOcFzdPUySkolZPUcdeNaZWJldhF8deNXOQ4cwRJ0SaBujW48Sagyjh90jhNlOeUzjhBC-eNDifUDSWmyScmDSeBRZWFR-emqiAUTdcS0jhNlOYiaikoyjamTiY8Djhy8ZYmC-Ao1OcFzdPUaiaS0jAFu-WsoShFGZAsude80Zko0ZWbCiaiaOcB0dcBGZAUCdWmX-foRdhXCiaiaOcBDOcu8OYiaikocdeNaZWJldhF8deNXOQ4cwRJ0SaBujW48Sagyjh90jhNlOYiaikoDSWmyScmDSeBRZWFR-emqiAUTdcS0jhNlJ6ol-Ao8S1ZyOAuzZemkdKJbZ148-AiGifuXZWyXOWgkdkG4fO9nIMMjgfMfH6qJceqbMs6IJMJ7fbK6-sMgeMj6MKG4f4TTIMIjgkMfH6qJcAqbMs65JMJ7fbKd-sMgegI6MTMg7H2ET6j.js" async></script>
<script>try{Typekit.load();}catch(e){}</script>
```

If Typekit is unavailable, `typography.css` falls back to Georgia — close for layout checks, not identical to the live site.

To self-host licensed fonts later, add files here and update `--font-body` in `tokens.css`.
