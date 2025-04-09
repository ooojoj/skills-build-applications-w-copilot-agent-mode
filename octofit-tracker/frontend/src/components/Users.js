import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/users/')
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  const handleEdit = (userId) => {
    // Logic for editing user details
    console.log(`Edit user with ID: ${userId}`);
    // You can implement a modal or redirect to an edit page here
  };

  const handleDelete = (userId) => {
    // Logic for deleting a user
    fetch(`https://super-halibut-4jvjxq4xq75c7pj9-8000.app.github.dev/api/users/${userId}/`, {
      method: 'DELETE',
    })
      .then(response => {
        if (response.ok) {
          setUsers(users.filter(user => user.id !== userId));
        } else {
          console.error('Failed to delete user');
        }
      })
      .catch(error => console.error('Error deleting user:', error));
  };

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
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.name}</td>
              <td>{user.email}</td>
              <td>
                <button className="btn btn-primary btn-sm" onClick={() => handleEdit(user.id)}>Edit</button>
                <button className="btn btn-danger btn-sm ms-2" onClick={() => handleDelete(user.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Users;
