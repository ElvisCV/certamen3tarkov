from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML, Field

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre'
        })
    )
    
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )
    
    subject = forms.CharField(
        max_length=200,
        label='Asunto',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '¿Sobre qué quieres contactarnos?'
        })
    )
    
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Escribe tu mensaje aquí...'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Field('subject', css_class='form-group mb-3'),
            Field('message', css_class='form-group mb-3'),
            Submit('submit', 'Enviar Mensaje', css_class='btn btn-warning btn-lg mt-3'),
            HTML('<br><small class="text-muted">* Este formulario es una demostración. No envía correos en esta versión.</small>')
        )

