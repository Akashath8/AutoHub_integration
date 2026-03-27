import os
import glob
import re

SELLER_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy\seller"
files = glob.glob(os.path.join(SELLER_DIR, "*.html"))

replacements = {
    "Escrow & Payouts": "Payments & Settlements",
    "Deal Fulfillment": "Order Completion",
    "Quotations": "Buyer Offers",
    "Document Center": "Upload & Verify Documents",
    "Auction Subscription": "Auction Plans & Participation"
}

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple replace
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Also fix some specific filenames or links if we want, but currently we just change text.
    # We should also ensure the sidebar has the 'Help & Onboarding Guide'.
    # I'll inject the 'Help & Onboarding Guide' right above company profile or at the bottom of the nav.
    
    if "nav-category\">Administration</div>" in content and "Help & Onboarding Guide" not in content:
        help_link = "\n            <a href=\"#\" onclick=\"startGuidedTour()\"><i class=\"fas fa-question-circle w-20px text-center\"></i> Help & Onboarding Guide</a>"
        content = content.replace("<div class=\"nav-category\">Administration</div>", "<div class=\"nav-category\">Administration</div>" + help_link)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated {len(files)} files.")
