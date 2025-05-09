
    document.addEventListener("DOMContentLoaded", function () {
        const sidebar = document.querySelector('.sidebar');
        const shipmentTable = document.getElementById("shipmentTable");
        const pagination = document.getElementById("pagination");
        const searchInput = document.getElementById("searchInput");

        let currentPage = 1;
        let rowsPerPage = calculateRowsPerPage();

        function calculateRowsPerPage() {
            const isSidebarHidden = sidebar.classList.contains("open") || getComputedStyle(sidebar).marginLeft === "-250px";
            return isSidebarHidden ? 15 : 10;
        }

        function getFilteredRows() {
            const filter = searchInput.value.toLowerCase();
            return Array.from(shipmentTable.querySelectorAll("tr")).filter(row => {
                return row.textContent.toLowerCase().includes(filter);
            });
        }

        function displayRows(page) {
            const allRows = shipmentTable.querySelectorAll("tr");
            const filteredRows = getFilteredRows();

            allRows.forEach(row => row.style.display = "none");

            const start = (page - 1) * rowsPerPage;
            const end = start + rowsPerPage;

            filteredRows.forEach((row, index) => {
                if (index >= start && index < end) {
                    row.style.display = "";
                }
            });

            // Scroll to top of table on new search or page click
            document.querySelector(".table-responsive").scrollTop = 0;
        }

        function setupPagination() {
            const filteredRows = getFilteredRows();
            const totalPages = Math.ceil(filteredRows.length / rowsPerPage);

            pagination.innerHTML = "";

            if (totalPages <= 1) return; // Don’t show pagination if not needed

            for (let i = 1; i <= totalPages; i++) {
                const btn = document.createElement("button");
                btn.className = "btn btn-sm btn-primary mx-1 pagination-button";
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

        function updateActiveButton() {
            const buttons = pagination.querySelectorAll(".pagination-button");
            buttons.forEach((btn, index) => {
                btn.classList.toggle("btn-secondary", index + 1 === currentPage);
                btn.classList.toggle("btn-primary", index + 1 !== currentPage);
            });
        }

        function initPagination() {
            rowsPerPage = calculateRowsPerPage();
            currentPage = 1;
            displayRows(currentPage);
            setupPagination();
        }

        // 🔄 Event: Search
        searchInput.addEventListener("input", () => {
            initPagination();
        });

        // 🔄 Event: Sidebar toggle
        const sidebarToggle = document.querySelector('.sidebar-toggler');
        if (sidebarToggle) {
            sidebarToggle.addEventListener("click", () => {
                setTimeout(() => {
                    initPagination();
                }, 300);
            });
        }

        // 🔄 Event: Window Resize
        window.addEventListener("resize", () => {
            initPagination();
        });

        // Initial Run
        initPagination();
    });



