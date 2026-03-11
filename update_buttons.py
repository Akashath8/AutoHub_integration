with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Volvo
html = html.replace(
'''<div class="row g-2 mb-2">
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-shopping-cart text-muted me-2"></i> Add to Cart</button></div>
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>
                        <div class="row g-2">
                            <div class="col-6"><button class="btn btn-pink w-100 rounded fw-bold"><i class="fas fa-bolt me-1"></i> Buy Now</button></div>
                            <div class="col-6"><button class="btn btn-cyan w-100 rounded fw-bold"><i class="fas fa-car me-1"></i> Book Test Drive</button></div>
                        </div>''',
'''<div class="row g-2 mb-2">
                            <div class="col-6"><button onclick="store.addToCart({id: 'fh16', name: '2021 Volvo FH16', price: 4500000, quantity: 1, image: 'https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&q=80'}); window.location.reload();" class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-shopping-cart text-muted me-2"></i> Add to Cart</button></div>
                            <div class="col-6"><button onclick="alert('Added to wishlist!')" class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>
                        <div class="row g-2">
                            <div class="col-6"><button onclick="window.location.href='cart.html'" class="btn btn-pink w-100 rounded fw-bold"><i class="fas fa-bolt me-1"></i> Buy Now</button></div>
                            <div class="col-6"><button onclick="window.location.href='my-test-drives.html'" class="btn btn-cyan w-100 rounded fw-bold"><i class="fas fa-car me-1"></i> Book Test Drive</button></div>
                        </div>''', 1)

# Traveller
html = html.replace(
'''<div class="row g-2 mb-2">
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-shopping-cart text-muted me-2"></i> Add to Cart</button></div>
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>
                        <div class="row g-2">
                            <div class="col-6"><button class="btn btn-pink w-100 rounded fw-bold"><i class="fas fa-bolt me-1"></i> Buy Now</button></div>
                            <div class="col-6"><button class="btn btn-cyan w-100 rounded fw-bold"><i class="fas fa-car me-1"></i> Book Test Drive</button></div>
                        </div>''',
'''<div class="row g-2 mb-2">
                            <div class="col-6"><button onclick="store.addToCart({id: 'traveller', name: '2022 Force Traveller', price: 1400000, quantity: 1, image: 'https://images.unsplash.com/photo-1559416523-140ddc3d238c?auto=format&fit=crop&q=80'}); window.location.reload();" class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-shopping-cart text-muted me-2"></i> Add to Cart</button></div>
                            <div class="col-6"><button onclick="alert('Added to wishlist!')" class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>
                        <div class="row g-2">
                            <div class="col-6"><button onclick="window.location.href='cart.html'" class="btn btn-pink w-100 rounded fw-bold"><i class="fas fa-bolt me-1"></i> Buy Now</button></div>
                            <div class="col-6"><button onclick="window.location.href='my-test-drives.html'" class="btn btn-cyan w-100 rounded fw-bold"><i class="fas fa-car me-1"></i> Book Test Drive</button></div>
                        </div>''', 1)

# Auction
html = html.replace(
'''<div class="row g-2 mt-auto">
                            <div class="col-6"><button class="btn btn-orange w-100 rounded fw-bold"><i class="fas fa-gavel me-1"></i> Place Bid</button></div>
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>''',
'''<div class="row g-2 mt-auto">
                            <div class="col-6"><button onclick="window.location.href='auction-subscription.html'" class="btn btn-orange w-100 rounded fw-bold"><i class="fas fa-gavel me-1"></i> Place Bid</button></div>
                            <div class="col-6"><button onclick="alert('Added to wishlist!')" class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>''', 1)

# Events View Auction
html = html.replace(
'''<button class="btn btn-orange px-4 py-2 fw-bold text-white rounded"><i class="fas fa-eye me-2"></i> View Auction</button>''',
'''<button onclick="window.location.href='listing.html'" class="btn btn-orange px-4 py-2 fw-bold text-white rounded"><i class="fas fa-eye me-2"></i> View Auction</button>'''
)

html = html.replace(
'''<button class="btn btn-cyan px-4 py-2 fw-bold rounded"><i class="fas fa-eye me-2"></i> View Auction</button>''',
'''<button onclick="window.location.href='listing.html'" class="btn btn-cyan px-4 py-2 fw-bold rounded"><i class="fas fa-eye me-2"></i> View Auction</button>'''
)

# Get in touch form send message
html = html.replace(
'''<button type="button" class="btn btn-cyan w-100 py-3 fw-bold rounded">Send Message</button>''',
'''<button type="button" onclick="alert('Message sent successfully!');" class="btn btn-cyan w-100 py-3 fw-bold rounded">Send Message</button>'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
