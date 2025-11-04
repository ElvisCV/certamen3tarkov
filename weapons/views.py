from django.views.generic import ListView
from .models import Weapon, Category

class WeaponListView(ListView):
    model = Weapon
    template_name = 'weapons/weapon_list.html'
    context_object_name = 'weapons'
    paginate_by = 10  # 10 registros por página
    
    def get_queryset(self):
        queryset = Weapon.objects.all()
        
        # Filtro 1: Por categoría
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        # Filtro 2: Por disponibilidad
        is_available = self.request.GET.get('available')
        if is_available == 'true':
            queryset = queryset.filter(is_available=True)
        elif is_available == 'false':
            queryset = queryset.filter(is_available=False)
        
        # Filtro 3: Por calibre (búsqueda)
        caliber = self.request.GET.get('caliber')
        if caliber:
            queryset = queryset.filter(caliber__icontains=caliber)
        
        return queryset.order_by('-created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_available'] = self.request.GET.get('available', '')
        context['selected_caliber'] = self.request.GET.get('caliber', '')
        return context