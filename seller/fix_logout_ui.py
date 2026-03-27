import os
import glob

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))

REPLACE_FROM = '<i class="fas fa-sign-out-alt ms-auto text-white-50 cursor-pointer" title="Logout" id="logoutBtn"></i>'
REPLACE_FROM_2 = '<i class="fas fa-sign-out-alt ms-auto text-white-50 cursor-pointer" title="Logout"></i>'

REPLACE_TO = '<a href="#" id="logoutBtn" class="text-decoration-none text-white-50 ms-auto py-2 px-2 fw-bold" style="font-size: 0.9rem;"><i class="fas fa-sign-out-alt me-1"></i>Logout</a>'

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    new_html = html.replace(REPLACE_FROM, REPLACE_TO).replace(REPLACE_FROM_2, REPLACE_TO)

    if new_html != html:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Updated {os.path.basename(path)}")

print("Logout text button injected.")
