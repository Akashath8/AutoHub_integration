// =====================================================
// SELL FLOW — AutoHub Marketplace  (js/sell.js)
// =====================================================

const SELL_KEY = 'autohub_sell_state';

// ─── DATA ────────────────────────────────────────────

const SELL_BRANDS = [
    { name: 'TVS', abbr: 'T', color: '#c00' },
    { name: 'Bajaj', abbr: 'B', color: '#003da5' },
    { name: 'Hero', abbr: 'H', color: '#e5001d' },
    { name: 'Honda', abbr: 'Ho', color: '#e4002b' },
    { name: 'Royal Enfield', abbr: 'RE', color: '#1a4f2e' },
    { name: 'Yamaha', abbr: 'Y', color: '#000' },
    { name: 'Suzuki', abbr: 'Su', color: '#004b8d' },
    { name: 'KTM', abbr: 'K', color: '#f60' },
    { name: 'Kawasaki', abbr: 'Kw', color: '#1ba035' },
    { name: 'Triumph', abbr: 'Tr', color: '#222' },
];

const SELL_MODELS = {
    'TVS': ['Apache 150', 'Apache RR 310', 'Apache RTR 160', 'Apache RTR 160 2V', 'Apache RTR 160 4V', 'Apache RTR 165 RP', 'Apache RTR 180', 'Apache RTR 180 2V', 'Apache RTR 200 4V', 'Jupiter', 'Jupiter ZX', 'Ntorq 125', 'Ronin', 'Radeon', 'Sport', 'Star City+', 'XL 100'],
    'Bajaj': ['Avenger 150', 'Avenger 220', 'CT 100', 'Discover 110', 'Discover 125', 'Dominar 250', 'Dominar 400', 'Platina 100', 'Platina 110', 'Pulsar 125', 'Pulsar 150', 'Pulsar 180', 'Pulsar 200 NS', 'Pulsar 220F', 'Pulsar RS 200', 'Pulsar N160', 'Pulsar N250'],
    'Hero': ['Destini 125', 'Glamour', 'HF Dawn', 'HF Deluxe', 'Maestro Edge 110', 'Maestro Edge 125', 'Passion Pro', 'Passion XPro', 'Pleasure+', 'Splendor+', 'Splendor iSmart', 'Super Splendor', 'Xoom', 'Xtreme 160R', 'Xtreme 200S'],
    'Honda': ['Activa 5G', 'Activa 6G', 'Activa 125', 'CB350', 'CB350RS', 'CB500F', 'CBR 150R', 'Dio', 'Grazia 125', 'Shine 100', 'Shine 125', 'SP 125', 'Unicorn', 'X-Blade'],
    'Royal Enfield': ['Bullet 350', 'Classic 350', 'Classic 500', 'Himalayan', 'Hunter 350', 'Interceptor 650', 'Meteor 350', 'Scram 411', 'Shotgun 650', 'Super Meteor 650'],
    'Yamaha': ['Aerox 155', 'FZ-FI', 'FZ-S FI', 'FZ-X', 'FZS 25', 'MT-15', 'R15 S', 'R15 V4', 'Ray ZR 125', 'Ray ZR Street Rally', 'Saluto', 'YZF R3'],
    'Suzuki': ['Access 125', 'Avenis 125', 'Burgman Street 125', 'Gixxer', 'Gixxer 250', 'Gixxer SF', 'Intruder'],
    'KTM': ['125 Duke', '200 Duke', '250 Adventure', '250 Duke', '390 Adventure', '390 Duke', 'RC 200', 'RC 390'],
    'Kawasaki': ['Ninja 300', 'Ninja 400', 'Ninja 650', 'Ninja ZX-10R', 'Versys 650', 'W175', 'Z650', 'Z900'],
    'Triumph': ['Bonneville T100', 'Bonneville T120', 'Speed 400', 'Street Triple', 'Tiger 900', 'Trident 660'],
};

// Variants: most models have a single variant same as model name.
// Populated dynamically.
function getVariants(model) {
    const overrides = {
        'Apache RTR 160': ['RTR 160 Single Disc', 'RTR 160 Double Disc'],
        'Apache RTR 160 2V': ['RTR 160 2V Disc', 'RTR 160 2V Drum'],
        'Apache RTR 160 4V': ['RTR 160 4V Single', 'RTR 160 4V Double', 'RTR 160 4V Special Edition'],
        'Apache RTR 180': ['RTR 180 Disc', 'RTR 180 Drum'],
        'Apache RTR 200 4V': ['RTR 200 4V Single', 'RTR 200 4V Double'],
        'Pulsar 150': ['Pulsar 150 Single Disc', 'Pulsar 150 Twin Disc'],
        'Activa 6G': ['Activa 6G DLX', 'Activa 6G STD'],
        'FZ-FI': ['FZ V3.0', 'FZ V2.0'],
        'R15 V4': ['R15 V4 STD', 'R15 V4 M GP Edition'],
    };
    return overrides[model] || [model];
}

const SELL_STATES = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
    'Chhattisgarh', 'Dadra & Nagar Haveli', 'Delhi', 'Goa', 'Gujarat',
    'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka',
    'Kerala', 'Ladakh', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
    'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
    'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
    'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
];

const RTO_MAP = {
    'Karnataka': { prefix: 'KA', count: 57 },
    'Tamil Nadu': { prefix: 'TN', count: 99 },
    'Maharashtra': { prefix: 'MH', count: 50 },
    'Delhi': { prefix: 'DL', count: 12 },
    'Kerala': { prefix: 'KL', count: 30 },
    'Gujarat': { prefix: 'GJ', count: 38 },
    'Uttar Pradesh': { prefix: 'UP', count: 90 },
    'West Bengal': { prefix: 'WB', count: 80 },
    'Rajasthan': { prefix: 'RJ', count: 50 },
    'Telangana': { prefix: 'TS', count: 35 },
    'Punjab': { prefix: 'PB', count: 30 },
    'Madhya Pradesh': { prefix: 'MP', count: 50 },
    'Andhra Pradesh': { prefix: 'AP', count: 37 },
    'Bihar': { prefix: 'BR', count: 60 },
    'Haryana': { prefix: 'HR', count: 99 },
    'Chhattisgarh': { prefix: 'CG', count: 30 },
    'Odisha': { prefix: 'OD', count: 31 },
    'Goa': { prefix: 'GA', count: 12 },
    'Assam': { prefix: 'AS', count: 30 },
    'Jharkhand': { prefix: 'JH', count: 25 },
    'Himachal Pradesh': { prefix: 'HP', count: 80 },
    'Uttarakhand': { prefix: 'UK', count: 20 },
    'Chandigarh': { prefix: 'CH', count: 4 },
    'default': { prefix: 'XX', count: 20 },
};

function getRTOs(stateName) {
    const entry = RTO_MAP[stateName] || RTO_MAP['default'];
    const list = [];
    for (let i = 1; i <= entry.count; i++) {
        list.push(entry.prefix + String(i).padStart(2, '0'));
    }
    return list;
}

// Base prices for price estimation (INR)
const BASE_PRICES = {
    'TVS': { 'Apache 150': 95000, 'Apache RR 310': 250000, 'Apache RTR 160': 115000, 'Apache RTR 160 2V': 120000, 'Apache RTR 160 4V': 130000, 'Apache RTR 165 RP': 140000, 'Apache RTR 180': 125000, 'Apache RTR 180 2V': 130000, 'Apache RTR 200 4V': 148000, 'Jupiter': 78000, 'Ntorq 125': 92000, 'Ronin': 155000, default: 80000 },
    'Bajaj': { 'Pulsar 150': 120000, 'Pulsar 180': 130000, 'Pulsar 200 NS': 155000, 'Pulsar 220F': 140000, 'Pulsar RS 200': 165000, 'Dominar 400': 230000, 'Dominar 250': 195000, 'Avenger 220': 145000, default: 85000 },
    'Hero': { 'Splendor+': 75000, 'HF Deluxe': 70000, 'Passion Pro': 78000, 'Xtreme 160R': 130000, 'Xtreme 200S': 160000, 'Glamour': 82000, default: 72000 },
    'Honda': { 'Activa 6G': 80000, 'Activa 125': 90000, 'CB350': 195000, 'CB350RS': 210000, 'CB500F': 520000, 'Unicorn': 112000, 'SP 125': 88000, default: 75000 },
    'Royal Enfield': { 'Classic 350': 195000, 'Meteor 350': 215000, 'Hunter 350': 170000, 'Himalayan': 225000, 'Interceptor 650': 310000, 'Super Meteor 650': 345000, default: 180000 },
    'Yamaha': { 'R15 V4': 180000, 'MT-15': 165000, 'FZ-S FI': 115000, 'FZ-FI': 110000, 'FZ-X': 120000, 'Aerox 155': 145000, default: 100000 },
    'Suzuki': { 'Access 125': 90000, 'Gixxer': 120000, 'Gixxer 250': 190000, 'Burgman Street 125': 98000, default: 85000 },
    'KTM': { '200 Duke': 190000, '250 Duke': 245000, '390 Duke': 320000, '125 Duke': 155000, 'RC 390': 350000, default: 175000 },
    'Kawasaki': { 'Ninja 300': 320000, 'Ninja 400': 530000, 'Z650': 710000, 'Versys 650': 720000, default: 300000 },
    'Triumph': { 'Speed 400': 230000, 'Trident 660': 720000, 'Street Triple': 950000, default: 400000 },
};

const CURRENT_YEAR = 2026;

function calcPrice(brand, model, year, owner, kms) {
    const brandPrices = BASE_PRICES[brand] || { default: 100000 };
    let base = brandPrices[model] || brandPrices['default'] || 100000;

    // Year depreciation
    const age = CURRENT_YEAR - parseInt(year, 10);
    let depRate = 0;
    if (age <= 0) depRate = 0;
    else if (age === 1) depRate = 0.20;
    else if (age === 2) depRate = 0.32;
    else if (age === 3) depRate = 0.42;
    else if (age === 4) depRate = 0.49;
    else depRate = Math.min(0.49 + (age - 4) * 0.05, 0.75);

    let price = base * (1 - depRate);

    // Mileage adjustment
    const k = parseInt(kms, 10) || 0;
    if (k < 5000) price *= 1.02;
    else if (k < 20000) price *= 1.0;
    else if (k < 40000) price *= 0.96;
    else if (k < 60000) price *= 0.91;
    else price *= 0.85;

    // Ownership
    if (owner === '2nd Owner') price *= 0.94;
    else if (owner === '3rd Owner') price *= 0.88;

    price = Math.round(price / 500) * 500;
    return { mid: price, low: Math.round(price * 0.93 / 500) * 500, high: Math.round(price * 1.08 / 500) * 500 };
}

// ─── STATE MANAGEMENT ────────────────────────────────

function getSellState() {
    try {
        const s = sessionStorage.getItem(SELL_KEY);
        return s ? JSON.parse(s) : freshSellState();
    } catch (e) { return freshSellState(); }
}
function saveSellState(state) {
    sessionStorage.setItem(SELL_KEY, JSON.stringify(state));
}
function freshSellState() {
    return { step: 1, brand: '', model: '', variant: '', year: '', state: '', rto: '', owner: '', kms: '', pincode: '' };
}
function clearSellState() {
    sessionStorage.removeItem(SELL_KEY);
}

// ─── SELL LANDING PAGE ────────────────────────────────

const sellLanding = {
    init() {
        // Show selected city
        const city = localStorage.getItem('autohub_selected_city');
        const cityEl = document.getElementById('sellHeroCity');
        if (cityEl && city) cityEl.textContent = city;

        // Populate mini brand grid (3 brands in stage 2)
        this._renderBrandMini();

        // If sell state already has a pincode, go straight to stage 2
        const state = getSellState();
        if (state.pincode && state.pincode.length === 6) {
            document.getElementById('pincodeDisplay').value = state.pincode;
            this._showStage2();
        }
    },

    onPincodeInput(el) {
        const val = el.value.replace(/\D/g, '');
        el.value = val;
        const btn = document.getElementById('proceedBtn');
        const ck = document.getElementById('pincodeCheck');
        if (val.length === 6) {
            btn.disabled = false;
            ck.style.display = 'flex';
            ck.innerHTML = '<i class="fas fa-check-circle text-success"></i>';
        } else {
            btn.disabled = true;
            ck.style.display = 'none';
        }
    },

    proceed() {
        const pincode = document.getElementById('pincodeInput').value.trim();
        if (pincode.length !== 6) return;
        const state = getSellState();
        state.pincode = pincode;
        saveSellState(state);
        document.getElementById('pincodeDisplay').value = pincode;
        this._showStage2();
    },

    _showStage2() {
        document.getElementById('stage1').style.display = 'none';
        document.getElementById('stage2').style.display = 'block';
        this._renderBrandMini();
    },

    _renderBrandMini() {
        const el = document.getElementById('brandMiniGrid');
        if (!el) return;
        const mini = SELL_BRANDS.slice(0, 3);
        el.innerHTML = mini.map(b => `
            <div class="brand-mini-card" onclick="sellLanding.selectBrand('${b.name}')">
                <div class="brand-mini-logo" style="background:${b.color};">${b.abbr}</div>
                <div class="brand-mini-name">${b.name}</div>
            </div>
        `).join('');
    },

    getEstimateByReg() {
        const reg = document.getElementById('regInput').value.trim();
        if (!reg) { alert('Please enter a vehicle registration number.'); return; }
        const state = getSellState();
        state.regNumber = reg;
        state.step = 1; // Start from brand selection
        saveSellState(state);
        window.location.href = 'sell-wizard.html';
    },

    selectBrand(brand) {
        const state = getSellState();
        state.brand = brand;
        state.model = '';
        state.variant = '';
        state.year = '';
        state.state = '';
        state.rto = '';
        state.owner = '';
        state.kms = '';
        state.step = 2; // Jump to Model step
        saveSellState(state);
        window.location.href = 'sell-wizard.html';
    },

    viewAllBrands(e) {
        if (e) e.preventDefault();
        const state = getSellState();
        state.step = 1;
        saveSellState(state);
        window.location.href = 'sell-wizard.html';
    },
};

// ─── SELL WIZARD ──────────────────────────────────────

const WIZARD_STEPS = [
    { id: 'brand', label: 'Brand', count: '1/11', title: 'Select the', highlight: 'Brand', suffix: 'of your two-wheeler', search: false, grid: false },
    { id: 'model', label: 'Model', count: '2/11', title: 'Select the', highlight: 'Model', suffix: 'of your two-wheeler', search: true, grid: false },
    { id: 'variant', label: 'Variant', count: '3/11', title: 'Select the', highlight: 'Variant', suffix: 'of your two-wheeler', search: false, grid: false },
    { id: 'year', label: 'Year', count: '4/11', title: 'Select the', highlight: 'Manufacturing Year', suffix: 'of your two-wheeler', search: false, grid: false },
    { id: 'state', label: 'State', count: '5/11', title: 'Select the', highlight: 'Registered State', suffix: 'of your two-wheeler', search: false, grid: false },
    { id: 'rto', label: 'RTO', count: '6/11', title: 'Select', highlight: 'RTO', suffix: '', search: true, grid: true },
    { id: 'owner', label: 'Owner', count: '7/11', title: 'Select the', highlight: 'Ownership History', suffix: 'of your two-wheeler', search: false, grid: false },
    { id: 'kms', label: 'KMs Driven', count: '8/11', title: 'Enter Exact', highlight: 'Odometer Reading', suffix: '', search: false, grid: false, kmsInput: true },
];

const sellWizard = {
    _allItems: [],   // for search filtering

    init() {
        const state = getSellState();
        this.renderTabs(state);
        this.renderStep(state);
    },

    goBack() {
        const state = getSellState();
        if (state.step <= 1) {
            window.location.href = 'sell.html';
            return;
        }
        state.step--;
        // Clear the value for step we're going back from
        const stepDef = WIZARD_STEPS[state.step - 1]; // going back means we clear current
        if (stepDef) state[stepDef.id] = '';
        saveSellState(state);
        this.renderTabs(state);
        this.renderStep(state);
    },

    renderTabs(state) {
        const container = document.getElementById('wizardTabs');
        if (!container) return;
        container.innerHTML = WIZARD_STEPS.map((s, i) => {
            const stepNum = i + 1;
            const isDone = stepNum < state.step;
            const isCurr = stepNum === state.step;
            let cls = 'wizard-tab';
            if (isDone) cls += ' done';
            if (isCurr) cls += ' current';
            const badge = isDone ? '<span class="tab-done-dot"><i class="fas fa-check"></i></span>' : '';
            return `<button class="${cls}" onclick="sellWizard.jumpToStep(${stepNum})">${badge}${s.label}</button>`;
        }).join('');
    },

    jumpToStep(n) {
        const state = getSellState();
        // Only allow jumping to completed steps or current
        if (n > state.step) return;
        state.step = n;
        // Clear all steps from n onward
        WIZARD_STEPS.slice(n - 1).forEach(s => state[s.id] = '');
        saveSellState(state);
        this.renderTabs(state);
        this.renderStep(state);
    },

    renderStep(state) {
        const stepIdx = (state.step || 1) - 1;
        const def = WIZARD_STEPS[Math.min(stepIdx, WIZARD_STEPS.length - 1)];
        if (!def) return;

        // Breadcrumb
        const crumbs = [];
        if (state.brand) crumbs.push(state.brand);
        if (state.year) crumbs.push(state.year);
        if (state.model) crumbs.push(state.model);
        if (state.variant && state.variant !== state.model) crumbs.push(state.variant);
        document.getElementById('wizardBreadcrumb').textContent = crumbs.length ? crumbs.join(' ') : 'Select Brand';

        // Title
        document.getElementById('stepTitle').innerHTML =
            `${def.title} <span class="text-accent-orange">${def.highlight}</span>${def.suffix ? ' ' + def.suffix : ''}`;
        document.getElementById('stepCounter').textContent = def.count;

        // Search bar
        const searchBar = document.getElementById('wizardSearchBar');
        const searchInput = document.getElementById('wizardSearch');
        searchBar.style.display = def.search ? 'flex' : 'none';
        if (searchInput) searchInput.value = '';

        // KMs section
        document.getElementById('kmsSection').style.display = def.kmsInput ? 'flex' : 'none';
        document.getElementById('continueWrap').style.display = def.kmsInput ? 'block' : 'none';

        // Render items
        const items = this._getItems(def.id, state);
        this._allItems = items;
        this._renderItems(items, def);
    },

    _getItems(stepId, state) {
        switch (stepId) {
            case 'brand': return SELL_BRANDS.map(b => ({ label: b.name, meta: b }));
            case 'model': return (SELL_MODELS[state.brand] || []).map(m => ({ label: m }));
            case 'variant': return getVariants(state.model).map(v => ({ label: v }));
            case 'year': return Array.from({ length: 15 }, (_, i) => ({ label: String(CURRENT_YEAR - i) }));
            case 'state': return SELL_STATES.map(s => ({ label: s }));
            case 'rto': return getRTOs(state.state).map(r => ({ label: r }));
            case 'owner': return [
                { label: '1st Owner', icon: 'fas fa-user', iconBg: '#e85b3a' },
                { label: '2nd Owner', icon: 'fas fa-user-friends', iconBg: '#e85b3a' },
                { label: '3rd Owner', icon: 'fas fa-users', iconBg: '#e85b3a' },
            ];
            case 'kms': return [];
            default: return [];
        }
    },

    _renderItems(items, def) {
        const area = document.getElementById('wizardItems');
        if (!area) return;
        if (def.kmsInput) { area.innerHTML = ''; return; }

        if (def.id === 'brand') {
            area.innerHTML = `<div class="brand-grid-full">${items.map(item => `
                    <div class="brand-card-full" onclick="sellWizard.selectItem('brand','${item.label}')">
                        <div class="brand-logo-full" style="background:${item.meta.color};">${item.meta.abbr}</div>
                        <div class="brand-name-full">${item.label}</div>
                    </div>
                `).join('')
                }</div>`;
        } else if (def.id === 'rto') {
            area.innerHTML = `<div class="rto-grid">${items.map(item => `<button class="rto-cell" onclick="sellWizard.selectItem('rto','${item.label}')">${item.label}</button>`).join('')
                }</div>`;
        } else if (def.id === 'owner') {
            area.innerHTML = items.map(item => `
                <div class="owner-row" onclick="sellWizard.selectItem('owner','${item.label}')">
                    <span class="owner-label">${item.label}</span>
                    <span class="owner-icon-wrap" style="background:${item.iconBg};"><i class="${item.icon}"></i></span>
                </div>
            `).join('');
        } else {
            area.innerHTML = items.map(item => `
                <div class="list-row" onclick="sellWizard.selectItem('${def.id}','${item.label}')">${item.label}</div>
            `).join('');
        }
    },

    filterItems(query) {
        const state = getSellState();
        const stepIdx = (state.step || 1) - 1;
        const def = WIZARD_STEPS[stepIdx];
        const q = query.toLowerCase();
        const filtered = q ? this._allItems.filter(i => i.label.toLowerCase().includes(q)) : this._allItems;
        this._renderItems(filtered, def);
    },

    selectItem(stepId, value) {
        const state = getSellState();
        state[stepId] = value;

        const nextStep = state.step + 1;
        if (nextStep > WIZARD_STEPS.length) {
            // All steps done — show phone panel
            saveSellState(state);
            this.renderTabs(state);
            this.renderStep(state);
            this.showPhonePanel(state);
        } else {
            state.step = nextStep;
            saveSellState(state);
            this.renderTabs(state);
            this.renderStep(state);
        }
    },

    continueFromKms() {
        const kmsVal = document.getElementById('kmsInput').value.trim();
        if (!kmsVal || parseInt(kmsVal, 10) < 0) {
            document.getElementById('kmsInput').focus();
            return;
        }
        const state = getSellState();
        state.kms = kmsVal;
        saveSellState(state);
        this.showPhonePanel(state);
    },

    showPhonePanel(state) {
        // Show a blurred price teaser
        const estimate = calcPrice(state.brand, state.model, state.year, state.owner, state.kms);
        document.getElementById('phonePanelPrice').textContent = '₹ ██████';

        document.getElementById('phoneOverlay').style.display = 'block';
        const panel = document.getElementById('phonePanel');
        panel.classList.add('open');
        setTimeout(() => { document.getElementById('phoneInput').focus(); }, 300);
    },

    closePhonePanel() {
        document.getElementById('phoneOverlay').style.display = 'none';
        document.getElementById('phonePanel').classList.remove('open');
    },

    submitPhone() {
        const phone = document.getElementById('phoneInput').value.trim();
        if (phone.length !== 10 || !/^\d+$/.test(phone)) {
            document.getElementById('phoneInput').classList.add('is-invalid');
            return;
        }
        document.getElementById('phoneInput').classList.remove('is-invalid');
        this.closePhonePanel();
        this.showPriceEstimate(phone);
    },

    showPriceEstimate(phone) {
        const state = getSellState();
        const est = calcPrice(state.brand, state.model, state.year, state.owner, state.kms);

        const vehicleName = [state.brand, state.year, state.model].filter(Boolean).join(' ');
        document.getElementById('peVehicleName').textContent = vehicleName;

        // Animated price reveal
        document.getElementById('pePriceAmount').textContent = '₹ ' + est.mid.toLocaleString('en-IN');
        document.getElementById('pePriceRange').textContent =
            '₹ ' + est.low.toLocaleString('en-IN') + ' – ₹ ' + est.high.toLocaleString('en-IN');

        // Summary chips
        const summaryItems = [
            { icon: 'fas fa-tag', label: state.brand },
            { icon: 'fas fa-motorcycle', label: state.model },
            { icon: 'fas fa-layer-group', label: state.variant },
            { icon: 'fas fa-calendar', label: state.year },
            { icon: 'fas fa-map-marker-alt', label: state.state },
            { icon: 'fas fa-id-card', label: state.rto },
            { icon: 'fas fa-user', label: state.owner },
            { icon: 'fas fa-tachometer-alt', label: state.kms ? state.kms + ' kms' : '' },
        ].filter(i => i.label);

        document.getElementById('peSummary').innerHTML = summaryItems.map(item => `
            <div class="pe-chip">
                <i class="${item.icon} pe-chip-icon"></i>
                <span>${item.label}</span>
            </div>
        `).join('');

        document.getElementById('priceEstimateScreen').style.display = 'flex';
        document.getElementById('priceEstimateScreen').scrollTop = 0;

        // Save phone in state
        state.phone = phone;
        saveSellState(state);
    },

    bookEvaluation() {
        const state = getSellState();
        // Save as a quotation in the store
        const quotation = {
            id: 'SELL-' + Date.now(),
            type: 'Sell Evaluation',
            vehicle: [state.brand, state.model, state.variant].filter(Boolean).join(' '),
            year: state.year,
            kms: state.kms,
            state: state.state,
            rto: state.rto,
            owner: state.owner,
            phone: state.phone,
            date: new Date().toLocaleDateString('en-IN'),
            status: 'Evaluation Scheduled',
        };
        if (typeof store !== 'undefined' && store.addQuotation) {
            store.addQuotation(quotation);
        }
        clearSellState();
        window.location.href = 'my-quotes.html';
    },
};
