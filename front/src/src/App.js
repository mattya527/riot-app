import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import UserNameForm from './pages/UsernameForm';
import MatchHistoryList from './pages/MatchHistoryList';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<UserNameForm />} />
        <Route path="/match-history-list" element={<MatchHistoryList />} />
      </Routes>
    </Router>
  );
}

export default App;
