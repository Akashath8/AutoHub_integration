// js/application.js

let currentStep = 1;

document.addEventListener("DOMContentLoaded", function () {
    initializeFromPlatformA();
    renderPANSection();
    setupOccupationToggle();
    updateProgress();
});

function renderPANSection() {
    const app = loadApplication();
    const panSection = document.getElementById("panSection");

    if (app.panVerified) {
        panSection.innerHTML = `
            <div class="alert alert-success">
                PAN Already Verified from Platform A
            </div>
        `;
    } else {
        panSection.innerHTML = `
            <input class="form-control mb-2" placeholder="Enter PAN Number">
            <button class="btn btn-primary">Verify PAN</button>
        `;
    }
}

function nextStep() {
    if (currentStep < 6) {
        document.querySelector(`[data-step="${currentStep}"]`).classList.add("d-none");
        currentStep++;
        document.querySelector(`[data-step="${currentStep}"]`).classList.remove("d-none");
        updateProgress();
    } else {
        alert("Next Module (Documents) Coming Next");
    }
}

function prevStep() {
    if (currentStep > 1) {
        document.querySelector(`[data-step="${currentStep}"]`).classList.add("d-none");
        currentStep--;
        document.querySelector(`[data-step="${currentStep}"]`).classList.remove("d-none");
        updateProgress();
    }
}

function updateProgress() {
    const percent = (currentStep / 6) * 100;
    document.getElementById("progressBar").style.width = percent + "%";
}

function verifyAadhaar() {
    document.getElementById("aadhaarVerified").classList.remove("d-none");
}

function setupOccupationToggle() {
    const radios = document.querySelectorAll('input[name="occupation"]');
    radios.forEach(r => {
        r.addEventListener("change", function () {
            if (this.value === "self") {
                document.getElementById("gstSection").classList.remove("d-none");
            } else {
                document.getElementById("gstSection").classList.add("d-none");
            }
        });
    });

    document.getElementById("gstYesNo")?.addEventListener("change", function () {
        if (this.value === "yes") {
            document.getElementById("gstNumber").classList.remove("d-none");
        } else {
            document.getElementById("gstNumber").classList.add("d-none");
        }
    });
}
