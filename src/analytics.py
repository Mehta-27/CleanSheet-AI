import os

import streamlit as st
import streamlit.components.v1 as components

GTAG_ID = "G-M5QRG84BS9"

GTAG_CODE = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GTAG_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GTAG_ID}');
</script>"""


def inject_google_tag() -> None:
    """Inject Google Analytics tag into the Streamlit app.

    First tries to patch the static index.html for proper GA tracking.
    Falls back to components.html() if static patching fails.
    """
    try:
        # Try to find and patch Streamlit's static index.html
        st_dir = os.path.dirname(st.__file__)
        index_path = os.path.join(st_dir, "static", "index.html")

        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                html = f.read()

            if GTAG_ID not in html:
                html = html.replace("<head>", f"<head>{GTAG_CODE}", 1)
                with open(index_path, "w", encoding="utf-8") as f:
                    f.write(html)
            return
    except Exception:
        pass

    # Fallback: inject via Streamlit component (invisible iframe)
    components.html(GTAG_CODE, height=0, width=0)
