// Wait for the DOM to be fully loaded before executing the script
document.addEventListener("DOMContentLoaded", function () {
    // Get references to key DOM elements
    const sidebar = document.querySelector('.sidebar');
    const shipmentTable = document.getElementById("shipmentTable");
    const pagination = document.getElementById("pagination");
    const searchInput = document.getElementById("searchInput");

    // Initialize pagination variables
    let currentPage = 1;
    let rowsPerPage = calculateRowsPerPage();

    // Calculate how many rows to display per page based on sidebar state
    function calculateRowsPerPage() {
        const isSidebarHidden = sidebar.classList.contains("open") || getComputedStyle(sidebar).marginLeft === "-250px";
        return isSidebarHidden ? 15 : 10; // Show more rows when sidebar is hidden
    }

    // Filter table rows based on search input
    function getFilteredRows() {
        const filter = searchInput.value.toLowerCase();
        return Array.from(shipmentTable.querySelectorAll("tr")).filter(row => {
            return row.textContent.toLowerCase().includes(filter);
        });
    }

    // Display rows for the current page
    function displayRows(page) {
        const allRows = shipmentTable.querySelectorAll("tr");
        const filteredRows = getFilteredRows();

        // Hide all rows initially
        allRows.forEach(row => row.style.display = "none");

        // Calculate start and end indices for current page
        const start = (page - 1) * rowsPerPage;
        const end = start + rowsPerPage;

        // Show only the rows for the current page
        filteredRows.forEach((row, index) => {
            if (index >= start && index < end) {
                row.style.display = "";
            }
        });

        // Scroll to top of table on new search or page click
        document.querySelector(".table-responsive").scrollTop = 0;
    }

    // Set up pagination buttons
    function setupPagination() {
        const filteredRows = getFilteredRows();
        const totalPages = Math.ceil(filteredRows.length / rowsPerPage);

        pagination.innerHTML = ""; // Clear existing buttons

        if (totalPages <= 1) return; // Don't show pagination if only one page

        // Create a button for each page
        for (let i = 1; i <= totalPages; i++) {
            const btn = document.createElement("button");
            btn.className = "btn btn-sm btn-light mx-1 pagination-button";
            btn.textContent = i;
            btn.addEventListener("click", function () {
                currentPage = i;
                displayRows(currentPage);
                updateActiveButton();
            });
            pagination.appendChild(btn);
        }

        updateActiveButton();
    }

    // Update the active state of pagination buttons
    function updateActiveButton() {
        const buttons = pagination.querySelectorAll(".pagination-button");
        buttons.forEach((btn, index) => {
            // Highlight the current page button
            btn.classList.toggle("btn-light", index + 1 === currentPage);
            btn.classList.toggle("btn-outline-light", index + 1 !== currentPage);
        });
    }

    // Initialize or reset pagination
    function initPagination() {
        rowsPerPage = calculateRowsPerPage();
        currentPage = 1;
        displayRows(currentPage);
        setupPagination();
    }

    // 🔄 Event: Search input changes
    searchInput.addEventListener("input", () => {
        initPagination(); // Reset pagination when search term changes
    });

    // 🔄 Event: Sidebar toggle
    const sidebarToggle = document.querySelector('.sidebar-toggler');
    if (sidebarToggle) {
        sidebarToggle.addEventListener("click", () => {
            // Wait for sidebar animation to complete before recalculating
            setTimeout(() => {
                initPagination();
            }, 300);
        });
    }

    // 🔄 Event: Window Resize
    window.addEventListener("resize", () => {
        initPagination(); // Recalculate on window resize
    });

    // Initial Run - set up pagination when page loads
    initPagination();
});