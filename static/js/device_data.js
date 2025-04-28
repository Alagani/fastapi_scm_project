// Filter table based on dropdown selection and search input
const deviceSelect = document.getElementById('deviceSelect');
const searchInput = document.getElementById('searchInput');
const tableRows = document.querySelectorAll('#deviceDataTable tbody tr');

function filterTable() {
    const selectedDevice = deviceSelect.value.toLowerCase();
    const searchTerm = searchInput.value.toLowerCase();

    tableRows.forEach(row => {
        const deviceId = row.cells[0].textContent.toLowerCase();
        const rowText = row.textContent.toLowerCase();

        // Show row if it matches both the selected device and the search term
        const matchesDevice = !selectedDevice || deviceId.includes(selectedDevice);
        const matchesSearch = !searchTerm || rowText.includes(searchTerm);

        row.style.display = matchesDevice && matchesSearch ? '' : 'none';
    });
}

// Add event listeners
deviceSelect.addEventListener('change', filterTable);
searchInput.addEventListener('keyup', filterTable);