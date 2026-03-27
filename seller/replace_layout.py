import os
import glob
import re

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))

SIDEBAR_HTML = """    <aside class="sidebar z-3 shadow-lg">
        <div class="sidebar-header">AutoHub <span class="text-warning">B2B</span></div>
        <div class="sidebar-nav custom-scrollbar">
            <a href="dashboard.html" data-page="dashboard.html"><i class="fas fa-chart-line w-20px text-center"></i> Dashboard</a>
            <a href="notifications.html" data-page="notifications.html"><i class="fas fa-bell w-20px text-center"></i> Action Center <span class="badge bg-danger ms-auto rounded-pill">12</span></a>
            
            <div class="nav-category">Inventory & Sales</div>
            <a href="inventory.html" data-page="inventory.html"><i class="fas fa-car w-20px text-center"></i> Inventory Management</a>
            <a href="add-vehicle.html" data-page="add-vehicle.html"><i class="fas fa-plus-circle w-20px text-center"></i> Add New Vehicle</a>
            <a href="buyer-preview.html" data-page="buyer-preview.html"><i class="fas fa-eye w-20px text-center"></i> Buyer Preview</a>
            
            <div class="nav-category">Deal Pipeline</div>
            <a href="quotations.html" data-page="quotations.html"><i class="fas fa-handshake w-20px text-center"></i> Buyer Offers <span class="badge bg-primary ms-auto">5</span></a>
            <a href="orders.html" data-page="orders.html"><i class="fas fa-clipboard-list w-20px text-center"></i> Order Processing</a>
            <a href="deal-fulfillment.html" data-page="deal-fulfillment.html"><i class="fas fa-tasks w-20px text-center"></i> Order Completion</a>
            
            <div class="nav-category">Finance & Compliance</div>
            <a href="payments.html" data-page="payments.html"><i class="fas fa-wallet w-20px text-center"></i> Payments & Settlements</a>
            <a href="invoices.html" data-page="invoices.html"><i class="fas fa-file-invoice-dollar w-20px text-center"></i> Invoices & Tax</a>
            <a href="documents.html" data-page="documents.html"><i class="fas fa-folder-open w-20px text-center"></i> Upload & Verify Documents <span class="badge bg-warning text-dark ms-auto">2</span></a>
            
            <div class="nav-category">Administration</div>
            <a href="#" onclick="startGuidedTour()"><i class="fas fa-question-circle w-20px text-center"></i> Help & Onboarding Guide</a>
            <a href="profile.html" data-page="profile.html"><i class="fas fa-building w-20px text-center"></i> Company Profile</a>
            <a href="auction-subscription.html" data-page="auction-subscription.html"><i class="fas fa-gavel w-20px text-center"></i> Auction Plans & Participation</a>
        </div>
        <div class="sidebar-footer d-flex align-items-center gap-2">
            <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center" style="width:32px;height:32px;font-weight:bold;">RM</div>
            <div>
                <div class="fw-bold text-white lh-1">Royal Motors Pvt</div>
                <div class="text-white-50 small" style="font-size:10px;">ID: SELL-4921 &amp;bull; Pro Tier</div>
            </div>
            <i class="fas fa-sign-out-alt ms-auto text-white-50 cursor-pointer" title="Logout"></i>
        </div>
    </aside>"""

CSS_REPLACEMENT = """        /* GLOBAL LAYOUT FIX */
        html, body { height: 100%; margin: 0; overflow: hidden; background-color: var(--bg-light); font-family: 'Inter', sans-serif; }
        .app-layout { display: flex; height: 100vh; width: 100%; }
        
        .sidebar { width: 260px; background: #0f172a; color: white; display: flex; flex-direction: column; overflow-y: auto; flex-shrink: 0; }
        .sidebar-header { padding: 20px; font-size: 1.25rem; font-weight: bold; color: white; border-bottom: 1px solid rgba(255,255,255,0.1); }
        .sidebar-nav { flex: 1; overflow-y: auto; padding: 15px 0; }
        .nav-category { padding: 15px 20px 5px; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #64748b; font-weight: bold; }
        .sidebar a { color: #cbd5e1; text-decoration: none; padding: 10px 20px; display: flex; align-items: center; gap: 10px; font-size: 0.9rem; transition: 0.2s; }
        .sidebar a:hover, .sidebar a.active { background: var(--sidebar-hover); color: white; border-left: 4px solid var(--primary-accent); padding-left: 16px; }
        .sidebar-footer { padding: 15px 20px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.85rem; }

        .main-wrapper { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
        .topbar { height: 70px; flex-shrink: 0; background: white; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; }
        .main-content { flex: 1; overflow-y: auto; padding: 24px; }"""

import sys

for path in files:
    filename = os.path.basename(path)
    if filename == "update_terms.py" or filename == "replace_layout.py":
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace CSS
    # Remove the old body rule
    content = re.sub(r"body\s*\{[^}]*display:\s*flex;[^}]*\}", "", content)
    # Remove old .sidebar and .main-wrapper rules to avoid conflicts, including their sub-rules
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

    # Insert the new CSS block after <style>
    if "<style>" in content:
        content = content.replace("<style>", "<style>\n" + CSS_REPLACEMENT, 1)

    # 2. Extract and replace the aside tag.
    # Match from <aside class="sidebar"... to </aside>
    aside_pattern = re.compile(r"<aside\b[^>]*\bclass=[\"'][^\"']*sidebar[^\"']*[\"'][^>]*>.*?</aside>", re.DOTALL | re.IGNORECASE)
    if aside_pattern.search(content):
        # Insert active class for this specific file
        specific_sidebar = SIDEBAR_HTML.replace(f'data-page="{filename}"', f'data-page="{filename}" class="active"')
        content = aside_pattern.sub(specific_sidebar, content)
    else:
        print(f"No sidebar found in {filename}")

    # 3. Wrap with <div class="app-layout">
    # We want to wrap from <aside> to </div> ending main-wrapper.
    # But some scripts are inside main-wrapper, some are outside.
    # Let's cleanly inject <div class="app-layout"> before <aside> 
    # and </div> after the end of main-wrapper OR before the first <script> tag at the bottom.
    
    # If app-layout is already there, skip wrapping.
    if 'class="app-layout"' not in content:
        # Wrap the whole body EXCEPT scripts
        # Replace <body> with <body>\n<div class="app-layout">
        content = re.sub(r"(<body[^>]*>)", r"\1\n    <div class=\"app-layout\">", content, count=1)
        
        # We need to close the div at the end of the content.
        # usually right before <script src="...bootstrap..."> or </body>
        # Let's find the first <script tag that loads bootstrap or shepherd, and place </div> before it.
        # If no script, place before </body>
        script_idx = content.rfind('<script src="https://cdn.jsdelivr.net/npm/bootstrap')
        if script_idx == -1:
            script_idx = content.rfind('</body>')
            
        if script_idx != -1:
            content = content[:script_idx] + "    </div>\n" + content[script_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Processed {len(files)} files.")
