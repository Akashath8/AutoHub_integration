with open('index.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - AutoHub Marketplace</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Icon Font -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/main.css">
    <style>
        body {
            background-color: var(--dark-bg);
            color: #f8f9fa;
        }

        /* Override Bootstrap defaults for dark theme readability */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
        }

        .text-muted {
            color: #9ca3af !important;
        }

        /* Navbar Customization */
        .navbar {
            background-color: var(--dark-bg) !important;
            padding: 1rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .search-input {
            background-color: rgba(255,255,255,0.08) !important;
            color: #fff !important;
            border: none;
        }
        .search-input::placeholder {
            color: rgba(255,255,255,0.5);
        }

        /* Hero Section */
        .hero-section {
            background: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.9)), url('https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80') center/cover;
            padding: 8rem 2rem 6rem;
            text-align: center;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        /* Horizontal Scroll for Cards */
        .custom-scrollbar::-webkit-scrollbar {
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background-color: rgba(255,255,255,0.2);
            border-radius: 10px;
        }

        /* Features Section Cards */
        .feature-card {
            background-color: #1a233a;
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 1rem;
            padding: 2rem;
            height: 100%;
            transition: transform 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            border-color: var(--cyan-accent);
        }

        /* Auction Tabs */
        .auction-tabs .nav-link {
            color: #9ca3af;
            font-weight: 600;
            border: none;
            border-bottom: 2px solid transparent;
            padding: 0.5rem 1rem;
        }
        .auction-tabs .nav-link.active {
            color: var(--orange-accent);
            background: transparent;
            border-bottom: 2px solid var(--orange-accent);
        }

        /* Footer */
        .footer-dark {
            background-color: #111827;
            padding: 4rem 2rem 2rem;
            border-top: 1px solid rgba(255,255,255,0.05);
        }
        .footer-dark a {
            color: #9ca3af;
            text-decoration: none;
            display: block;
            margin-bottom: 0.5rem;
            transition: color 0.2s;
        }
        .footer-dark a:hover {
            color: #fff;
        }

        /* Accordion Customization */
        .accordion-item {
            background-color: var(--dark-card) !important;
            border: 1px solid rgba(255,255,255,0.1);
            margin-bottom: 1rem;
            border-radius: 8px !important;
        }
        .accordion-button {
            background-color: var(--dark-card) !important;
            color: #fff !important;
            font-weight: 600;
            box-shadow: none !important;
            border-radius: 8px !important;
        }
        .accordion-button::after {
            filter: invert(1);
        }
        .accordion-body {
            color: #9ca3af;
        }

        /* Process Steps */
        .process-card {
            background-color: #1e293b;
            border-radius: 16px;
            padding: 2rem 1.5rem;
            text-align: left;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.05);
            height: 100%;
        }
        .process-card .step-number {
            position: absolute;
            top: 20px;
            right: 20px;
            font-size: 3.5rem;
            font-weight: 800;
            color: rgba(255,255,255,0.03);
            line-height: 1;
        }
    </style>
</head>

<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg sticky-top">
        <div class="container">
            <!-- Brand + Location Dropdown -->
            <div class="d-flex align-items-center gap-2">
                <a class="navbar-brand" href="index.html">AutoHub <span class="text-pink">Marketplace</span></a>
                <div class="dropdown d-none d-lg-block ms-3">
                    <button class="btn nav-link px-3 py-1 rounded" id="navLocationBtn" data-bs-toggle="dropdown" aria-expanded="false" style="background-color: rgba(255,255,255,0.08);">
                        <i class="fas fa-map-marker-alt text-pink me-1"></i> 
                        <span class="small text-muted d-block" style="font-size: 0.65rem; line-height: 1;">Location</span>
                        <span style="font-size: 0.85rem; font-weight: 600; color: #fff;">Pune <i class="fas fa-chevron-down ms-1" style="font-size:0.6rem;"></i></span>
                    </button>
                    <!-- Location menu will open here -->
                </div>
            </div>

            <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
                <i class="fas fa-bars text-white"></i>
            </button>

            <div class="collapse navbar-collapse" id="navbarContent">
                <!-- Center Search -->
                <div class="ms-4 me-auto" style="width: 40px; border-radius: 6px; overflow:hidden;">
                    <button class="btn search-input w-100 p-2"><i class="fas fa-search"></i></button>
                    <!-- Expandable search implementation omitted for layout fidelity -->
                </div>

                <!-- Right nav items -->
                <ul class="navbar-nav ms-auto align-items-center gap-3">
                    <li class="nav-item"><a class="nav-link text-white fw-bold" href="listing.html">Buy</a></li>
                    <li class="nav-item"><a class="nav-link text-white fw-bold" href="sell-wizard.html">Sell</a></li>
                    <li class="nav-item"><a class="nav-link text-white fw-bold" href="auction-subscription.html">Auctions</a></li>
                    <li class="nav-item"><a class="nav-link text-white fw-bold" href="#">Finance</a></li>
                    
                    <li class="nav-item ms-3 position-relative">
                        <a class="nav-link" href="#" title="Notifications">
                            <i class="fas fa-bell text-warning"></i>
                            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-pink">3</span>
                        </a>
                    </li>
                    <li class="nav-item position-relative">
                        <a class="nav-link" href="#" title="Wishlist">
                            <i class="fas fa-heart text-pink"></i>
                            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-pink">0</span>
                        </a>
                    </li>
                    <li class="nav-item me-3 position-relative">
                        <a class="nav-link" href="cart.html">
                            <i class="fas fa-shopping-cart text-secondary"></i>
                            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-pink" id="cartCount">0</span>
                        </a>
                    </li>

                    <!-- Profile / Login Area -->
                    <li class="nav-item" id="navProfileArea">
                        <!-- Handled by JS -->
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <div class="hero-section">
        <div class="container">
            <h1 class="display-3 fw-bold mb-1">India's Smart</h1>
            <h1 class="display-3 fw-bold mb-4 text-pink">Vehicle Marketplace</h1>
            <p class="lead mb-4 fw-normal">Buy, Sell, Auction, or Finance Vehicles in One Platform</p>
            
            <div class="d-flex justify-content-center gap-3 mb-4 flex-wrap">
                <a href="listing.html" class="btn btn-pink rounded px-4 py-2">Buy Vehicle</a>
                <a href="sell-wizard.html" class="btn btn-light rounded px-4 py-2 text-dark fw-bold">Sell Vehicle</a>
                <a href="auction-subscription.html" class="btn btn-outline-light rounded px-4 py-2 fw-bold" style="border-color: rgba(255,255,255,0.3);">Explore Auctions</a>
            </div>
            <p class="small text-muted">Currently showing buyer-focused marketplace content.</p>
        </div>
    </div>

    <!-- Marketplace Listings -->
    <div class="container py-5">
        <div class="text-center mb-5">
            <h2 class="fw-bold">Marketplace Listings</h2>
            <p class="text-muted">Direct purchase vehicles and live auction inventory available now.</p>
        </div>

        <div class="row g-4 justify-content-center" id="listingsGrid">
            <!-- Dynamically populated by JS to match screenshots -->
            
            <!-- Direct Sell Card 1 -->
            <div class="col-md-4">
                <div class="card bg-dark-card border-0 h-100 position-relative" style="border-radius: 12px; overflow: hidden;">
                    <span class="badge position-absolute top-0 start-0 m-3 px-3 py-2" style="background-color: #10b981; border-radius: 20px;">DIRECT SELL</span>
                    <img src="https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&q=80" class="card-img-top" alt="Scania" style="height: 220px; object-fit: cover;">
                    <div class="card-body p-4">
                        <h5 class="fw-bold text-white mb-2">2021 Volvo FH16</h5>
                        <p class="text-muted small mb-3">Heavy Duty &bull; 50,000 km &bull; Pune</p>
                        <div class="d-flex justify-content-between align-items-end mb-4">
                            <h4 class="text-pink fw-bold mb-0">₹ 45,00,000</h4>
                            <small class="text-muted">Certified Vehicle</small>
                        </div>
                        <div class="row g-2 mb-2">
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-shopping-cart text-muted me-2"></i> Add to Cart</button></div>
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>
                        <div class="row g-2">
                            <div class="col-6"><button class="btn btn-pink w-100 rounded fw-bold"><i class="fas fa-bolt me-1"></i> Buy Now</button></div>
                            <div class="col-6"><button class="btn btn-cyan w-100 rounded fw-bold"><i class="fas fa-car me-1"></i> Book Test Drive</button></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Direct Sell Card 2 -->
            <div class="col-md-4">
                <div class="card bg-dark-card border-0 h-100 position-relative" style="border-radius: 12px; overflow: hidden;">
                    <span class="badge position-absolute top-0 start-0 m-3 px-3 py-2" style="background-color: #10b981; border-radius: 20px;">DIRECT SELL</span>
                    <img src="https://images.unsplash.com/photo-1559416523-140ddc3d238c?auto=format&fit=crop&q=80" class="card-img-top" alt="Traveller" style="height: 220px; object-fit: cover;">
                    <div class="card-body p-4">
                        <h5 class="fw-bold text-white mb-2">2022 Force Traveller</h5>
                        <p class="text-muted small mb-3">Commercial &bull; 15,000 km &bull; Mumbai</p>
                        <div class="d-flex justify-content-between align-items-end mb-4">
                            <h4 class="text-pink fw-bold mb-0">₹ 14,00,000</h4>
                            <small class="text-muted">Ready for Delivery</small>
                        </div>
                        <div class="row g-2 mb-2">
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-shopping-cart text-muted me-2"></i> Add to Cart</button></div>
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>
                        <div class="row g-2">
                            <div class="col-6"><button class="btn btn-pink w-100 rounded fw-bold"><i class="fas fa-bolt me-1"></i> Buy Now</button></div>
                            <div class="col-6"><button class="btn btn-cyan w-100 rounded fw-bold"><i class="fas fa-car me-1"></i> Book Test Drive</button></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Auction Card -->
            <div class="col-md-4">
                <div class="card bg-dark-card border-0 h-100 position-relative" style="border-radius: 12px; overflow: hidden;">
                    <span class="badge position-absolute top-0 start-0 m-3 px-3 py-2 text-white" style="background-color: var(--orange-accent); border-radius: 20px;">AUCTION</span>
                    <img src="https://images.unsplash.com/photo-1519003722824-194d4455a60c?auto=format&fit=crop&q=80" class="card-img-top" alt="Scania Touring" style="height: 220px; object-fit: cover;">
                    <div class="card-body p-4">
                        <h5 class="fw-bold text-white mb-2">2019 Scania Touring</h5>
                        <p class="text-muted small mb-3">Passenger &bull; 120,000 km &bull; Live Bid</p>
                        
                        <div class="d-flex justify-content-between align-items-center mb-4">
                            <div>
                                <small class="text-muted d-block" style="font-size: 0.75rem;">Current Bid</small>
                                <h4 class="text-pink fw-bold mb-0">₹ 32,50,000</h4>
                            </div>
                            <div class="text-end">
                                <small class="text-muted d-block">12 Bids &bull; Ends in 2h 15m</small>
                            </div>
                        </div>
                        
                        <div class="row g-2 mt-auto">
                            <div class="col-6"><button class="btn btn-orange w-100 rounded fw-bold"><i class="fas fa-gavel me-1"></i> Place Bid</button></div>
                            <div class="col-6"><button class="btn btn-outline-secondary w-100 border-0 bg-dark text-white rounded"><i class="fas fa-heart text-muted me-2"></i> Wishlist</button></div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <!-- Live & Upcoming Auction Events (White Section) -->
    <div class="bg-white text-dark py-5" style="border-radius: 20px 20px 0 0;">
        <div class="container">
            <ul class="nav nav-tabs auction-tabs mb-4 px-2" id="myTab" role="tablist">
                <li class="nav-item" role="presentation">
                    <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#live-pane" type="button">
                        <span class="badge bg-pink text-white me-2">LIVE</span> Live Auctions (2)
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" data-bs-toggle="tab" data-bs-target="#upcoming-pane" type="button">
                        <i class="fas fa-calendar-alt me-2 text-muted"></i> Upcoming Auctions (2)
                    </button>
                </li>
            </ul>

            <div class="tab-content" id="myTabContent">
                <div class="tab-pane fade show active" id="live-pane" role="tabpanel">
                    <h4 class="fw-bold mb-2">Live & Upcoming Auction Events</h4>
                    <p class="text-muted mb-4">Browse sample auction events below. Each card includes a quick summary and a direct view button.</p>
                    
                    <div class="row g-4">
                        <!-- Event 1 -->
                        <div class="col-md-6">
                            <div class="card border-0 shadow-sm rounded-4 p-4 h-100" style="background-color: #f8fafc;">
                                <div class="d-flex justify-content-between align-items-start mb-2">
                                    <h5 class="fw-bold mb-0">Fleet Truck Clearance Auction</h5>
                                    <span class="fw-bold">12 Lots</span>
                                </div>
                                <span class="badge bg-pink bg-opacity-10 text-pink border border-pink border-opacity-25 px-2 py-1 mb-3">LIVE</span>
                                <p class="text-muted text-sm mb-4">Heavy-duty trucks from enterprise fleet upgrades with verified inspection reports.</p>
                                <div class="d-flex align-items-center text-secondary small mb-4 fw-bold">
                                    <i class="fas fa-map-marker-alt me-2"></i> Pune <span class="mx-3">|</span> 
                                    <i class="fas fa-clock me-2"></i> Ends Today, 6:30 PM
                                </div>
                                <div>
                                    <button class="btn btn-orange px-4 py-2 fw-bold text-white rounded"><i class="fas fa-eye me-2"></i> View Auction</button>
                                </div>
                            </div>
                        </div>
                        <!-- Event 2 -->
                        <div class="col-md-6">
                            <div class="card border-0 shadow-sm rounded-4 p-4 h-100" style="background-color: #f8fafc;">
                                <div class="d-flex justify-content-between align-items-start mb-2">
                                    <h5 class="fw-bold mb-0">Premium Bus Liquidation Event</h5>
                                    <span class="fw-bold">8 Lots</span>
                                </div>
                                <span class="badge bg-pink bg-opacity-10 text-pink border border-pink border-opacity-25 px-2 py-1 mb-3">LIVE</span>
                                <p class="text-muted text-sm mb-4">Touring buses and passenger vehicles listed by institutional sellers for quick bidding.</p>
                                <div class="d-flex align-items-center text-secondary small mb-4 fw-bold">
                                    <i class="fas fa-map-marker-alt me-2"></i> Bengaluru <span class="mx-3">|</span> 
                                    <i class="fas fa-clock me-2"></i> Ends Today, 8:00 PM
                                </div>
                                <div>
                                    <button class="btn btn-orange px-4 py-2 fw-bold text-white rounded"><i class="fas fa-eye me-2"></i> View Auction</button>
                                </div>
                            </div>
                        </div>
                        <!-- Event 3 & 4 (Upcoming visible when scrolled or tabbed) omitted -->
                        <div class="col-md-6">
                            <div class="card border-0 shadow-sm rounded-4 p-4 h-100" style="background-color: #f8fafc;">
                                <div class="d-flex justify-content-between align-items-start mb-2">
                                    <h5 class="fw-bold mb-0">Construction Vehicles Mega Sale</h5>
                                    <span class="fw-bold">15 Lots</span>
                                </div>
                                <span class="badge bg-info bg-opacity-10 text-info border border-info border-opacity-25 px-2 py-1 mb-3">UPCOMING</span>
                                <p class="text-muted text-sm mb-4">Tipper trucks, loaders, and site-ready commercial vehicles scheduled for bidding tomorrow.</p>
                                <div class="d-flex align-items-center text-secondary small mb-4 fw-bold">
                                    <i class="fas fa-map-marker-alt me-2"></i> Hyderabad <span class="mx-3">|</span> 
                                    <i class="fas fa-calendar-alt me-2"></i> Tomorrow, 11:00 AM
                                </div>
                                <div>
                                    <button class="btn btn-cyan px-4 py-2 fw-bold rounded"><i class="fas fa-eye me-2"></i> View Auction</button>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card border-0 shadow-sm rounded-4 p-4 h-100" style="background-color: #f8fafc;">
                                <div class="d-flex justify-content-between align-items-start mb-2">
                                    <h5 class="fw-bold mb-0">Dealer Exchange Auction</h5>
                                    <span class="fw-bold">10 Lots</span>
                                </div>
                                <span class="badge bg-info bg-opacity-10 text-info border border-info border-opacity-25 px-2 py-1 mb-3">UPCOMING</span>
                                <p class="text-muted text-sm mb-4">Dealer-owned cars, vans, and fleet returns with transparent reserve prices.</p>
                                <div class="d-flex align-items-center text-secondary small mb-4 fw-bold">
                                    <i class="fas fa-map-marker-alt me-2"></i> Chennai <span class="mx-3">|</span> 
                                    <i class="fas fa-calendar-alt me-2"></i> Friday, 3:00 PM
                                </div>
                                <div>
                                    <button class="btn btn-cyan px-4 py-2 fw-bold rounded"><i class="fas fa-eye me-2"></i> View Auction</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- How Buying Works -->
    <div class="py-5" style="background-color: var(--dark-bg); border-top: 1px solid rgba(255,255,255,0.05);">
        <div class="container">
            <h2 class="fw-bold mb-5">How Buying Works</h2>
            <div class="row g-3">
                <div class="col">
                    <div class="process-card">
                        <div class="step-number">01</div>
                        <div class="fs-4 mb-3" style="color: #a78bfa;"><i class="fas fa-search"></i></div>
                        <h6 class="fw-bold text-white mb-2">Browse Vehicles</h6>
                        <p class="small text-muted mb-0">Explore thousands of certified cars and commercial vehicles with transparent pricing and verified inventory.</p>
                    </div>
                </div>
                <div class="col">
                    <div class="process-card">
                        <div class="step-number">02</div>
                        <div class="fs-4 mb-3" style="color: #60a5fa;"><i class="fas fa-list-alt"></i></div>
                        <h6 class="fw-bold text-white mb-2">Compare Details</h6>
                        <p class="small text-muted mb-0">Check inspection reports, photos, ownership records, and price benchmarks before shortlisting.</p>
                    </div>
                </div>
                <div class="col">
                    <div class="process-card">
                        <div class="step-number">03</div>
                        <div class="fs-4 mb-3" style="color: #9ca3af;"><i class="fas fa-university"></i></div>
                        <h6 class="fw-bold text-white mb-2">Apply for Finance</h6>
                        <p class="small text-muted mb-0">Review finance options, pre-approvals, and institutional assistance for faster purchasing decisions.</p>
                    </div>
                </div>
                <div class="col">
                    <div class="process-card">
                        <div class="step-number">04</div>
                        <div class="fs-4 mb-3" style="color: #94a3b8;"><i class="fas fa-shopping-cart"></i></div>
                        <h6 class="fw-bold text-white mb-2">Add & Checkout</h6>
                        <p class="small text-muted mb-0">Add vehicles to cart, save to wishlist, buy instantly, or place bids depending on the inventory type.</p>
                    </div>
                </div>
                <div class="col">
                    <div class="process-card">
                        <div class="step-number">05</div>
                        <div class="fs-4 mb-3" style="color: #fbbf24;"><i class="fas fa-truck"></i></div>
                        <h6 class="fw-bold text-white mb-2">RC & Delivery</h6>
                        <p class="small text-muted mb-0">Complete documentation, transfer ownership, and schedule delivery through the marketplace workflow.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- About AutoHub -->
    <div class="py-5" style="background-color: var(--dark-bg); border-top: 1px solid rgba(255,255,255,0.05);">
        <div class="container text-center mb-5">
            <h2 class="fw-bold">About AutoHub</h2>
        </div>
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-5 pe-lg-5 mb-4 mb-md-0">
                    <h5 class="fw-bold text-white mb-3">Transforming B2B Vehicle Commerce</h5>
                    <p class="text-muted" style="line-height: 1.8;">AutoHub Marketplace is India's premier platform designed exclusively for B2B vehicle buying, selling, and auctioning. We bring transparency, institutional-grade assurance, and seamless financing to fleet operators, dealerships, and enterprise businesses.</p>
                </div>
                <div class="col-md-7">
                    <img src="https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&q=80" alt="Driving" class="img-fluid rounded-4 shadow-lg w-100" style="object-fit: cover; height: 350px;">
                </div>
            </div>
        </div>
    </div>

    <!-- What Our Partners Say -->
    <div class="py-5" style="background-color: var(--dark-bg); border-top: 1px solid rgba(255,255,255,0.05);">
        <div class="container text-center mb-5">
            <h2 class="fw-bold">What Our Partners Say</h2>
        </div>
        <div class="container">
            <div class="row justify-content-center g-4">
                <div class="col-md-5">
                    <div class="bg-dark-card p-4 rounded-4 position-relative h-100" style="border-left: 4px solid var(--cyan-accent);">
                        <p class="text-white mb-4">"AutoHub completely streamlined how we procure fleet vehicles. The financing integration is a game-changer."</p>
                        <h6 class="fw-bold text-cyan mb-0">- Rajesh K., Logistics CEO</h6>
                    </div>
                </div>
                <div class="col-md-5">
                    <div class="bg-dark-card p-4 rounded-4 position-relative h-100" style="border-left: 4px solid var(--cyan-accent);">
                        <p class="text-white mb-4">"Selling our decommissioned buses through their auction portal got us 15% above our target price."</p>
                        <h6 class="fw-bold text-cyan mb-0">- Amit P., Fleet Manager</h6>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- FAQ -->
    <div class="py-5" style="background-color: var(--dark-bg); border-top: 1px solid rgba(255,255,255,0.05);">
        <div class="container text-center mb-4">
            <h2 class="fw-bold">Frequently Asked Questions</h2>
        </div>
        <div class="container text-center mb-5">
            <div class="d-inline-flex gap-2 p-1 bg-dark-card rounded-pill">
                <button class="btn btn-cyan rounded-pill px-4 fw-bold">Buyers</button>
                <button class="btn text-white px-4">Sellers</button>
                <button class="btn text-white px-4">Finance</button>
                <button class="btn text-white px-4">Auctions</button>
            </div>
        </div>
        <div class="container" style="max-width: 800px;">
            <div class="accordion" id="faqAccordion">
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingOne">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
                            How do I register as a B2B buyer?
                        </button>
                    </h2>
                    <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#faqAccordion">
                        <div class="accordion-body">
                            Click on the Register/Sign in button at the top right, submit your company details, uploading GST and PAN documents for verification.
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingTwo">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                            Are all vehicles inspected before purchase?
                        </button>
                    </h2>
                    <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#faqAccordion">
                        <div class="accordion-body">
                            Yes, all Direct Sell and certified auction vehicles undergo a rigorous multi-point inspection process by our qualified engineers.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Get in Touch -->
    <div class="py-5" style="background-color: var(--dark-bg); border-top: 1px solid rgba(255,255,255,0.05);">
        <div class="container text-center mb-5">
            <h2 class="fw-bold">Get in Touch</h2>
        </div>
        <div class="container" style="max-width: 600px;">
            <div class="bg-dark-card p-4 rounded-4 border border-secondary border-opacity-25">
                <form>
                    <div class="mb-3">
                        <input type="text" class="form-control bg-dark border-secondary border-opacity-25 text-white" placeholder="Your Name / Company Name" style="padding: 0.8rem;">
                    </div>
                    <div class="mb-3">
                        <input type="email" class="form-control bg-dark border-secondary border-opacity-25 text-white" placeholder="Email Address" style="padding: 0.8rem;">
                    </div>
                    <div class="mb-4">
                        <textarea class="form-control bg-dark border-secondary border-opacity-25 text-white" rows="4" placeholder="How can we help you?" style="padding: 0.8rem;"></textarea>
                    </div>
                    <button type="button" class="btn btn-cyan w-100 py-3 fw-bold rounded">Send Message</button>
                </form>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer-dark text-start">
        <div class="container">
            <div class="row g-4 mb-5">
                <div class="col-lg-4 col-md-6 pe-5">
                    <h4 class="fw-bold mb-3">AutoHub <span class="text-pink">Marketplace</span></h4>
                    <p class="text-muted small">Premium vehicle marketplace for buying, selling, and leasing with institutional-grade assurance.</p>
                </div>
                <div class="col-lg-2 col-md-6">
                    <h6 class="text-white fw-bold mb-4">Useful Links</h6>
                    <a href="#">Home</a>
                    <a href="#">About Us</a>
                    <a href="#">Investors</a>
                    <a href="#">FAQ</a>
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms And Conditions</a>
                </div>
                <div class="col-lg-2 col-md-4">
                    <h6 class="text-white fw-bold mb-4">About Us</h6>
                    <a href="#">Company Overview</a>
                    <a href="#">Our Mission</a>
                    <a href="#">Careers</a>
                    <a href="#">Press & Media</a>
                </div>
                <div class="col-lg-2 col-md-4">
                    <h6 class="text-white fw-bold mb-4">How It Works</h6>
                    <a href="#">Buying Guide</a>
                    <a href="#">Selling Process</a>
                    <a href="#">Financing Explained</a>
                    <a href="#">Rental Terms</a>
                </div>
                <div class="col-lg-2 col-md-4">
                    <h6 class="text-white fw-bold mb-4">Solutions</h6>
                    <a href="#">Buy on Marketplace</a>
                    <a href="#">Sell on Marketplace</a>
                    <a href="#">Auction Events</a>
                    <a href="#">Finance Your Vehicle</a>
                </div>
            </div>
            
            <div class="row pt-4" style="border-top: 1px solid rgba(255,255,255,0.05);">
                <div class="col-md-6 mb-3 mb-md-0">
                    <p class="text-muted small mb-0">&copy; 2025 AutoHub Marketplace. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <span class="text-white fw-bold me-3">Contact Us</span>
                    <a href="#" class="d-inline-block text-muted me-3"><i class="fas fa-envelope text-pink me-1"></i> support@autohub.com</a>
                    <a href="#" class="d-inline-block text-muted"><i class="fas fa-phone-alt text-pink me-1"></i> 1800-ELITE-HUB</a>
                </div>
            </div>
        </div>
    </footer>


    <!-- Login/Signup Modal (Lazy Auth) -->
    <div class="modal fade" id="authModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content bg-dark-card text-white border border-secondary border-opacity-25 shadow-lg" style="border-radius: 12px; overflow: hidden;">
                <div class="row g-0">
                    <div class="col-md-5 d-none d-md-block" style="background: linear-gradient(135deg, var(--dark-bg), var(--pink-accent));">
                        <div class="p-4 text-white h-100 d-flex flex-column justify-content-center">
                            <h4 class="fw-bold mb-3">AutoHub</h4>
                            <p class="small opacity-75">Your journey to the perfect car starts here. Sign in to save, shortlist, and buy.</p>
                        </div>
                    </div>
                    <div class="col-md-7 p-4">
                        <div class="d-flex justify-content-between align-items-center mb-4">
                            <h5 class="fw-bold mb-0">Login or Sign Up</h5>
                            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                        </div>
                        <form id="lazyAuthForm">
                            <div class="mb-3">
                                <label class="form-label small text-muted">Email or Mobile Number</label>
                                <input type="text" id="lazyAuthUser" class="form-control bg-dark text-white border-secondary border-opacity-25" placeholder="Enter details" required>
                            </div>
                            <div class="mb-4">
                                <label class="form-label small text-muted">Password</label>
                                <input type="password" id="lazyAuthPass" class="form-control bg-dark text-white border-secondary border-opacity-25" placeholder="••••••••" required>
                            </div>
                            <button type="submit" class="btn btn-cyan w-100 fw-bold mb-3">Continue</button>

                            <div class="d-flex align-items-center mb-3">
                                <hr class="flex-grow-1 border-secondary border-opacity-50 m-0">
                                <span class="mx-3 text-muted small">OR</span>
                                <hr class="flex-grow-1 border-secondary border-opacity-50 m-0">
                            </div>

                            <button type="button" class="btn btn-outline-light w-100 fw-bold mb-4 d-flex align-items-center justify-content-center">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google" style="height: 18px; margin-right: 8px;">
                                Continue with Google
                            </button>

                            <div class="text-center mt-2">
                                <span class="text-muted small">New to AutoHub?</span>
                                <a href="register.html" class="text-decoration-none fw-bold small ms-1 text-cyan">Create New Account</a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/store.js"></script>
    <script src="js/data.js"></script>
    <script src="js/location.js"></script>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const user = store.getUser();
            const cart = store.getCart();

            // Setup Profile Area (Lazy Auth)
            const profileArea = document.getElementById('navProfileArea');
            if (user && user.isLoggedIn) {
                profileArea.innerHTML = `
                    <div class="dropdown">
                        <button class="btn btn-cyan rounded-pill px-4" id="profileDropdown" data-bs-toggle="dropdown">
                            <i class="fas fa-building me-1"></i> <span class="fw-bold">${user.companyName || user.firstName}</span>
                        </button>
                        <ul class="dropdown-menu dropdown-menu-end shadow bg-dark-card border-secondary border-opacity-25" style="border-radius: 8px;">
                            ${user.role === 'Dealer' ? '<li><a class="dropdown-item py-2 text-white" href="dealer-dashboard.html"><i class="fas fa-tachometer-alt me-3 text-cyan"></i>Dealer Dashboard</a></li>' : ''}
                            <li><a class="dropdown-item py-2 text-white" href="#"><i class="fas fa-user me-3 text-muted"></i>My Profile</a></li>
                            <li><a class="dropdown-item py-2 text-white" href="orders.html"><i class="fas fa-box me-3 text-muted"></i>My Orders</a></li>
                            <li><a class="dropdown-item py-2 text-white" href="my-quotes.html"><i class="fas fa-file-invoice me-3 text-muted"></i>Quotations</a></li>
                            <li><a class="dropdown-item py-2 text-white" href="my-test-drives.html"><i class="fas fa-car me-3 text-muted"></i>Test Drives</a></li>
                            <li><hr class="dropdown-divider border-secondary border-opacity-25"></li>
                            <li><a class="dropdown-item py-2 text-pink fw-bold" href="#" id="logoutBtn"><i class="fas fa-sign-out-alt me-3"></i>Logout</a></li>
                        </ul>
                    </div>
                `;
                document.getElementById('logoutBtn').addEventListener('click', (e) => {
                    e.preventDefault();
                    store.logoutUser();
                    window.location.reload();
                });
            } else {
                profileArea.innerHTML = `
                    <button class="btn btn-cyan rounded-pill px-4 fw-bold" id="navLoginBtn"><i class="fas fa-user me-1"></i> Register / Sign In</button>
                `;
                document.getElementById('navLoginBtn').addEventListener('click', () => {
                    const authModal = new bootstrap.Modal(document.getElementById('authModal'));
                    authModal.show();
                });
            }

            // Provide Cart Count
            const cartCounter = document.getElementById('cartCount');
            if(cartCounter) cartCounter.textContent = cart.items.length || 0;

            // Handle Lazy Login Submit
            document.getElementById('lazyAuthForm').addEventListener('submit', (e) => {
                e.preventDefault();
                const u = document.getElementById('lazyAuthUser').value;
                if (!u) return;
                store.saveUser({
                    firstName: u.split('@')[0],
                    email: u,
                    isLoggedIn: true
                });
                window.location.reload();
            });
        });
    </script>
</body>

</html>''')
