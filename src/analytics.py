import streamlit as st
import streamlit.components.v1 as components

GA_ID = "G-M5QRG84BS9"

GA_HTML = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>"""


def inject_google_tag() -> None:
    components.html(GA_HTML, height=0, width=0)
