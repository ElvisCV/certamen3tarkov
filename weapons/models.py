from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Categoría de armas (Rifle, Subfusil, Pistola, etc.)"""
    name = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
    description = models.TextField(verbose_name="Descripción")
    icon = models.CharField(max_length=50, default="fa-gun", verbose_name="Icono Font Awesome")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weapons:weapon_list') + f'?category={self.id}'

class Weapon(models.Model):
    # 5 atributos obligatorios
    name = models.CharField(max_length=200, verbose_name="Nombre del Arma")
    description = models.TextField(verbose_name="Descripción")
    img = models.URLField(max_length=500, verbose_name="URL de Imagen")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, 
                                  verbose_name="Categoría", related_name='weapons')
    caliber = models.CharField(max_length=50, default="5.56x45mm", verbose_name="Calibre")
    is_available = models.BooleanField(default=True, verbose_name="Disponible")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    
    class Meta:
        verbose_name = "Arma"
        verbose_name_plural = "Armas"
        ordering = ['-created']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weapons:weapon_list')

class Modification(models.Model):
    """Modificaciones que se pueden aplicar a las armas"""
    name = models.CharField(max_length=200, verbose_name="Nombre de la Modificación")
    description = models.TextField(verbose_name="Descripción")
    modification_type = models.CharField(max_length=50, choices=[
        ('muzzle', 'Boca de Cañón'),
        ('stock', 'Culata'),
        ('grip', 'Empuñadura'),
        ('sight', 'Mira'),
        ('magazine', 'Cargador'),
        ('other', 'Otro')
    ], verbose_name="Tipo de Modificación")
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='modifications',
                               verbose_name="Arma Compatible")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    class Meta:
        verbose_name = "Modificación"
        verbose_name_plural = "Modificaciones"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.weapon.name}"