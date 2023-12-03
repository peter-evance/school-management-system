// src/components/PasswordReset.js
import React, { useState } from 'react';
import './PasswordReset.css';


const PasswordReset = () => {
  const [email, setEmail] = useState('');

  const handlePasswordResetSubmit = () => {
    // Implement logic to handle the password reset form submission
    console.log('Password reset form submitted');
  };

  return (
    <div>
      <label>
        <p>Enter your email to reset your password:</p>
        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
      </label>
      <button onClick={handlePasswordResetSubmit}>Submit</button>
    </div>
  );
};

export default PasswordReset;
