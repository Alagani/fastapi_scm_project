/**
 * MAIN FILTER EVENT HANDLER
 * Handles device filtering when "Get Data" button is clicked.
 * Filters table rows based on selected device ID and refreshes pagination.
 */
document.getElementById("getDataBtn").addEventListener("click", function() {
    const selectedDeviceId = document.getElementById("deviceSelect").value;
    const allRows = Array.from(document.querySelectorAll("#deviceDataTable tbody tr"));
    let visibleRows = [];

    allRows.forEach(row => {
        const cellValue = row.cells[0].textContent.trim();
        if (!selectedDeviceId || cellValue === selectedDeviceId) {
            visibleRows.push(row);
        }
        row.style.display = "none";
    });

    updatePagination(visibleRows);
    displayPage(1, visibleRows);
});

// Global variable to store currently visible rows for pagination navigation
let currentVisibleRows = [];

/**
 * PAGINATION DISPLAY FUNCTION
 * Displays a specific page of rows (14 rows per page).
 * Hides all rows, then shows only those belonging to the requested page.
 * Updates pagination button styling to highlight the current page.
 */
function displayPage(page, visibleRows) {
    currentVisibleRows = visibleRows;
    const rowsPerPage = 14;
    const start = (page - 1) * rowsPerPage;
    const end = start + rowsPerPage;

    currentVisibleRows.forEach(row => row.style.display = "none");
    
    currentVisibleRows.slice(start, end).forEach(row => {
        row.style.display = "";
    });

    setActiveButton(page);
}

/**
 * PAGINATION BUTTON GENERATOR
 * Creates numbered pagination buttons based on total visible rows.
 * Calculates required pages (14 rows per page) and generates clickable buttons.
 * Each button triggers displayPage() when clicked.
 */
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

/**
 * PAGINATION UPDATE WRAPPER
 * Simple wrapper function that calls createPaginationButtons().
 * Used to refresh pagination controls when data changes.
 */
function updatePagination(visibleRows) {
    createPaginationButtons(visibleRows);
}

/**
 * PAGINATION BUTTON STYLING
 * Updates visual styling of pagination buttons to highlight the active page.
 * Active button gets solid styling, inactive buttons get outline styling.
 */
function setActiveButton(activePage) {
    const buttons = document.querySelectorAll("#pagination button");
    buttons.forEach(btn => {
        const isActive = parseInt(btn.textContent) === activePage;
        btn.classList.toggle("btn-light", isActive);
        btn.classList.toggle("btn-outline-light", !isActive);
    });
}

/**
 * INITIALIZATION
 * Sets up the table when the page loads.
 * Creates initial pagination for all rows and displays the first page.
 */
document.addEventListener("DOMContentLoaded", function() {
    const rows = Array.from(document.querySelectorAll("#deviceDataTable tbody tr"));
    updatePagination(rows);
    displayPage(1, rows);
});