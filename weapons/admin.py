from django.contrib import admin
from django.utils.html import format_html
from .models import Weapon, Category, Modification

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'created')
    search_fields = ('name', 'description')
    list_filter = ('created',)

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    # Al menos 5 parámetros personalizados:
    # 1. list_display personalizado
    list_display = ('name', 'category', 'caliber', 'is_available', 'created', 'updated', 'modification_count')
    # 2. list_filter personalizado
    list_filter = ('category', 'is_available', 'caliber', 'created', 'updated')
    # 3. search_fields personalizado
    search_fields = ('name', 'description', 'caliber', 'category__name')
    # 4. readonly_fields personalizado
    readonly_fields = ('created', 'updated', 'modification_count_display')
    # 5. fieldsets personalizado con organización
    fieldsets = (
        ('Información del Arma', {
            'fields': ('name', 'description', 'img', 'category')
        }),
        ('Especificaciones', {
            'fields': ('caliber', 'is_available')
        }),
        ('Estadísticas', {
            'fields': ('modification_count_display',),
            'classes': ('collapse',)
        }),
        ('Metadatos', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )
    # 6. list_editable para edición rápida
    list_editable = ('is_available',)
    # 7. date_hierarchy para navegación por fechas
    date_hierarchy = 'created'
    # 8. ordering personalizado
    ordering = ('-created',)
    # 9. list_per_page para paginación
    list_per_page = 25
    
    def modification_count(self, obj):
        """Muestra el número de modificaciones disponibles"""
        count = obj.modifications.count()
        if count > 0:
            return format_html('<span style="color: green;">{}</span>', count)
        return format_html('<span style="color: red;">0</span>', count)
    modification_count.short_description = 'Modificaciones'
    
    def modification_count_display(self, obj):
        """Muestra el número de modificaciones en el detalle"""
        return obj.modifications.count()
    modification_count_display.short_description = 'Total de Modificaciones'

@admin.register(Modification)
class ModificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'weapon', 'modification_type', 'price', 'created')
    list_filter = ('modification_type', 'created', 'weapon__category')
    search_fields = ('name', 'description', 'weapon__name')
    readonly_fields = ('created',)
    fieldsets = (
        ('Información de la Modificación', {
            'fields': ('name', 'description', 'modification_type')
        }),
        ('Compatibilidad', {
            'fields': ('weapon', 'price')
        }),
        ('Metadatos', {
            'fields': ('created',),
            'classes': ('collapse',)
        }),
    )