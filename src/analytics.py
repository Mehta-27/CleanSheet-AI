import os
import streamlit as st
import streamlit.components.v1 as components

GTAG_ID = "G-M5QRG84BS9"

GTAG_CODE = f"""<!-- Google tag (gtag.js) -->
<script id="google-tag-manager" async src="https://www.googletagmanager.com/gtag/js?id={GTAG_ID}"></script>
<script id="google-tag-config">
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GTAG_ID}');
</script>"""

FALLBACK_JS = f"""
<script>
try {{
    const parentDoc = window.parent.document;
    if (!parentDoc.getElementById('google-tag-manager')) {{
        const script1 = parentDoc.createElement('script');
        script1.id = 'google-tag-manager';
        script1.async = true;
        script1.src = 'https://www.googletagmanager.com/gtag/js?id={GTAG_ID}';
        parentDoc.head.insertBefore(script1, parentDoc.head.firstChild);

        const script2 = parentDoc.createElement('script');
        script2.id = 'google-tag-config';
        script2.innerHTML = `
            window.dataLayer = window.dataLayer || [];
            function gtag(){{window.dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{GTAG_ID}');
        `;
        parentDoc.head.insertBefore(script2, script1.nextSibling);
    }}
}} catch (e) {{
    console.warn("Could not inject Google Tag to parent head due to security sandbox restriction:", e);
}}
</script>
"""

def inject_google_tag() -> None:
    """Inject Google Tag (gtag.js) tracking code into the page head.
    
    Tries programmatically patching the underlying Streamlit static/index.html file first.
    If patching fails due to permission restrictions or filesystem constraints, falls back
    to an iframe component that injects the script tag directly to window.parent.document.
    """
    patch_success = False
    try:
        streamlit_dir = os.path.dirname(st.__file__)
        index_path = os.path.join(streamlit_dir, "static", "index.html")
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            if GTAG_ID not in content:
                # Find <head> tag and insert immediately after it
                head_tag = "<head>"
                if head_tag in content:
                    new_content = content.replace(head_tag, f"{head_tag}\n{GTAG_CODE}", 1)
                    with open(index_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    patch_success = True
            else:
                patch_success = True
    except Exception:
        # Gracefully handle write permission errors or missing file errors
        pass
        
    # If static index.html patching failed, use the iframe escape fallback
    if not patch_success:
        components.html(FALLBACK_JS, height=0, width=0)
