import os
import glob
from bs4 import BeautifulSoup

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
dashboard_path = os.path.join(SELLER_DIR, "dashboard.html")

with open(dashboard_path, "r", encoding="utf-8") as f:
    dash_html = f.read()

dash_soup = BeautifulSoup(dash_html, "html.parser")

# 1. Extract the primary styling block
style_block = str(dash_soup.find("style"))

# 2. Extract Sidebar and Header templates
sidebar_block = str(dash_soup.find("aside", class_="sidebar-mini"))
header_block = str(dash_soup.find("header", class_="top-header"))

# Remove hardcoded 'active' classes from the copied components
sidebar_soup = BeautifulSoup(sidebar_block, "html.parser")
for a in sidebar_soup.find_all("a", class_="nav-item"):
    classes = a.get('class', [])
    if 'active' in classes:
        classes.remove('active')
        a['class'] = classes

header_soup = BeautifulSoup(header_block, "html.parser")
horizontal_nav = header_soup.find("nav", class_="horizontal-nav")
if horizontal_nav:
    for a in horizontal_nav.find_all("a"):
        classes = a.get('class', [])
        if 'active' in classes:
            classes.remove('active')
            a['class'] = classes

sidebar_str = str(sidebar_soup)
header_str = str(header_soup)

# Navigation Highlighting JS
NAV_ACTIVE_JS = """
<!-- Dynamic Nav Highlighting -->
<script id="dynamic-nav-js">
    document.addEventListener("DOMContentLoaded", function() {
        let currentPath = window.location.pathname.split('/').pop();
        if(!currentPath || currentPath === '') currentPath = 'dashboard.html';
        
        // Highlight side nav
        const sideNavs = document.querySelectorAll('.sidebar-mini a.nav-item');
        let sideMatched = false;
        sideNavs.forEach(nav => {
            const href = nav.getAttribute('href');
            if (href && href === currentPath) {
                nav.classList.add('active');
                sideMatched = true;
            }
        });
        // Default to first icon if no match
        if(!sideMatched) {
            document.querySelector('.sidebar-mini a.nav-item')?.classList.add('active');
        }

        // Highlight horizontal nav
        const topNavs = document.querySelectorAll('.horizontal-nav a');
        topNavs.forEach(nav => {
            const href = nav.getAttribute('href');
            if (href && currentPath.includes(href.split('.')[0]) && href !== '#') {
                nav.classList.add('active');
            }
        });
        
        // Match base
        if(currentPath === 'dashboard.html') {
            document.querySelector('.horizontal-nav a[href="dashboard.html"]')?.classList.add('active');
        }
    });
</script>
"""

# Process all other seller pages
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))
for path in files:
    filename = os.path.basename(path)
    if filename == "dashboard.html":
        # Inject the nav JS into dashboard too so it highlights properly
        soup = BeautifulSoup(dash_html, "html.parser")
        if not soup.find(id="dynamic-nav-js"):
            body = soup.find("body")
            if body:
                body.append(BeautifulSoup(NAV_ACTIVE_JS, "html.parser"))
                with open(path, "w", encoding="utf-8") as f:
                    f.write(str(soup))
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    
    # 1. Clean old styles
    for s in soup.find_all("style"):
        s.extract()
        
    # Append the new master style
    head = soup.find("head")
    if head:
        head.append(BeautifulSoup(style_block, "html.parser"))
        
    # 2. Unwrap .app-layout if it exists (Our new layout relies on body directly)
    app_layout = soup.find("div", class_="app-layout")
    if app_layout:
        app_layout.unwrap()

    # 3. Replace Sidebar
    old_sidebar = soup.find("aside", class_=lambda x: x and ("sidebar" in x))
    if old_sidebar:
        old_sidebar.replace_with(BeautifulSoup(sidebar_str, "html.parser"))
        
    # 4. Replace Header
    old_header = soup.find("header", class_=lambda x: x and ("topbar" in x.split() or "top-header" in x.split()))
    if old_header:
        old_header.replace_with(BeautifulSoup(header_str, "html.parser"))

    # 5. Fix Content Area Classes
    # Ensure what holds the content has class page-content 
    main_content = soup.find(class_=lambda x: x and "main-content" in x.split())
    if main_content and "main-wrapper" not in main_content.get("class", []):
         # Sometimes it's called main-content, change to page-content
         main_content['class'] = [c for c in main_content.get('class', []) if c != 'main-content'] + ['page-content']

    # 6. Inject the Nav Logic JS
    if not soup.find(id="dynamic-nav-js"):
        body = soup.find("body")
        if body:
            body.append(BeautifulSoup(NAV_ACTIVE_JS, "html.parser"))

    # Add light-theme fixes to internal elements (e.g. remove text-white, change bg-dark to white)
    # We will remove `text-white` classes from general containers if they existed
    for elem in soup.find_all(class_=lambda x: x and "text-white" in x.split()):
        # don't remove from badges or buttons
        if elem.name not in ["span", "button", "a", "i", "div"]:
            classes = elem.get('class', [])
            if 'text-white' in classes:
                classes.remove('text-white')
                elem['class'] = classes

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"Propagated theme universally to {filename}")

print("All seller platform pages upgraded to the Light-Theme globally.")
