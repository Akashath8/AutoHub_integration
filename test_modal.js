const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('my-quotes.html', 'utf8');

const dom = new JSDOM(html, {
    url: "http://localhost/",
    runScripts: "dangerously",
    resources: "usable"
});

dom.window.document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM loaded");

    // Inject mock store object to avoid localStorage errors
    dom.window.store = {
        getUser: () => ({ firstName: 'Test', lastName: 'User' }),
        getCart: () => ({ items: [] }),
        getQuotations: () => [
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
        ],
        logoutUser: () => { }
    };

    setTimeout(() => {
        try {
            console.log("Attempting to open modal...");
            dom.window.openDetailsModal(0);
            console.log("Modal function executed");
        } catch (e) {
            console.error("Caught error:", e);
        }
    }, 1000);
});
