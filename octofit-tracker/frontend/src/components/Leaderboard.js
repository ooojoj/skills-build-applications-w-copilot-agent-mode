import React from 'react';

function Leaderboard() {
  return (
    <div className="container mt-4">
      <h1 className="display-4 text-center">Leaderboard</h1>
      <table className="table table-striped">
        <thead className="thead-dark">
          <tr>
            <th scope="col">Rank</th>
            <th scope="col">User</th>
            <th scope="col">Score</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>John Doe</td>
            <td>1500</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Jane Smith</td>
            <td>1400</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;
