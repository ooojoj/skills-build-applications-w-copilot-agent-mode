import React from 'react';

function Workouts() {
  return (
    <div className="container mt-4">
      <h1 className="display-4 text-center">Workouts</h1>
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">Morning Yoga</h5>
          <p className="card-text">Duration: 30 minutes</p>
          <button className="btn btn-primary">Start</button>
        </div>
      </div>
      <div className="card mt-3">
        <div className="card-body">
          <h5 className="card-title">Evening Run</h5>
          <p className="card-text">Duration: 45 minutes</p>
          <button className="btn btn-primary">Start</button>
        </div>
      </div>
    </div>
  );
}

export default Workouts;
