import os
import glob
import re

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))

OLD_CSS = """        body { background-color: var(--bg-light); font-family: 'Inter', sans-serif; display: flex; height: 100vh; overflow: hidden; }
        
        .sidebar { width: 260px; background: var(--sidebar-bg); color: #cbd5e1; display: flex; flex-direction: column; flex-shrink: 0; }
        .sidebar-header { padding: 20px; font-size: 1.25rem; font-weight: bold; color: white; border-bottom: 1px solid rgba(255,255,255,0.1); }
        .sidebar-nav { flex: 1; overflow-y: auto; padding: 15px 0; }
        .nav-category { padding: 15px 20px 5px; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #64748b; font-weight: bold; }
        .sidebar a { color: #cbd5e1; text-decoration: none; padding: 10px 20px; display: flex; align-items: center; gap: 10px; font-size: 0.9rem; transition: 0.2s; }
        .sidebar a:hover, .sidebar a.active { background: var(--sidebar-hover); color: white; border-left: 4px solid var(--primary-accent); padding-left: 16px; }
        .sidebar-footer { padding: 15px 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.85rem; }

        .main-wrapper { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
        .topbar { height: 60px; background: white; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; flex-shrink: 0; }
        .main-content { flex: 1; overflow-y: auto; padding: 24px; }"""

import sys

for path in files:
    filename = os.path.basename(path)
    if filename in ["update_terms.py", "replace_layout.py", "undo_layout.py"]:
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # REMOVE THE APP-LAYOUT WRAPPER
    if '<div class="app-layout">' in content:
        # replace the exact wrapper start
        content = content.replace('<body>\n    <div class="app-layout">', '<body>')
        content = content.replace('<body>\n    <div class=\"app-layout\">', '<body>')
        content = content.replace('<div class="app-layout">', '')
        # now finding the closing </div>
        # My script put closing </div> right before the first script loading bootstrap or right before </body>
        script_idx = content.rfind('<script src="https://cdn.jsdelivr.net/npm/bootstrap')
        if script_idx != -1:
            div_idx = content.rfind('</div>', 0, script_idx)
            if div_idx != -1:
                content = content[:div_idx] + content[div_idx+6:] # remove that specific </div>
        else:
            div_idx = content.rfind('</div>', 0, content.rfind('</body>'))
            if div_idx != -1:
                content = content[:div_idx] + content[div_idx+6:]

    # REVERT CSS
    # Remove the CSS I injected
    content = re.sub(r"/\*\s*GLOBAL LAYOUT FIX\s*\*/[^}]*\}\s*\.app-layout[^\}]*\}", "", content)
    
    # Remove all the sub rules belonging to standard sidebar/main to clean them out 
    content = re.sub(r"html,\s*body\s*\{[^}]*\}", "", content)
    content = re.sub(r"\.sidebar(?!\-)[^}]*\}", "", content)
    content = re.sub(r"\.sidebar-header[^}]*\}", "", content)
    content = re.sub(r"\.sidebar-nav[^}]*\}", "", content)
    content = re.sub(r"\.nav-category[^}]*\}", "", content)
    content = re.sub(r"\.sidebar a[^}]*\}", "", content)
    content = re.sub(r"\.sidebar a:hover[^}]*\}", "", content)
    content = re.sub(r"\.sidebar-footer[^}]*\}", "", content)
    content = re.sub(r"\.main-wrapper[^}]*\}", "", content)
    content = re.sub(r"\.topbar[^}]*\}", "", content)
    content = re.sub(r"\.main-content[^}]*\}", "", content)

    # Insert old CSS
    if ":root {" in content:
        # Insert OLD_CSS right after :root { ... }
        content = re.sub(r"(:root\s*\{[^}]*\})", r"\1\n" + OLD_CSS, content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Reverted files.")
