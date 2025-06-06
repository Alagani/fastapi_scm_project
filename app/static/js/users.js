// Search functionality
document.getElementById('searchInput').addEventListener('keyup', function () {
    const filter = this.value.toLowerCase();
    const rows = document.querySelectorAll('#usersTable tbody tr');
    
    rows.forEach(row => {
        // Get text from specific columns only (Username, Email, Role)
        const username = row.cells[1].textContent.toLowerCase();
        const email = row.cells[2].textContent.toLowerCase();
        const role = row.cells[3].textContent.toLowerCase();
        
        // Check if any of these columns contain the filter text
        const matches = username.includes(filter) || 
                         email.includes(filter) || 
                         role.includes(filter);
        
        row.style.display = matches ? '' : 'none';
    });
});

// Delete functionality
document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', async function () {
        const row = this.closest('tr');
        const userEmail = row.querySelector('td:nth-child(3)').textContent.trim();

        if (confirm('Are you sure you want to delete this user?')) {
            try {
                const response = await fetch(`/users/${userEmail}`, {
                    method: 'DELETE'
                });

                if (!response.ok) {
                    throw new Error('Failed to delete user');
                }

                alert('User deleted successfully');
                row.remove();
            } catch (error) {
                alert(error.message);
            }
        }
    });
});

// Update functionality
function attachRoleToggleListeners() {
    document.querySelectorAll('.role-btn').forEach(button => {
        button.addEventListener('click', async function () {
            const row = this.closest('tr');
            const userEmail = row.querySelector('td:nth-child(3)').textContent.trim();
            const isAdmin = this.classList.contains('btn-warning'); // Check if current button is "Make User" (admin)
            const newRole = isAdmin ? 'user' : 'admin';

            if (confirm('Are you sure you want to update role?')) {
                try {
                    const response = await fetch(`/users/${userEmail}`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ role: newRole })
                    });

                    if (!response.ok) {
                        throw new Error('Failed to update user role');
                    }

                    // Update button text and styling
                    if (newRole === 'admin') {
                        this.textContent = 'Make User';
                        this.classList.remove('btn-success');
                        this.classList.add('btn-warning');
                    } else {
                        this.textContent = 'Make Admin';
                        this.classList.remove('btn-warning');
                        this.classList.add('btn-success');
                    }
                    
                    alert('User role updated successfully');
                } catch (error) {
                    alert(error.message);
                }
            }
        });
    });
}

attachRoleToggleListeners();