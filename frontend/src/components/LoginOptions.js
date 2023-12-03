// src/components/LoginOptions.js
import React from 'react';
import { Link } from 'react-router-dom';
import './LoginOptions.css';

const LoginOptions = () => {
  return (
    <div className="login-options">
      <Link to="/student" className="login-button">
        Student
      </Link>
      <Link to="/admin" className="login-button">
        Admin
      </Link>
      <button className="login-button" onClick={() => console.log('Teacher login clicked')}>Teacher</button>
      {/* Add more buttons for additional roles as needed */}
    </div>
  );
};

export default LoginOptions;
