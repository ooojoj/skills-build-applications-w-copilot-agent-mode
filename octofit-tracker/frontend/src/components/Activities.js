import React from 'react';

function Activities() {
  return (
    <div className="container mt-4">
      <h1 className="display-4 text-center">Activities</h1>
      <table className="table table-striped">
        <thead className="thead-dark">
          <tr>
            <th scope="col">Activity</th>
            <th scope="col">Duration</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Running</td>
            <td>30 minutes</td>
            <td>
              <button className="btn btn-primary btn-sm">Edit</button>
              <button className="btn btn-danger btn-sm ms-2">Delete</button>
            </td>
          </tr>
          <tr>
            <td>Swimming</td>
            <td>45 minutes</td>
            <td>
              <button className="btn btn-primary btn-sm">Edit</button>
              <button className="btn btn-danger btn-sm ms-2">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
