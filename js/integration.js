// js/integration.js

function getQueryParams() {
    const params = {};
    window.location.search.replace(/[?&]+([^=&]+)=([^&]*)/gi,
        function (str, key, value) {
            params[key] = decodeURIComponent(value);
        });
    return params;
}

function initializeFromPlatformA() {
    const params = getQueryParams();
    let app = loadApplication();

    if (params.productId) {
        app.productId = params.productId;
    }

    if (params.panVerified === "true") {
        app.panVerified = true;
    }

    if (params.loanAmount) {
        app.loanDetails.amount = parseInt(params.loanAmount);
    }

    saveApplication(app);
}
