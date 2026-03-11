/**
 * AutoHub - Authentication Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    // --- Login Logic ---
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;

            if (email && password) {
                let userRole = '';
                let mockUser = null;
                let redirectUrl = 'index.html';

                // Static Credentials Check
                if (email === 'test@dealer.com' && password === 'pass@123') {
                    userRole = 'Dealer';
                    mockUser = {
                        firstName: 'Test Dealer',
                        companyName: 'Test Dealer Motors',
                        email: email,
                        role: 'Dealer',
                        isLoggedIn: true,
                        gst: '27DEALER1234Z5',
                        dealerTrustStatus: 'Trusted Dealer', // Giving trusted status for easy UI flow
                        verificationStatus: 'Approved'
                    };
                    redirectUrl = 'dealer-dashboard.html';
                } else if (email === 'test@buyer.com' && password === 'pass@123') {
                    userRole = 'Buyer';
                    mockUser = {
                        firstName: 'Test Buyer',
                        companyName: 'Test Buyer Corp',
                        email: email,
                        role: 'Buyer',
                        isLoggedIn: true,
                        gst: '27BUYER5678Z9',
                        dealerTrustStatus: 'N/A'
                    };
                    redirectUrl = 'index.html';
                } else {
                    alert('Invalid credentials. Please use test@dealer.com or test@buyer.com with password pass@123.');
                    return;
                }

                // Save mock user for demo
                store.saveUser(mockUser);
                
                alert(`Login Successful as ${userRole}!`);
                window.location.href = redirectUrl;

            } else {
                alert('Please enter valid credentials.');
            }
        });
    }

    // --- Registration Logic ---
    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const companyName = document.getElementById('companyName').value;
            const contactPerson = document.getElementById('contactPerson').value;
            const email = document.getElementById('email').value;
            const mobile = document.getElementById('mobile').value;
            const role = document.getElementById('role').value;
            const gst = document.getElementById('gst').value.toUpperCase();
            const regNo = document.getElementById('regNo').value.toUpperCase();
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            // Validation
            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }

            const newUser = {
                firstName: companyName, // Map to existing state structure temporarily if used directly
                companyName: companyName,
                contactPerson: contactPerson,
                email,
                mobile,
                role: role,
                gst: gst,
                regNo: regNo,
                dealerTrustStatus: role === 'Dealer' ? 'Non-Trusted Dealer' : 'N/A', // Escrow requirement
                verificationStatus: role === 'Dealer' ? 'Pending' : 'Approved', // Auto-approve buyers for now
                isLoggedIn: true // Auto-login after register
            };

            store.saveUser(newUser);
            
            if (role === 'Dealer') {
                alert('Registration Successful! Your dealer account is pending verification. Redirecting to dashboard...');
                window.location.href = 'dealer-dashboard.html';
            } else {
                alert('Registration Successful! Redirecting...');
                window.location.href = 'index.html';
            }
        });
    }
});
