// Search functionality
document.getElementById('searchInput').addEventListener('keyup', function () {
    const filter = this.value.toLowerCase();
    const rows = document.querySelectorAll('#usersTable tbody tr');
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? '' : 'none';
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

function attachRoleToggleListeners() {
    document.querySelectorAll('.role-btn').forEach(button => {
        button.addEventListener('click', async function () {
            const row = this.closest('tr');
            const userEmail = row.querySelector('td:nth-child(3)').textContent.trim();
            const currentRole = this.textContent.trim().toLowerCase();
            const newRole = currentRole === 'admin' ? 'user' : 'admin'; 

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

                this.textContent = newRole.charAt(0).toUpperCase() + newRole.slice(1);
                this.classList.toggle('btn-primary');
                this.classList.toggle('btn-secondary');
                alert('User role updated successfully');
            } catch (error) {
                alert(error.message);
            }
        }
        });
    });
}

attachRoleToggleListeners();