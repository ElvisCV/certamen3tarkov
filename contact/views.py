from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')
    
    def form_valid(self, form):
        # El formulario no necesita ser funcional según los requisitos
        messages.success(self.request, '¡Gracias por tu mensaje! Te responderemos pronto.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Contacto - Tarkov Wiki'
        return context




