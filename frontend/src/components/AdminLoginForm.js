// src/components/AdminLoginForm.js
import React, { useState } from 'react';

const AdminLoginForm = () => {
  const [adminUsername, setAdminUsername] = useState('');
  const [adminPassword, setAdminPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleAdminLogin = () => {
    // Implement admin login logic here
    // Check if the adminUsername and adminPassword match your criteria
    // For simplicity, let's assume a predefined admin username and password
    const predefinedAdminUsername = 'admin';
    const predefinedAdminPassword = 'admin123';

    if (adminUsername === predefinedAdminUsername && adminPassword === predefinedAdminPassword) {
      setIsLoggedIn(true);
    } else {
      console.log('Invalid admin credentials. Please try again.');
    }
  };

  const handleAdminLogout = () => {
    // Implement admin logout logic here
    setIsLoggedIn(false);
    setAdminUsername('');
    setAdminPassword('');
  };

  return (
    <div className="admin-login-form">
      {isLoggedIn ? (
        <div>
          <p>Welcome, Admin {adminUsername}!</p>
          <button onClick={handleAdminLogout}>Logout</button>
        </div>
      ) : (
        <div>
          <label>
            <input
              type="text"
              value={adminUsername}
              onChange={(e) => setAdminUsername(e.target.value)}
              placeholder="Admin Username"
            />
          </label>
          <label>
            <input
              type="password"
              value={adminPassword}
              onChange={(e) => setAdminPassword(e.target.value)}
              placeholder="Admin Password"
            />
          </label>
          <button onClick={handleAdminLogin}>Admin Sign in</button>
        </div>
      )}
    </div>
  );
};

export default AdminLoginForm;

