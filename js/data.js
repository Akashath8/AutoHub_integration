/**
 * AutoHub - Mock Data Source
 */

const VEHICLES = [
    {
        id: 'v1',
        name: 'Hyundai i10 Neo',
        brand: 'Hyundai',
        price: 850650,
        type: 'Hatchback',
        year: 2022,
        km: 42000,
        fuel: 'Petrol',
        transmission: 'Manual',
        owner: '2nd Owner',
        location: 'Pune',
        sellerName: 'Deshpande Auto, Pune',
        image: 'https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&q=80&w=400',
        description: 'Compact and efficient city car with modern features.',
        variant: '1.2 KAPPA SPORTZ',
        rto: 'MH-12',
        emi: '16,230',
        hubLocation: 'AutoHub Wakad, Pune',
        conditionTag: 'High quality',
        specs: {
            engine: '1.2L Kappa',
            power: '82 bhp',
            torque: '114 Nm',
            mileage: '20.7 kmpl'
        }
    },
    {
        id: 'v2',
        name: 'Toyota Fortuner',
        brand: 'Toyota',
        price: 3450000,
        type: 'SUV',
        year: 2021,
        km: 25000,
        fuel: 'Diesel',
        transmission: 'Automatic',
        owner: '1st Owner',
        location: 'Mumbai',
        sellerName: 'Magic Automobiles, Mumbai',
        image: 'https://images.unsplash.com/photo-1626668893632-6f3c4466d22f?auto=format&fit=crop&q=80&w=400',
        description: 'Robust SUV with premium interiors and powerful performance.',
        variant: '2.8 4X4 AT',
        rto: 'MH-01',
        emi: '65,855',
        hubLocation: 'AutoHub Andheri, Mumbai',
        conditionTag: 'Assurred',
        specs: {
            engine: '2.8L Diesel',
            power: '201 bhp',
            torque: '500 Nm',
            mileage: '10 kmpl'
        }
    },
    {
        id: 'v3',
        name: 'Toyota Crysta',
        brand: 'Toyota',
        price: 2950000,
        type: 'MPV',
        year: 2020,
        km: 35000,
        fuel: 'Diesel',
        transmission: 'Manual',
        owner: '1st Owner',
        location: 'Bangalore',
        sellerName: 'Capital Motors, Bangalore',
        image: 'https://images.unsplash.com/photo-1623569567926-47b746654e5a?auto=format&fit=crop&q=80&w=400',
        description: 'Comfortable family MPV known for reliability.',
        variant: '2.4 ZX 7 STR',
        rto: 'KA-03',
        emi: '56,311',
        hubLocation: 'AutoHub Indiranagar, Bangalore',
        conditionTag: 'Premium variant',
        specs: {
            engine: '2.4L Diesel',
            power: '148 bhp',
            torque: '343 Nm',
            mileage: '12 kmpl'
        }
    },
    {
        id: 'v4',
        name: 'Honda City',
        brand: 'Honda',
        price: 1250000,
        type: 'Sedan',
        year: 2023,
        km: 10000,
        fuel: 'Petrol',
        transmission: 'Automatic',
        owner: '1st Owner',
        location: 'Delhi',
        sellerName: 'Northwest Dealers, Delhi',
        image: 'https://images.unsplash.com/photo-1609529669235-c07e4e1bd6e9?auto=format&fit=crop&q=80&w=400',
        description: 'Premium sedan with advanced safety features.',
        variant: 'ZX CVT',
        rto: 'DL-01',
        emi: '23,861',
        hubLocation: 'AutoHub Vasant Kunj, Delhi',
        conditionTag: 'Low kms driven',
        specs: {
            engine: '1.5L i-VTEC',
            power: '119 bhp',
            torque: '145 Nm',
            mileage: '18 kmpl'
        }
    },
    {
        id: 'v5',
        name: 'Mahindra Thar',
        brand: 'Mahindra',
        price: 1600000,
        type: 'SUV',
        year: 2022,
        km: 15000,
        fuel: 'Diesel',
        transmission: 'Manual',
        owner: '1st Owner',
        location: 'Pune',
        sellerName: 'Deshpande Auto, Pune', // Same seller as v1 to demo multi-vehicle single seller
        image: 'https://images.unsplash.com/photo-1606161290610-c529a674d89a?auto=format&fit=crop&q=80&w=400',
        description: 'Off-road beast with iconic design.',
        variant: 'LX 4-STR HARD TOP',
        rto: 'MH-14',
        emi: '30,542',
        hubLocation: 'AutoHub Hinjewadi, Pune',
        conditionTag: 'Trending',
        specs: {
            engine: '2.2L mHawk',
            power: '130 bhp',
            torque: '300 Nm',
            mileage: '15 kmpl'
        }
    }
];
