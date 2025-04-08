import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Welcome to Octofit Tracker</h1>
      </header>
      <nav>
        <a href="/activities">Activities</a>
        <a href="/leaderboard">Leaderboard</a>
        <a href="/teams">Teams</a>
        <a href="/users">Users</a>
        <a href="/workouts">Workouts</a>
      </nav>
    </div>
  );
}

export default App;
