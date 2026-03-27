import os
import glob
from bs4 import BeautifulSoup

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))

NEW_LAYOUT_CSS = """
    <style id="app-layout-styles">
        /* App Shell Layout */
        body { margin: 0; padding: 0; background-color: var(--bg-light); font-family: 'Inter', sans-serif; overflow: hidden; }
        .app-layout { display: flex; height: 100vh; width: 100vw; overflow: hidden; }
        
        .app-layout > .sidebar { 
            width: 260px; 
            flex-shrink: 0; 
            background: var(--sidebar-bg, #0f172a); 
            display: flex; 
            flex-direction: column; 
            height: 100vh; 
            overflow-y: auto; 
            z-index: 1040;
        }
        
        .main-wrapper { 
            flex: 1; 
            display: flex; 
            flex-direction: column; 
            height: 100vh; 
            overflow: hidden; 
            position: relative;
        }
        
        .main-wrapper > .topbar {
            flex-shrink: 0;
            z-index: 1030;
        }
        
        .main-wrapper > .main-content { 
            flex: 1; 
            overflow-y: auto; 
            padding: 24px; 
            background-color: var(--bg-light, #f1f5f9);
        }
    </style>
"""

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    
    if soup.find(class_="app-layout"):
        continue

    # 1. Clean old body CSS block mapping
    style_tags = soup.find_all("style")
    for style in style_tags:
        if style.string:
            import re
            style.string = re.sub(r"body\s*\{[^}]*overflow:\s*hidden[^}]*\}", "body { background-color: var(--bg-light); font-family: 'Inter', sans-serif; margin: 0; }", style.string)
    
    # 2. Insert the styles
    head = soup.find("head")
    if head and not soup.find(id="app-layout-styles"):
        css_soup = BeautifulSoup(NEW_LAYOUT_CSS, "html.parser")
        head.append(css_soup)

    # 3. DOM Manipulation
    body = soup.find("body")
    if not body: continue

    sidebar = soup.find(class_=lambda x: x and "sidebar" in x.split())
    # The existing main-content holds the header and the page content
    old_main_content = soup.find(class_=lambda x: x and "main-content" in x.split())
    
    if sidebar and old_main_content:
        # Create App Layout Wrapper
        app_layout = soup.new_tag("div", attrs={"class": "app-layout"})
        
        # The existing main-content becomes main-wrapper to hold header and scrollable body
        old_main_content['class'] = [c for c in old_main_content['class'] if c != 'main-content'] + ['main-wrapper']
        
        # The internal page-content becomes main-content (which handles the scrolling of content exclusively)
        page_content = old_main_content.find(class_=lambda x: x and "page-content" in x.split())
        if page_content:
            page_content['class'] = [c for c in page_content['class'] if c != 'page-content'] + ['main-content']

        sidebar.extract()
        old_main_content.extract()

        app_layout.append(sidebar)
        app_layout.append(old_main_content)

        body.insert(0, app_layout)
        
        with open(path, "w", encoding="utf-8") as f:
             # Make output look relatively beautiful
             # Don't use prettify as it inserts newlines everywhere causing structural visual breaks occasionally
             f.write(str(soup))
             
        print("Restored new app layout on", os.path.basename(path))

print("All Seller Dashboards restored to Premium App Layout.")
