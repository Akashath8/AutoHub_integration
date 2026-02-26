/**
 * AutoHub & LOS - Central State Store
 * Handles persistence to localStorage for User, Cart, and Loan Application.
 */

class Store {
    constructor() {
        this.STORAGE_KEYS = {
            USER: 'autohub_user',
            CART: 'autohub_cart',
            LOAN_APP: 'los_application',
            ORDERS: 'autohub_orders',
            QUOTATIONS: 'autohub_quotations',
            SELECTED_FINANCE: 'los_selected_finance'
        };

        // Initialize empty states if not present
        if (!this.getUser()) {
            // Mock persistent user for demo if needed, or leave null
        }
        if (!this.getCart()) {
            this.saveCart({ items: [], total: 0 });
        }
        if (!this.getOrders()) {
            this.saveOrders([]);
        }
    }

    // --- User Management ---
    getUser() {
        return JSON.parse(localStorage.getItem(this.STORAGE_KEYS.USER));
    }

    saveUser(user) {
        localStorage.setItem(this.STORAGE_KEYS.USER, JSON.stringify(user));
    }

    logoutUser() {
        localStorage.removeItem(this.STORAGE_KEYS.USER);
    }

    // --- Cart Management ---
    getCart() {
        return JSON.parse(localStorage.getItem(this.STORAGE_KEYS.CART));
    }

    saveCart(cart) {
        localStorage.setItem(this.STORAGE_KEYS.CART, JSON.stringify(cart));
    }

    addToCart(product) {
        const cart = this.getCart();
        // Simple logic: If product exists, increment qty, else add
        const existingItem = cart.items.find(item => item.id === product.id);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.items.push({ ...product, quantity: 1 });
        }
        this.recalculateCartTotal(cart);
        this.saveCart(cart);
    }

    clearCart() {
        this.saveCart({ items: [], total: 0 });
    }

    recalculateCartTotal(cart) {
        cart.total = cart.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    }

    // --- Special Finance Selection Management ---
    getSelectedForFinance() {
        return JSON.parse(localStorage.getItem(this.STORAGE_KEYS.SELECTED_FINANCE)) || [];
    }

    saveSelectedForFinance(items) {
        localStorage.setItem(this.STORAGE_KEYS.SELECTED_FINANCE, JSON.stringify(items));
    }

    clearSelectedForFinance() {
        localStorage.removeItem(this.STORAGE_KEYS.SELECTED_FINANCE);
    }

    // --- Loan Application Management ---
    getApplication() {
        return JSON.parse(localStorage.getItem(this.STORAGE_KEYS.LOAN_APP)) || {};
    }

    saveApplication(data) {
        const current = this.getApplication();
        const updated = { ...current, ...data };
        localStorage.setItem(this.STORAGE_KEYS.LOAN_APP, JSON.stringify(updated));
    }

    clearApplication() {
        localStorage.removeItem(this.STORAGE_KEYS.LOAN_APP);
    }

    // --- Order History ---
    getOrders() {
        return JSON.parse(localStorage.getItem(this.STORAGE_KEYS.ORDERS)) || [];
    }

    saveOrders(orders) {
        localStorage.setItem(this.STORAGE_KEYS.ORDERS, JSON.stringify(orders));
    }

    addOrder(order) {
        const orders = this.getOrders();
        orders.unshift(order); // Add to top
        this.saveOrders(orders);
    }

    getQuotations() {
        const quotes = JSON.parse(localStorage.getItem(this.STORAGE_KEYS.QUOTATIONS));
        if (quotes && quotes.length > 0) {
            return quotes;
        }

        // Seed with a mock quotation of a single seller having multiple vehicles
        const seededQuotes = [
            {
                id: 'QT-849201',
                category: 'Pre-Owned',
                type: 'Buy',
                brand: 'Multiple Brands',
                productName: 'Multiple Vehicles',
                price: 2450650,
                offerPrice: 2400000,
                quantity: 2,
                sellerName: 'Deshpande Auto, Pune',
                receivedDate: new Date().toLocaleDateString('en-GB'),
                vehicles: [
                    {
                        id: 'v1',
                        name: 'Hyundai i10 Neo',
                        brand: 'Hyundai',
                        price: 850650,
                        year: 2022,
                        km: 42000,
                        image: 'https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&q=80&w=400'
                    },
                    {
                        id: 'v5',
                        name: 'Mahindra Thar',
                        brand: 'Mahindra',
                        price: 1600000,
                        year: 2022,
                        km: 15000,
                        image: 'https://images.unsplash.com/photo-1606161290610-c529a674d89a?auto=format&fit=crop&q=80&w=400'
                    }
                ]
            }
        ];
        this.saveQuotations(seededQuotes);
        return seededQuotes;
    }

    saveQuotations(quotes) {
        localStorage.setItem(this.STORAGE_KEYS.QUOTATIONS, JSON.stringify(quotes));
    }

    addQuotation(quote) {
        const quotes = this.getQuotations();
        quotes.unshift(quote);
        this.saveQuotations(quotes);
    }
}

// Export a singleton instance
const store = new Store();
