from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('test-404/', views.test_404, name='test_404'),  # Ruta de prueba para ver el 404
]