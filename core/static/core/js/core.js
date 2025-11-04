// JavaScript para funcionalidades generales de Tarkov Wiki

document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scroll para enlaces internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Cerrar navbar al hacer click en un enlace (mobile)
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse.classList.contains('show')) {
                navbarCollapse.classList.remove('show');
            }
        });
    });
    
    // Agregar clase active al enlace actual en navbar
    const currentLocation = window.location.pathname;
    const navItems = document.querySelectorAll('.navbar-nav .nav-link');
    
    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (currentLocation === href || (href !== '/' && currentLocation.startsWith(href))) {
            item.classList.add('active');
        }
    });
    
    // Animacion de scroll para elementos
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-visible');
            }
        });
    }, observerOptions);
    
    // Observar elementos con clase fade-in
    document.querySelectorAll('.card, .feature-box, .stat-box').forEach(el => {
        observer.observe(el);
    });
    
    // Console log de bienvenida (Easter Egg)
    console.log('%c⚡ TARKOV WIKI ⚡', 'color: #ffc107; font-size: 24px; font-weight: bold;');
    console.log('%cBienvenido a Tarkov Wiki - Tu guia para sobrevivir en Tarkov', 'color: #666; font-size: 14px;');
    console.log('%cDesarrollado con Django y Bootstrap', 'color: #999; font-size: 12px;');
});

// Funcion para mostrar alertas personalizadas
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        
        // Auto-cerrar despues de 5 segundos
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }
}