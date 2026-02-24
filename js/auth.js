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
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Simple mock validation
            if (email && password) {
                // In a real app, we'd verify against a database. 
                // For this demo, we simulate a successful login if fields are filled.
                // We'll try to find a stored user, or create a mock one if "demo@autohub.com"

                let user = store.getUser();
                if (!user) {
                    // Create a mock session for demo if no user exists yet
                    user = {
                        firstName: 'Demo',
                        lastName: 'User',
                        email: email,
                        isLoggedIn: true,
                        pan: 'ABCDE1234F',
                        panVerified: true
                    };
                    store.saveUser(user);
                } else {
                    user.isLoggedIn = true;
                    store.saveUser(user);
                }

                alert('Login Successful!');
                window.location.href = 'index.html';
            } else {
                alert('Please enter valid credentials.');
            }
        });
    }

    // --- Registration Logic ---
    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const firstName = document.getElementById('firstName').value;
            const lastName = document.getElementById('lastName').value;
            const email = document.getElementById('email').value;
            const mobile = document.getElementById('mobile').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            const pan = document.getElementById('pan').value.toUpperCase();

            // Validation
            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }

            // PAN Logic: If PAN entered -> Verified = true
            const panVerified = pan.length === 10;

            const newUser = {
                firstName,
                lastName,
                email,
                mobile,
                pan: panVerified ? pan : null,
                panVerified: panVerified,
                isLoggedIn: true // Auto-login after register
            };

            store.saveUser(newUser);
            alert('Registration Successful! Redirecting...');
            window.location.href = 'index.html';
        });
    }
});
