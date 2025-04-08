import React from 'react';

function Teams() {
  return (
    <div className="container mt-4">
      <h1 className="display-4 text-center">Teams</h1>
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">Team Alpha</h5>
          <p className="card-text">Members: John, Jane, Alice</p>
          <button className="btn btn-primary">View Details</button>
        </div>
      </div>
      <div className="card mt-3">
        <div className="card-body">
          <h5 className="card-title">Team Beta</h5>
          <p className="card-text">Members: Bob, Charlie, Eve</p>
          <button className="btn btn-primary">View Details</button>
        </div>
      </div>
    </div>
  );
}

export default Teams;
