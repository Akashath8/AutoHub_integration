import os
import glob
from bs4 import BeautifulSoup
import re

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))

NEW_CSS = """        :root { --sidebar-bg: #0f172a; --sidebar-hover: #1e293b; --primary-accent: #f97316; --bg-light: #f1f5f9; }
        body { background-color: var(--bg-light); font-family: 'Inter', sans-serif; display: flex; height: 100vh; overflow: hidden; margin: 0; }
        
        .sidebar { width: 260px; display: flex; flex-direction: column; background: var(--sidebar-bg); color: #cbd5e1; flex-shrink: 0; }
        .sidebar-header { padding: 20px; font-size: 1.25rem; font-weight: bold; color: white; border-bottom: 1px solid rgba(255,255,255,0.1); }
        .sidebar-nav { flex: 1; padding: 15px 0; overflow-y: auto; }
        .nav-category { padding: 15px 20px 5px; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #64748b; font-weight: bold; }
        .sidebar a { color: #cbd5e1; text-decoration: none; padding: 10px 20px; display: flex; align-items: center; gap: 10px; font-size: 0.9rem; transition: 0.2s; }
        .sidebar a:hover, .sidebar a.active { background: var(--sidebar-hover); color: white; border-left: 4px solid var(--primary-accent); padding-left: 16px; }
        .sidebar-footer { padding: 15px 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.85rem; }

        .main-content { flex: 1; overflow-y: auto; display: flex; flex-direction: column; }
        .topbar { height: 60px; background: white; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; flex-shrink: 0; }
        .page-content { flex: 1; padding: 24px; }"""

import sys

for path in files:
    filename = os.path.basename(path)
    if filename in ["update_terms.py", "replace_layout.py", "undo_layout.py", "clean_layout.py"]:
        continue

    # First clean the badly escaped class name just in case
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.replace('class=\\"app-layout\\"', 'class="app-layout"')
    raw = raw.replace('class=\\"app-layout"', 'class="app-layout"')
    
    soup = BeautifulSoup(raw, "html.parser")

    # 1. CSS Cleaning
    # Remove old css blocks (heuristic removal via regex on string, then re-parse)
    style_tag = soup.find('style')
    if style_tag and style_tag.string:
        css = style_tag.string
        css = re.sub(r"/\*\s*GLOBAL LAYOUT FIX\s*\*/[^}]*\}\s*\.app-layout[^\}]*\}", "", css)
        css = re.sub(r"html,\s*body\s*\{[^}]*\}", "", css)
        css = re.sub(r"body\s*\{[^}]*\}", "", css)
        css = re.sub(r"\.app-layout\s*\{[^}]*\}", "", css)
        
        # Remove standard blocks to insert our clean one
        css = re.sub(r":root\s*\{[^}]*\}", "", css)
        css = re.sub(r"\.sidebar(?!\-)[^}]*\}", "", css)
        css = re.sub(r"\.sidebar-header[^}]*\}", "", css)
        css = re.sub(r"\.sidebar-nav[^}]*\}", "", css)
        css = re.sub(r"\.nav-category[^}]*\}", "", css)
        css = re.sub(r"\.sidebar a[^}]*\}", "", css)
        css = re.sub(r"\.sidebar a:hover[^}]*\}", "", css)
        css = re.sub(r"\.sidebar-footer[^}]*\}", "", css)
        css = re.sub(r"\.main-wrapper[^}]*\}", "", css)
        css = re.sub(r"\.topbar[^}]*\}", "", css)
        css = re.sub(r"\.main-content[^}]*\}", "", css)
        css = re.sub(r"\.page-content[^}]*\}", "", css)
        
        style_tag.string = "\n" + NEW_CSS + "\n" + css

    # 2. HTML unwrapping
    app_layout = soup.find('div', class_='app-layout')
    if app_layout:
        app_layout.unwrap()

    # 3. Rename main-wrapper -> main-content
    # And rename inner main-content -> page-content
    main_wrapper = soup.find('div', class_='main-wrapper')
    inner_main = soup.find(class_='main-content')
    
    if inner_main:
        inner_main['class'] = ['page-content']
        # if it's a <main> tag, it's fine.
        
    if main_wrapper:
        main_wrapper['class'] = ['main-content']

    # Also remove nested app-layouts if any
    for al in soup.find_all('div', class_='app-layout'):
        al.unwrap()

    with open(path, "w", encoding="utf-8") as f:
        # Avoid bs4 auto-formatting completely destroying indentation if possible
        # Actually bs4 prettify might break things, so we just write the string
        f.write(str(soup))

print(f"Cleaned layout wrappers across files.")
