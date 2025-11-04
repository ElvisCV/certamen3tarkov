// JavaScript para funcionalidades de la seccion de armas

document.addEventListener('DOMContentLoaded', function() {
    
    // Lazy loading para imagenes de armas
    const weaponImages = document.querySelectorAll('.weapon-img');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        weaponImages.forEach(img => imageObserver.observe(img));
    }
    
    // Animacion al hacer hover en las cards
    const weaponCards = document.querySelectorAll('.weapon-card');
    
    weaponCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Scroll suave al cambiar de pagina
    const paginationLinks = document.querySelectorAll('.pagination .page-link');
    
    paginationLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Scroll hacia arriba antes de cambiar de pagina
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    });
    
    // Contador de armas visible
    const totalWeapons = document.querySelector('.text-muted');
    if (totalWeapons) {
        const count = totalWeapons.textContent.match(/\d+/);
        if (count) {
            console.log(`Total de armas en el arsenal: ${count[0]}`);
        }
    }
    
    // Funcion para filtrar armas (si se implementa busqueda en el futuro)
    function filterWeapons(searchTerm) {
        const cards = document.querySelectorAll('.weapon-card');
        searchTerm = searchTerm.toLowerCase();
        
        cards.forEach(card => {
            const title = card.querySelector('.card-title').textContent.toLowerCase();
            const description = card.querySelector('.card-text').textContent.toLowerCase();
            
            if (title.includes(searchTerm) || description.includes(searchTerm)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    }
    
    // Mensaje de bienvenida en consola
    console.log('%c🔫 ARSENAL DE ARMAS 🔫', 'color: #ffc107; font-size: 18px; font-weight: bold;');
    console.log('%cExplora el arsenal completo de Escape from Tarkov', 'color: #666; font-size: 12px;');
});

// Funcion para mostrar detalles del arma (placeholder para futura implementacion)
function showWeaponDetails(weaponId) {
    console.log(`Mostrando detalles del arma ID: ${weaponId}`);
    // Aqui se podria implementar un modal con informacion detallada
}