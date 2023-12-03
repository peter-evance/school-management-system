// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import LoginOptions from './components/LoginOptions';
import AdminLoginForm from './components/AdminLoginForm';
import PasswordReset from './components/PasswordReset';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginOptions />} />
        <Route path="/student" element={<LoginForm />} />
        <Route path="/admin" element={<AdminLoginForm />} />
        <Route path="/password-reset" element={<PasswordReset/>} />
      </Routes>
    </Router>
  );
};

export default App;

