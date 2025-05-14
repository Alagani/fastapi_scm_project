document.getElementById("getDataBtn").addEventListener("click", function() {
    const selectedDeviceId = document.getElementById("deviceSelect").value;
    const allRows = Array.from(document.querySelectorAll("#deviceDataTable tbody tr"));
    let visibleRows = [];

    // Filter rows based on selection
    allRows.forEach(row => {
        const cellValue = row.cells[0].textContent.trim();
        if (!selectedDeviceId || cellValue === selectedDeviceId) {
            visibleRows.push(row);
        }
        row.style.display = "none"; // Hide all initially
    });

    // Update pagination and show first page
    updatePagination(visibleRows);
    displayPage(1, visibleRows);
});

// Pagination functions
let currentVisibleRows = [];

function displayPage(page, visibleRows) {
    currentVisibleRows = visibleRows;
    const rowsPerPage = 14;
    const start = (page - 1) * rowsPerPage;
    const end = start + rowsPerPage;

    // Hide all rows first
    currentVisibleRows.forEach(row => row.style.display = "none");
    
    // Show only current page rows
    currentVisibleRows.slice(start, end).forEach(row => {
        row.style.display = "";
    });

    setActiveButton(page);
}

function createPaginationButtons(visibleRows) {
    const paginationContainer = document.getElementById("pagination");
    paginationContainer.innerHTML = "";
    const pageCount = Math.ceil(visibleRows.length / 14);

    for (let i = 1; i <= pageCount; i++) {
        const btn = document.createElement("button");
        btn.className = "btn btn-sm btn-light mx-1";
        btn.textContent = i;
        btn.addEventListener("click", () => displayPage(i, currentVisibleRows));
        paginationContainer.appendChild(btn);
    }
}

function updatePagination(visibleRows) {
    createPaginationButtons(visibleRows);
}

function setActiveButton(activePage) {
    const buttons = document.querySelectorAll("#pagination button");
    buttons.forEach(btn => {
        const isActive = parseInt(btn.textContent) === activePage;
        btn.classList.toggle("btn-light", isActive);
        btn.classList.toggle("btn-outline-light", !isActive);
    });
}

// Initialize
document.addEventListener("DOMContentLoaded", function() {
    const rows = Array.from(document.querySelectorAll("#deviceDataTable tbody tr"));
    updatePagination(rows);
    displayPage(1, rows);
});