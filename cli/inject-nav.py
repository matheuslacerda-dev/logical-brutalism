import os
import re

CSS = """
<style>
/* LOGICAL BRUTALISM: NAV HEADER */
.lb-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid var(--color-surface, #1E1E1E);
  padding: 24px;
  font-family: var(--font-code, 'JetBrains Mono', monospace);
  text-transform: uppercase;
  background: var(--color-void, #0A0A0A);
}
.lb-nav-logo {
  color: var(--color-white, #F0F0F0);
  font-weight: bold;
  text-decoration: none;
  font-size: 1rem;
}
.lb-nav-links {
  display: flex;
  gap: 2rem;
}
.lb-nav-link {
  color: var(--color-text, #888888);
  text-decoration: none;
  transition: none !important;
  font-size: 0.875rem;
  font-weight: 600;
}
/* AXIOMA P-06 E ANTI-SHIFT: BRACKETS TRANSPARENTES */
.lb-nav-link::before { content: "[ "; color: transparent; }
.lb-nav-link::after { content: " ]"; color: transparent; }
.lb-nav-link:hover { color: var(--color-amber, #FFB000); }
.lb-nav-link:hover::before, .lb-nav-link.active::before { color: var(--color-amber, #FFB000); }
.lb-nav-link:hover::after, .lb-nav-link.active::after { color: var(--color-amber, #FFB000); }
.lb-nav-link.active { color: var(--color-amber, #FFB000); }

/* Para suprimir anomalias do layout global do Tailwind (no market-comparison.html) */
nav.lb-nav { width: 100%; box-sizing: border-box; }
</style>
"""

def get_nav(is_root, active_idx):
    prefix = "./" if is_root else "../"
    links = [
        ("DOCUMENTO VIVO", f"{prefix}index.html"),
        ("UI COMPONENTS", f"{prefix}showcase/components.html"),
        ("DATA DENSITY", f"{prefix}showcase/data-components.html"),
        ("MERCADO", f"{prefix}showcase/market-comparison.html"),
        ("TESTE CEGO", f"{prefix}showcase/showcase-blind-test.html"),
    ]
    html = f'{CSS}\n<nav class="lb-nav">\n  <a href="{prefix}index.html" class="lb-nav-logo">BRUTALISMO_LÓGICO</a>\n  <div class="lb-nav-links">\n'
    for i, (name, path) in enumerate(links):
        cls = "lb-nav-link active" if i == active_idx else "lb-nav-link"
        html += f'    <a href="{path}" class="{cls}">{name}</a>\n'
    html += '  </div>\n</nav>\n'
    return html

files = [
    ("index.html", True, 0),
    ("showcase/components.html", False, 1),
    ("showcase/data-components.html", False, 2),
    ("showcase/market-comparison.html", False, 3),
    ("showcase/showcase-blind-test.html", False, 4)
]

for filepath, is_root, active_idx in files:
    full_path = os.path.join("d:/PROJETOS/logical-brutalism", filepath)
    if not os.path.exists(full_path):
        continue
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Prevenir dupla injeção
    if "lb-nav-logo" in content:
        continue

    nav_html = get_nav(is_root, active_idx)
    new_content = re.sub(r'(<body[^>]*>)', r'\1\n' + nav_html, content, count=1)
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Injetado: {filepath}")
