import React from 'react';

function Users() {
  return (
    <div className="container mt-4">
      <h1 className="display-4 text-center">Users</h1>
      <table className="table table-striped">
        <thead className="thead-dark">
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>John Doe</td>
            <td>john.doe@example.com</td>
            <td>
              <button className="btn btn-primary btn-sm">Edit</button>
              <button className="btn btn-danger btn-sm ms-2">Delete</button>
            </td>
          </tr>
          <tr>
            <td>Jane Smith</td>
            <td>jane.smith@example.com</td>
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

export default Users;
