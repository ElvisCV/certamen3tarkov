from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'core/pages/home.html'

class AboutView(TemplateView):
    template_name = 'core/pages/about.html'

class GalleryView(TemplateView):
    template_name = 'core/pages/gallery.html'

class FAQView(TemplateView):
    template_name = 'core/pages/faq.html'

def custom_404(request, exception):
    """Vista personalizada para errores 404"""
    return render(request, '404.html', status=404)