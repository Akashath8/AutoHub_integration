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
            SELECTED_FINANCE: 'los_selected_finance',
            TEST_DRIVES: 'autohub_test_drives'
        };

        // Initialize empty states if not present
        if (!this.getUser()) {
            // No default mock user to force login/register flow, or leave null for demo
        }
        if (!this.getCart()) {
            this.saveCart({ items: [], total: 0 });
        }

    }



    updateOrder(updatedOrder) {
        const orders = this.getOrders();
        const index = orders.findIndex(o => o.id === updatedOrder.id);
        if (index !== -1) {
            orders[index] = updatedOrder;
            this.saveOrders(orders);
        }
    }

    getOrderById(id) {
        return this.getOrders().find(o => o.id === id);
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
        const staticOrders = [
            {
                id: "ORD-1001",
                orderId: "ORD-1001",
                productName: "Tata Signa Truck",
                dealerName: "Deshpande Commercials",
                invoiceNo: "INV-2023-0104",
                totalAmount: 750000,
                paidAmount: 750000,
                outstandingAmount: 0,
                status: "PAID",
                paymentStatus: "Paid",
                delivery: "Delivered",
                lifecycleStep: 9,
                deliveryStage: "Delivery Confirmed",
                documents: [
                    { name: 'Invoice Generated', status: 'Completed', responsible: 'Dealer', date: '24 Oct 2023' },
                    { name: 'RC Transfer Initiated', status: 'Completed', responsible: 'Dealer', date: '25 Oct 2023' },
                    { name: 'RC Transfer Completed', status: 'Completed', responsible: 'RTO', date: '30 Oct 2023' },
                    { name: 'Insurance Transfer', status: 'Completed', responsible: 'Dealer', date: '01 Nov 2023' },
                    { name: 'Hypothecation Registration', status: 'Completed', responsible: 'Bank', date: '02 Nov 2023' },
                    { name: 'Vehicle Inspection', status: 'Completed', responsible: 'Logistics', date: '03 Nov 2023' },
                    { name: 'Delivery Challan', status: 'Completed', responsible: 'Dealer', date: '04 Nov 2023' }
                ],
                timeline: [
                    { title: 'Order Created', date: '22 Oct 10:30 AM', status: 'completed' },
                    { title: 'Payment Completed', date: '26 Oct 14:00 PM', status: 'completed', amount: 750000 },
                    { title: 'Final Delivery Completed', date: '05 Nov 11:45 AM', status: 'completed' }
                ]
            },
            {
                id: "ORD-1002",
                orderId: "ORD-1002",
                productName: "Ashok Leyland Dost+",
                dealerName: "Northwest Commercials",
                invoiceNo: "INV-2023-0145",
                totalAmount: 750000,
                paidAmount: 250000,
                outstandingAmount: 500000,
                status: "PARTIAL",
                paymentStatus: "Partial",
                delivery: "Blocked",
                lifecycleStep: 8,
                deliveryStage: "Blocked",
                documents: [
                    { name: 'Invoice Generated', status: 'Completed', responsible: 'Dealer', date: '24 Oct 2023' },
                    { name: 'RC Transfer Initiated', status: 'In Progress', responsible: 'Dealer' },
                    { name: 'Insurance Transfer', status: 'In Progress', responsible: 'Dealer' }
                ],
                timeline: [
                    { title: 'Order Created', date: '22 Oct 10:30 AM', status: 'completed' },
                    { title: 'First Payment Recorded', date: '26 Oct 14:00 PM', status: 'completed', amount: 250000 }
                ]
            },
            {
                id: "ORD-1003",
                orderId: "ORD-1003",
                productName: "Eicher Pro 2049",
                dealerName: "Global Heavy Eq.",
                invoiceNo: "INV-2023-0162",
                totalAmount: 1350000,
                paidAmount: 0,
                outstandingAmount: 1350000,
                status: "LOAN APPROVED",
                paymentStatus: "Pending",
                delivery: "Not Started",
                lifecycleStep: 6,
                deliveryStage: "Blocked",
                documents: [
                    { name: 'Invoice Generated', status: 'Completed', responsible: 'Dealer', date: '22 Oct 2023' }
                ],
                timeline: [
                    { title: 'Order Created', date: '22 Oct 10:30 AM', status: 'completed' },
                    { title: 'Loan Approved', date: '23 Oct 09:00 AM', status: 'completed' }
                ]
            }
        ];

        const savedOrders = JSON.parse(localStorage.getItem(this.STORAGE_KEYS.ORDERS)) || [];
        
        // Merge without duplicates
        const allOrders = [...staticOrders];
        savedOrders.forEach(so => {
            if (!allOrders.find(o => o.id === so.id)) {
                allOrders.push(so);
            }
        });

        return allOrders;
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

        // Seed with a mock quotation of a dealer having multiple vehicles
        const seededQuotes = [
            {
                id: 'QT-849201',
                category: 'Pre-Owned',
                type: 'B2B Purchase',
                brand: 'Multiple Brands',
                productName: 'Multiple Vehicles',
                price: 2450650,
                offerPrice: 2400000,
                quantity: 2,
                sellerName: 'Deshpande Commercials, Pune',
                buyerCompany: 'TechLogistics Corp',
                status: 'Pending Negotiation',
                receivedDate: new Date().toLocaleDateString('en-GB'),
                vehicles: [
                    {
                        id: 'v1',
                        name: 'Tata Ace Gold',
                        brand: 'Tata',
                        price: 480000,
                        year: 2023,
                        km: 5000,
                        image: 'https://images.unsplash.com/photo-1594042878693-514add1d4411?auto=format&fit=crop&q=80&w=400'
                    },
                    {
                        id: 'v5',
                        name: 'Ashok Leyland Dost+',
                        brand: 'Ashok Leyland',
                        price: 750000,
                        year: 2022,
                        km: 15000,
                        image: 'https://images.unsplash.com/photo-1626668893632-6f3c4466d22f?auto=format&fit=crop&q=80&w=400'
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

    // --- Test Drives Management ---
    getTestDrives() {
        return JSON.parse(localStorage.getItem(this.STORAGE_KEYS.TEST_DRIVES)) || [];
    }

    saveTestDrives(testDrives) {
        localStorage.setItem(this.STORAGE_KEYS.TEST_DRIVES, JSON.stringify(testDrives));
    }

    addTestDrive(testDrive) {
        const drives = this.getTestDrives();
        drives.unshift(testDrive); // Add to top
        this.saveTestDrives(drives);
    }

    updateTestDriveStatus(id, newStatus) {
        const drives = this.getTestDrives();
        const driveIndex = drives.findIndex(d => d.id === id);
        if (driveIndex !== -1) {
            drives[driveIndex].status = newStatus;
            this.saveTestDrives(drives);
        }
    }
}

// Export a singleton instance
const store = new Store();

// Role-based UI Adjustments
document.addEventListener('DOMContentLoaded', () => {
    const user = store.getUser();
    if (user && user.role === 'Buyer') {
        const sellButtons = document.querySelectorAll('a[href*="sell.html"], a[href*="#sellSection"], a[href*="sell-wizard.html"], button[onclick*="sellSection"]');
        sellButtons.forEach(btn => {
            btn.style.setProperty('display', 'none', 'important');
        });
    }
});
