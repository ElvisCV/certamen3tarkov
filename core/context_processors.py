def tarkov_stats(request):
    """
    Context processor personalizado que proporciona estadísticas
    globales de Tarkov Wiki para todas las plantillas
    """
    from weapons.models import Weapon, Category, Modification
    
    stats = {
        'total_weapons': Weapon.objects.count(),
        'available_weapons': Weapon.objects.filter(is_available=True).count(),
        'total_categories': Category.objects.count(),
        'total_modifications': Modification.objects.count(),
        'weapons_categories': Category.objects.all()[:5],  # Últimas 5 categorías
    }
    
    return {
        'tarkov_stats': stats
    }




