import os
import glob
from bs4 import BeautifulSoup

ROOT_DIR = r"d:\Old_backup\Tri-party LOS inregration\los-project - Copy"
files = glob.glob(os.path.join(ROOT_DIR, "*.html"))

MEGA_MENU_CSS = """
    <style id="super-mega-menu-css">
        /* Mega Menu Styles */
        .dropdown-mega { position: static; }
        .mega-menu {
            position: absolute; top: 100%; left: 0; right: 0; margin: 0 auto;
            width: 96%; max-width: 1100px; background: #ffffff;
            border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            padding: 30px; display: none; z-index: 1050; border: 1px solid #e2e8f0;
            text-align: left;
        }
        .dropdown-mega:hover .mega-menu { display: block; animation: fadeInMega 0.2s ease-in-out; }
        .mega-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
        .mega-item h6 { font-weight: 700; margin-bottom: 15px; color: #111827; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }
        .mega-item p { font-size: 13px; color: #6b7280; line-height: 1.4; transition: color 0.2s; }
        .mega-item a { transition: all 0.2s ease; border-radius: 6px; padding: 8px; margin: -8px; }
        .mega-item a:hover { background-color: #f8fafc; }
        .mega-item a:hover .fs-6 { color: var(--pink-accent, #ec4899); }
        .mega-item a:hover p { color: #4b5563; }
        @keyframes fadeInMega { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        /* Responsive Mobile Behavior */
        @media (max-width: 991px) {
            .mega-menu { position: static; width: 100%; box-shadow: none; padding: 15px; display: none; margin-top: 10px; }
            .dropdown-mega.show .mega-menu { display: block; }
            .mega-grid { grid-template-columns: 1fr; gap: 20px; }
        }
    </style>
"""

MEGA_MENU_HTML = """
    <!-- 1. BUY MENU -->
    <li class="nav-item dropdown-mega">
        <a class="nav-link text-main fw-bold" href="listing.html">Buy <i class="fas fa-chevron-down ms-1" style="font-size: 0.6em;"></i></a>
        <div class="mega-menu">
            <div class="mega-grid">
                <div class="mega-item">
                    <h6>Explore Vehicles</h6>
                    <a href="listing.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Search Vehicles</div><p class="mb-0">Browse all available vehicles</p></a>
                    <a href="listing.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Explore by Category</div><p class="mb-0">Cars, Commercial, EVs</p></a>
                    <a href="listing.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Featured Listings</div><p class="mb-0">Verified & premium vehicles</p></a>
                </div>
                <div class="mega-item">
                    <h6>Buying Tools</h6>
                    <a href="#" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Compare Vehicles</div><p class="mb-0">Side-by-side comparison</p></a>
                    <a href="#" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">EMI Calculator</div><p class="mb-0">Estimate monthly payments</p></a>
                    <a href="#" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Loan Assistance</div><p class="mb-0">Financing options available</p></a>
                </div>
                <div class="mega-item">
                    <h6>Buyer Support</h6>
                    <a href="#" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Book Test Drive</div><p class="mb-0">Schedule a visit</p></a>
                    <a href="#" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Buyer Guide</div><p class="mb-0">How Buying Works</p></a>
                    <a href="#" class="d-block text-decoration-none text-dark mb-4"><div class="fw-bold fs-6">Verified Listings & Trust</div><p class="mb-0">Quality assured</p></a>
                    <a href="listing.html" class="btn btn-pink w-100 fw-bold rounded text-white py-2" style="margin:0; text-align:center;">Start Buying</a>
                </div>
            </div>
        </div>
    </li>

    <!-- 2. SELL MENU -->
    <li class="nav-item dropdown-mega">
        <a class="nav-link text-main fw-bold" href="sell-wizard.html">Sell <i class="fas fa-chevron-down ms-1" style="font-size: 0.6em;"></i></a>
        <div class="mega-menu">
            <div class="mega-grid">
                <div class="mega-item">
                    <h6>Getting Started</h6>
                    <a href="sell-wizard.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">How Selling Works</div><p class="mb-0">List → Get Quotes → Close Deal</p></a>
                    <a href="sell-wizard.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Who Can Sell</div><p class="mb-0">Dealers, fleet owners, businesses</p></a>
                    <a href="sell-wizard.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Why Sell on AutoHub</div><p class="mb-0">Reach, pricing, trust</p></a>
                </div>
                <div class="mega-item">
                    <h6>Seller Benefits</h6>
                    <div class="d-block text-dark mb-3 ps-2"><div class="fw-bold fs-6"><i class="fas fa-check text-success me-2"></i> Access Verified Buyers</div></div>
                    <div class="d-block text-dark mb-3 ps-2"><div class="fw-bold fs-6"><i class="fas fa-check text-success me-2"></i> Auction vs Direct Sale</div></div>
                    <div class="d-block text-dark mb-3 ps-2"><div class="fw-bold fs-6"><i class="fas fa-check text-success me-2"></i> Smart Pricing Insights</div></div>
                    <div class="d-block text-dark mb-3 ps-2"><div class="fw-bold fs-6"><i class="fas fa-check text-success me-2"></i> Secure Payments & Escrow</div></div>
                    <div class="d-block text-dark mb-3 ps-2"><div class="fw-bold fs-6"><i class="fas fa-check text-success me-2"></i> Documentation Support</div></div>
                </div>
                <div class="mega-item">
                    <h6>Conversion</h6>
                    <div class="bg-light p-3 rounded mb-4 text-start" style="margin:0; border: 1px solid rgba(0,0,0,0.1);">
                        <div class="small fw-bold text-success mb-2"><i class="fas fa-shield-alt"></i> Trusted by dealers across India</div>
                        <div class="small fw-bold text-dark"><i class="fas fa-car border p-1 rounded me-1 bg-white"></i> 10,000+ vehicles sold</div>
                    </div>
                    <a href="register.html" class="btn btn-dark w-100 fw-bold rounded mb-2 py-2 text-white" style="margin:0; text-align:center;">Become a Seller</a>
                    <a href="#" class="btn btn-outline-dark w-100 fw-bold rounded py-2" style="margin:0; text-align:center;">Talk to Account Manager</a>
                </div>
            </div>
        </div>
    </li>

    <!-- 3. AUCTIONS MENU -->
    <li class="nav-item dropdown-mega">
        <a class="nav-link text-main fw-bold" href="auction-subscription.html">Auctions <i class="fas fa-chevron-down ms-1" style="font-size: 0.6em;"></i></a>
        <div class="mega-menu">
            <div class="mega-grid">
                <div class="mega-item">
                    <h6>Discover Auctions</h6>
                    <a href="auction-subscription.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Live Auctions</div><p class="mb-0">Bid in real-time</p></a>
                    <a href="auction-subscription.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Upcoming Events</div><p class="mb-0">Plan your purchases</p></a>
                    <a href="auction-subscription.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Past Auction Results</div><p class="mb-0">Market price discovery</p></a>
                </div>
                <div class="mega-item">
                    <h6>Participate</h6>
                    <a href="auction-subscription.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">How Auctions Work</div><p class="mb-0">Step-by-step guidance</p></a>
                    <a href="auction-subscription.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Join Auction Events</div><p class="mb-0">Register as a bidder</p></a>
                    <a href="auction-subscription.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Rules & Eligibility</div><p class="mb-0">What you need to know</p></a>
                </div>
                <div class="mega-item">
                    <h6>Seller Education</h6>
                    <a href="sell-wizard.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">List Vehicle in Auction</div><p class="mb-0">Reach massive audiences</p></a>
                    <a href="sell-wizard.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Auction Benefits</div><p class="mb-0">Faster liquidation</p></a>
                    <a href="sell-wizard.html" class="d-block text-decoration-none text-dark mb-4"><div class="fw-bold fs-6">Pricing Transparency</div><p class="mb-0">Market-driven value</p></a>
                    <a href="auction-subscription.html" class="btn w-100 fw-bold rounded text-white py-2" style="background-color: var(--orange-accent); margin:0; text-align:center;">View Live Auctions</a>
                </div>
            </div>
        </div>
    </li>

    <!-- 4. RESOURCES MENU -->
    <li class="nav-item dropdown-mega">
        <a class="nav-link text-main fw-bold" href="blogs.html">Resources <i class="fas fa-chevron-down ms-1" style="font-size: 0.6em;"></i></a>
        <div class="mega-menu">
            <div class="mega-grid">
                <div class="mega-item">
                    <h6>Learn</h6>
                    <a href="blogs.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Buyer Guide</div><p class="mb-0">Procurement made easy</p></a>
                    <a href="blogs.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Seller Guide</div><p class="mb-0">Maximize your margins</p></a>
                    <a href="blogs.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Auction Guide</div><p class="mb-0">Bidding strategies</p></a>
                </div>
                <div class="mega-item">
                    <h6>Support</h6>
                    <a href="support.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Help Center</div><p class="mb-0">Get assistance</p></a>
                    <a href="faqs.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">FAQs</div><p class="mb-0">Common questions</p></a>
                    <a href="support.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Contact Support</div><p class="mb-0">We are here to help</p></a>
                </div>
                <div class="mega-item">
                    <h6>Insights</h6>
                    <a href="blogs.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Blogs & Industry Insights</div><p class="mb-0">Latest automotive news</p></a>
                    <a href="blogs.html" class="d-block text-decoration-none text-dark mb-3"><div class="fw-bold fs-6">Market Trends</div><p class="mb-0">Demand forecasting</p></a>
                    <a href="blogs.html" class="d-block text-decoration-none text-dark mb-4"><div class="fw-bold fs-6">Price Reports</div><p class="mb-0">Valuation matrix</p></a>
                    <a href="blogs.html" class="btn btn-primary w-100 fw-bold rounded text-white py-2" style="margin:0; text-align:center;">Explore Resources</a>
                </div>
            </div>
        </div>
    </li>
"""

mega_soup = BeautifulSoup(MEGA_MENU_HTML, "html.parser")
mega_items = list(mega_soup.children) 

def is_mega_menu_present(ul):
    return 'dropdown-mega' in str(ul)

for path in files:
    if os.path.basename(path) in ["header.html", "footer.html", "success.html"]:
        # Skip weird files if necessary, let it run on everything
        pass

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    
    # Very relaxed check: 'navbar-nav' and typically 'ms-auto' or 'me-auto' for the main right block
    nav_ul_candidates = soup.find_all('ul', class_=lambda x: x and 'navbar-nav' in x)
    nav_ul = None
    for ul in nav_ul_candidates:
        if 'ms-auto' in ul.get('class', []) or 'me-auto' in ul.get('class', []):
            nav_ul = ul
            break

    if not nav_ul or is_mega_menu_present(nav_ul):
        continue
    
    # Add CSS if not present
    head = soup.find('head')
    if head and not soup.find(id="super-mega-menu-css"):
        css_soup = BeautifulSoup(MEGA_MENU_CSS, "html.parser")
        head.append(css_soup)

    # We need to remove the first navigation items: Buy, Sell, Auctions, Resources, Finance
    # Then prepend our Mega Menu variants.
    li_items = nav_ul.find_all('li', class_='nav-item', recursive=False)
    to_remove = []
    
    # Because of formatting variations, let's simply remove those specific links natively
    valid_remove_texts = ['buy', 'sell', 'auctions', 'resources', 'finance']
    
    for li in li_items:
        # Check all child `a` text combined, or just direct `a` child
        a = li.find('a', class_='nav-link')
        if not a: continue
        clean_text = ''.join(a.find_all(text=True, recursive=False)).strip().lower()
        if not clean_text:
            clean_text = a.text.strip().lower()

        # Specifically for "Resources" which has an inner dropdown toggle formatting
        if any(keyword in clean_text for keyword in valid_remove_texts):
             to_remove.append(li)

    # Remove them
    for li in to_remove:
        li.extract()

    # Insert Mega Menu items at the beginning
    for item in reversed(mega_items):
        nav_ul.insert(0, item)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Updated", os.path.basename(path))

print("Done updating navbar mega menus globally.")
