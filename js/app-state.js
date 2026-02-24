// js/app-state.js

const APP_STORAGE_KEY = "LOS_APPLICATION";

function getDefaultApplication() {
    return {
        productId: null,
        panVerified: false,
        applicant: {},
        coApplicants: [],
        documents: {
            kyc: [],
            address: [],
            financial: [],
            employment: [],
            bank: []
        },
        loanDetails: {},
        selectedOffer: null,
        status: "DRAFT",
        applicationId: null
    };
}

function loadApplication() {
    const data = localStorage.getItem(APP_STORAGE_KEY);
    return data ? JSON.parse(data) : getDefaultApplication();
}

function saveApplication(app) {
    localStorage.setItem(APP_STORAGE_KEY, JSON.stringify(app));
}

function resetApplication() {
    localStorage.removeItem(APP_STORAGE_KEY);
}
