import os
import re

CSS_ADDITIONS = """
        /* EXPANDABLE SIDEBAR STYLES */
        .sidebar-mini {
            width: var(--sidebar-width);
            transition: width 0.3s ease;
            overflow: hidden;
            position: relative;
        }
        .sidebar-mini.expanded {
            width: 240px;
        }
        .sidebar-mini .nav-item {
            display: flex;
            align-items: center;
            justify-content: flex-start;
            width: calc(100% - 24px);
            margin-left: 12px;
            margin-right: 12px;
            padding-left: 12px;
            overflow: hidden;
            white-space: nowrap;
            transition: all 0.2s;
        }
        .sidebar-mini .nav-item i {
            min-width: 24px;
            text-align: center;
        }
        .sidebar-mini .nav-text {
            margin-left: 15px;
            opacity: 0;
            transition: opacity 0.3s ease;
            font-size: 0.95rem;
            font-weight: 500;
        }
        .sidebar-mini.expanded .nav-text {
            opacity: 1;
        }
        .sidebar-toggle {
            cursor: pointer;
            margin-bottom: 20px;
            width: 100%;
            display: flex;
            justify-content: center;
            color: var(--text-muted);
            transition: 0.2s;
        }
        .sidebar-mini.expanded .sidebar-toggle {
            justify-content: flex-end;
            padding-right: 20px;
        }
        .sidebar-toggle:hover {
            color: var(--primary-blue);
        }

        /* DROPDOWN ENHANCEMENTS */
        .profile-dropdown {
            width: 260px;
            border-radius: 12px;
            animation: fadeIn 0.2s ease;
            padding: 0;
            overflow: hidden;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .dropdown-header-custom {
            padding: 20px;
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            border-bottom: 1px solid var(--border-light);
            text-align: center;
        }
        .dropdown-header-custom h6 {
            margin: 0;
            font-weight: 700;
            color: var(--text-main);
        }
        .dropdown-header-custom p {
            margin: 0;
            font-size: 0.8rem;
            color: var(--text-muted);
        }
        .profile-dropdown .dropdown-item {
            padding: 12px 20px;
            font-weight: 600;
            font-size: 0.9rem;
            transition: 0.2s;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .profile-dropdown .dropdown-item:hover {
            background-color: #f8fafc;
            color: var(--primary-blue);
        }
        .profile-dropdown .dropdown-item i {
            font-size: 1.1rem;
            width: 20px;
            text-align: center;
            color: #94a3b8;
        }
        .profile-dropdown .dropdown-item:hover i {
            color: var(--primary-blue);
        }
        .profile-dropdown .text-danger:hover {
            background-color: #fef2f2;
            color: #ef4444 !important;
        }
        .profile-dropdown .text-danger:hover i {
            color: #ef4444;
        }
"""

JS_ADDITIONS = """
<!-- Sidebar Toggle JS -->
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const sidebar = document.querySelector('.sidebar-mini');
        const toggleBtn = document.getElementById('sidebarToggleBtn');
        if (sidebar && toggleBtn) {
            toggleBtn.addEventListener('click', () => {
                sidebar.classList.toggle('expanded');
            });
        }
    });
</script>
</body>"""

NEW_SIDEBAR = """<!-- THIN LEFT SIDEBAR -->
    <aside class="sidebar-mini">
        <div class="sidebar-toggle" id="sidebarToggleBtn" title="Toggle Sidebar">
            <i class="fas fa-bars fa-lg"></i>
        </div>
        <div class="mb-2 w-100 d-flex justify-content-center brand-icon-only">
            <!-- Brand Icon -->
            <div style="width:44px; height:44px; display:flex; align-items:center; justify-content:center; border-radius:12px; background:var(--primary-blue); color:white; margin-bottom: 12px;">
                <i class="fas fa-car-side"></i>
            </div>
        </div>
        <a href="dashboard.html" class="nav-item {{PAGE_DASHBOARD}}" title="Dashboard">
            <i class="fas fa-chart-pie"></i><span class="nav-text">Dashboard</span>
        </a>
        <a href="inventory.html" class="nav-item {{PAGE_INVENTORY}}" title="Inventory">
            <i class="fas fa-car"></i><span class="nav-text">Inventory</span>
        </a>
        <a href="quotations.html" class="nav-item {{PAGE_QUOTATIONS}}" title="Quotations">
            <i class="fas fa-file-invoice-dollar"></i><span class="nav-text">Quotations</span>
        </a>
        <a href="orders.html" class="nav-item {{PAGE_ORDERS}}" title="Orders">
            <i class="fas fa-shopping-cart"></i><span class="nav-text">Orders</span>
        </a>
        <a href="payments.html" class="nav-item {{PAGE_PAYMENTS}}" title="Payments">
            <i class="fas fa-wallet"></i><span class="nav-text">Payments</span>
        </a>
        <a href="documents.html" class="nav-item {{PAGE_DOCUMENTS}}" title="Documents">
            <i class="fas fa-file-alt"></i><span class="nav-text">Documents</span>
        </a>
        
        <div class="sidebar-bottom w-100">
            <a href="#" class="nav-item" title="Help">
                <i class="far fa-question-circle"></i><span class="nav-text">Help</span>
            </a>
        </div>
    </aside>"""

NEW_HEADER = """<!-- HEADER -->
        <header class="top-header">
            <div class="brand-logo">
                <i class="fas fa-car-side" style="visibility: hidden; width: 0; margin:0;"></i>
                <div>
                    <div>AUTOHUB</div>
                    <span>DEALER PORTAL</span>
                </div>
            </div>

            <nav class="horizontal-nav">
                <!-- Top Navbar Links Removed for Cleanliness -->
            </nav>

            <div class="header-actions">
                <div class="search-container">
                    <i class="fas fa-search"></i>
                    <input type="text" placeholder="Search Inventory, Leads...">
                </div>
                <div class="notification-btn me-2">
                    <i class="far fa-bell"></i>
                    <div class="notification-dot"></div>
                </div>
                <div class="user-avatar dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" style="border: 2px solid var(--primary-blue); background:#fff; color:var(--primary-blue);">
                    S.J.
                </div>
                <!-- ENHANCED PROFILE DROPDOWN -->
                <ul class="dropdown-menu dropdown-menu-end shadow border-0 profile-dropdown mt-2">
                    <div class="dropdown-header-custom">
                        <div class="user-avatar mx-auto mb-2" style="width:48px; height:48px; font-size:1.1rem; background: var(--primary-blue); color: white;">SJ</div>
                        <h6>Sarah Jenkins</h6>
                        <p>sarah.j@autohub.com</p>
                    </div>
                    <li><a class="dropdown-item" href="profile.html"><i class="fas fa-user-circle"></i> My Profile</a></li>
                    <li><a class="dropdown-item" href="profile.html"><i class="fas fa-cog"></i> Settings</a></li>
                    <li><hr class="dropdown-divider m-0"></li>
                    <li><a class="dropdown-item text-danger" href="#" onclick="document.getElementById('logoutBtn') ? document.getElementById('logoutBtn').click() : window.location.href='../login.html'"><i class="fas fa-sign-out-alt"></i> Logout</a></li>
                </ul>
            </div>
        </header>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine active page
    filename = os.path.basename(filepath)
    sidebar = NEW_SIDEBAR
    for page in ['dashboard', 'inventory', 'quotations', 'orders', 'payments', 'documents']:
        placeholder = f"{{{{PAGE_{page.upper()}}}}}"
        if filename.startswith(page):
            sidebar = sidebar.replace(placeholder, 'active')
        else:
            sidebar = sidebar.replace(placeholder, '')

    # Ensure {{...}} is completely gone if missing
    sidebar = re.sub(r'\{\{PAGE_[A-Z]+\}\}', '', sidebar)

    # 1. Replace Aside
    content = re.sub(r'<!-- THIN LEFT SIDEBAR -->(.*?)</aside>', sidebar, content, flags=re.DOTALL)
    
    # Also if the file doesn't have the comment but has <aside class="sidebar-mini">
    if '<!-- THIN LEFT SIDEBAR -->' not in content and '<aside class="sidebar-mini">' in content:
        content = re.sub(r'<aside class="sidebar-mini">(.*?)</aside>', sidebar, content, flags=re.DOTALL)

    # 2. Replace Header
    content = re.sub(r'<!-- HEADER -->(.*?)</header>', NEW_HEADER, content, flags=re.DOTALL)
    if '<!-- HEADER -->' not in content and '<header class="top-header">' in content:
        content = re.sub(r'<header class="top-header">(.*?)</header>', NEW_HEADER, content, flags=re.DOTALL)

    # 3. Inject CSS
    if '/* EXPANDABLE SIDEBAR STYLES */' not in content:
        content = content.replace('</style>', CSS_ADDITIONS + '\n    </style>')

    # 4. Inject JS
    if '<!-- Sidebar Toggle JS -->' not in content:
        content = content.replace('</body>', JS_ADDITIONS)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

def main():
    directory = '.'
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            process_file(filepath)

if __name__ == '__main__':
    main()
