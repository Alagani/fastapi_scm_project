(function () {
    // Sidebar Toggler
    const sidebarToggler = document.querySelector('.sidebar-toggler');
    if (sidebarToggler) {
        sidebarToggler.addEventListener('click', () => {
            const sidebar = document.querySelector('.sidebar');
            const content = document.querySelector('.content');
            if (sidebar && content) {
                sidebar.classList.toggle('open');
                content.classList.toggle('open');
            }
        });
    }
})();
