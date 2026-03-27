import os
import glob
from bs4 import BeautifulSoup

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))

class_replacements = {
    "bg-theme-primary": "bg-white",
    "bg-theme-secondary": "bg-light",
    "bg-theme-accent": "bg-primary text-white",
    "text-white": "text-dark",
    "text-white-50": "text-muted",
    "text-main": "text-dark",
    "border-theme": "border",
    "btn-outline-light": "btn-outline-secondary",
    "border-secondary border-opacity-25": "border-light",
    # Mute dark tables
    "table-dark": "",
}

for path in files:
    filename = os.path.basename(path)
    if filename == "dashboard.html": 
        # Dashboard is completely custom and already perfect.
        continue

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Only look inside main content to avoid touching sidebar or anything else
    page_content = soup.find(class_=lambda x: x and "page-content" in x.split())
    if not page_content:
        continue

    # Find all elements within page content
    for elem in page_content.find_all(True):
        classes = elem.get('class', [])
        if not classes:
            continue
            
        new_classes = []
        changed = False
        for c in classes:
            if c in class_replacements:
                replacement = class_replacements[c]
                if replacement:
                    new_classes.extend(replacement.split())
                changed = True
            else:
                new_classes.append(c)
                
        if changed:
            # We must be careful not to make text-dark on a Primary button!
            # If element is a button with btn-primary, remove text-dark.
            if "btn-primary" in new_classes and "text-dark" in new_classes:
                new_classes.remove("text-dark")
                
            elem['class'] = list(dict.fromkeys(new_classes)) # unique

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print(f"Neutralized dark UI components in {filename}")

print("Internal content components synchronized with light theme.")
