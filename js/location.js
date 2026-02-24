/**
 * AutoHub - Location & City Selection Manager
 * Manages city selection via localStorage and provides the city-picker modal.
 */

const LOCATION_KEY = 'autohub_selected_city';

// --- City Data ---
const POPULAR_CITIES = ['Bangalore', 'Chennai', 'Pune', 'Mumbai'];

const MORE_CITIES = [
    'Ahmedabad', 'Coimbatore', 'Chengalpattu', 'Cuddalore', 'Davanagere',
    'Delhi', 'Hassan', 'Hosur', 'Hyderabad', 'Jaipur', 'Kallakurichi',
    'Kolar Gold Fields', 'Krishnagiri', 'Kumbakonam', 'Madurai', 'Mysore',
    'New Delhi', 'Surat', 'Thiruvananthapuram', 'Tiruchirappalli', 'Vellore'
];

// --- Storage Helpers ---
function getSelectedCity() {
    return localStorage.getItem(LOCATION_KEY) || null;
}

function setSelectedCity(city) {
    localStorage.setItem(LOCATION_KEY, city);
}

// --- Navbar Location Button Update ---
function updateNavbarLocation() {
    const btn = document.getElementById('navLocationBtn');
    if (!btn) return;
    const city = getSelectedCity();
    btn.innerHTML = `<i class="fas fa-map-marker-alt me-1 text-accent"></i> ${city || 'Select City'} <i class="fas fa-chevron-down ms-1" style="font-size:0.7rem;"></i>`;
}

// --- Modal Injection ---
function injectCityModal() {
    if (document.getElementById('citySelectionModal')) return; // Already injected

    const modalHTML = `
    <div class="modal fade" id="citySelectionModal" tabindex="-1" aria-labelledby="cityModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-md">
            <div class="modal-content city-modal-content">
                <div class="modal-header border-0 pb-0">
                    <button type="button" class="btn btn-link text-dark p-0 me-2" data-bs-dismiss="modal">
                        <i class="fas fa-arrow-left"></i>
                    </button>
                    <h5 class="modal-title fw-bold" id="cityModalLabel">Select Your City</h5>
                    <button type="button" class="btn-close ms-auto" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body pt-3">
                    <!-- Share Location Banner -->
                    <div class="city-location-banner mb-3 p-3 rounded-2">
                        <p class="mb-2 small fw-semibold">Help us find the <span class="text-accent fw-bold">nearest vehicle</span> for you in no time 🏍️</p>
                        <button class="btn btn-outline-warning w-100 py-2 fw-semibold" id="shareLocationBtn">
                            <i class="fas fa-location-arrow me-2"></i> Share Location
                        </button>
                    </div>

                    <div class="text-center text-muted small my-2">— OR —</div>

                    <!-- Search City -->
                    <div class="input-group mb-4">
                        <span class="input-group-text bg-light border-end-0"><i class="fas fa-search text-muted"></i></span>
                        <input type="text" id="citySearchInput" class="form-control border-start-0 bg-light" placeholder="Search City...">
                    </div>

                    <!-- Popular Cities -->
                    <p class="text-muted small fw-semibold mb-2">Popular Cities</p>
                    <div class="row g-2 mb-4" id="popularCitiesGrid">
                        ${POPULAR_CITIES.map(city => `
                        <div class="col-6">
                            <button class="btn btn-light city-select-btn w-100 text-start py-2 px-3 border" data-city="${city}">
                                <i class="fas fa-city text-muted me-2 small"></i>${city}
                            </button>
                        </div>`).join('')}
                    </div>

                    <!-- More Cities -->
                    <p class="text-muted small fw-semibold mb-2">More Cities</p>
                    <div class="city-more-grid" id="moreCitiesGrid">
                        ${MORE_CITIES.map(city => `
                        <button class="btn btn-outline-secondary btn-sm city-select-btn" data-city="${city}">${city}</button>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>
    </div>`;

    document.body.insertAdjacentHTML('beforeend', modalHTML);

    // Wire up city buttons
    document.querySelectorAll('.city-select-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            onCitySelected(btn.dataset.city);
        });
    });

    // Search filter
    document.getElementById('citySearchInput').addEventListener('input', function () {
        const q = this.value.toLowerCase();
        document.querySelectorAll('.city-select-btn').forEach(btn => {
            btn.closest('.col-6')
                ? btn.closest('.col-6').style.display = btn.dataset.city.toLowerCase().includes(q) ? '' : 'none'
                : btn.style.display = btn.dataset.city.toLowerCase().includes(q) ? '' : 'none';
        });
    });

    // Share location via geolocation
    document.getElementById('shareLocationBtn').addEventListener('click', () => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                () => {
                    // For demo: just use a default city since we don't do reverse geocoding
                    onCitySelected('Bangalore');
                },
                () => alert('Location access denied. Please select a city manually.')
            );
        } else {
            alert('Geolocation is not supported by your browser.');
        }
    });
}

// --- City Selection Handler ---
let _pendingMode = null;

function onCitySelected(city) {
    setSelectedCity(city);
    updateNavbarLocation();

    const modal = bootstrap.Modal.getInstance(document.getElementById('citySelectionModal'));
    if (modal) modal.hide();

    if (_pendingMode) {
        window.location.href = `listing.html?mode=${_pendingMode}&city=${encodeURIComponent(city)}`;
        _pendingMode = null;
    }
}

// --- Public: Handle Buy/Rent/Sell button clicks ---
function handleModeClick(mode) {
    // Sell always goes to the dedicated sell flow page
    if (mode === 'sell') {
        window.location.href = 'sell.html';
        return;
    }
    const city = getSelectedCity();
    if (city) {
        // City already selected — go directly to listing
        window.location.href = `listing.html?mode=${mode}&city=${encodeURIComponent(city)}`;
    } else {
        // No city — show modal first (for Buy/Rent)
        _pendingMode = mode;
        const modal = new bootstrap.Modal(document.getElementById('citySelectionModal'));
        modal.show();
    }
}

// --- Navbar Dropdown City Selection ---
function handleNavLocationClick(city) {
    setSelectedCity(city);
    updateNavbarLocation();
    // Close dropdown
    bootstrap.Dropdown.getInstance(document.getElementById('navLocationToggle'))?.hide();
}

// --- Initialise on DOMContentLoaded ---
document.addEventListener('DOMContentLoaded', () => {
    injectCityModal();
    updateNavbarLocation();

    // Wire Buy/Rent/Sell nav buttons
    document.querySelectorAll('[data-mode]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            handleModeClick(btn.dataset.mode);
        });
    });

    // Wire navbar location dropdown city items
    document.querySelectorAll('[data-nav-city]').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            handleNavLocationClick(item.dataset.navCity);
        });
    });
});
