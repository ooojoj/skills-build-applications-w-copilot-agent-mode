import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="display-4 text-center">Workouts</h1>
      {workouts.map(workout => (
        <div className="card mt-3" key={workout.id}>
          <div className="card-body">
            <h5 className="card-title">{workout.name}</h5>
            <p className="card-text">{workout.description}</p>
            <button className="btn btn-primary">Start</button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Workouts;
