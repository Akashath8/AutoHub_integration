import os
import glob
from bs4 import BeautifulSoup

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))

LOGOUT_SCRIPT = """
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const logoutBtn = document.getElementById("logoutBtn");
            if (logoutBtn) {
                logoutBtn.addEventListener("click", function(e) {
                    e.preventDefault();
                    if (confirm("Are you sure you want to logout?")) {
                        localStorage.clear();
                        sessionStorage.clear();
                        window.location.href = "../index.html";
                    }
                });
            }
        });
    </script>
"""

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Check if already added
    if "logoutBtn" in html and "Are you sure you want to logout?" in html:
        continue

    # Add id="logoutBtn" to the icon or replace it if the user specifically asked for a link
    # But since the layout has `<i class="fas fa-sign-out-alt ms-auto text-white-50 cursor-pointer" title="Logout"></i>`
    # Let's just find that and add the ID
    if 'title="Logout"' in html and 'id="logoutBtn"' not in html:
        html = html.replace('title="Logout"', 'title="Logout" id="logoutBtn"')
    elif '<i class="fas fa-sign-out-alt ms-auto text-white-50 cursor-pointer"></i>' in html and 'logoutBtn' not in html:
        html = html.replace('<i class="fas fa-sign-out-alt ms-auto text-white-50 cursor-pointer"></i>', '<i id="logoutBtn" class="fas fa-sign-out-alt ms-auto text-white-50 cursor-pointer" title="Logout"></i>')

    # Add the script before </body>
    if LOGOUT_SCRIPT.strip() not in html:
        html = html.replace("</body>", LOGOUT_SCRIPT + "\n</body>")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print("Logout functionality injected into all Seller Portal pages.")
