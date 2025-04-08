import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="display-4 text-center">Teams</h1>
      {teams.map(team => (
        <div className="card mt-3" key={team.id}>
          <div className="card-body">
            <h5 className="card-title">{team.name}</h5>
            <p className="card-text">Members: {team.members.join(', ')}</p>
            <button className="btn btn-primary">View Details</button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Teams;
