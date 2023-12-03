import React, { useState } from 'react';
import './LoginForm.css';
import { Link } from 'react-router-dom';

const LoginForm = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    const predefinedStudentUsername = 'stud1';
    const predefinedStudentPassword = '1234';

    // Set the username and password directly
    setUsername(predefinedStudentUsername);
    setPassword(predefinedStudentPassword);

    setIsLoggedIn(true);
    // You can add a success message or redirect the user here
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    setUsername('');
    setPassword('');
  };

  
  return (
    <div className="login-form">
      {isLoggedIn ? (
        <div>
          <p>Welcome, {username}!</p>
          <button onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <div>
          <label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
          </label>
          <label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
          </label>
          <button onClick={handleLogin}>Sign in</button>
          <br/><br/>
          <Link to="/password-reset">Forgot Password?</Link>
        </div>
      )}
    </div>
  );
};

export default LoginForm;

