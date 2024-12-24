from django.forms import ModelForm
from . import models

class EmployeeForm(ModelForm):
    class Meta:
        model = models.RegisterEmployee
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Primeiro nome'}
        )
        
        self.fields['lastname'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Sobrenome'}
        )
        
        self.fields['credential'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Credencial'}
        )
        
        self.fields['enterprise'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Empresa'}
        )
        
        self.fields['sector'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Setor'}
        )
        
        self.fields['user'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Portaria'}
        )
        
        
class KeyForm(ModelForm):
    class Meta:
        model = models.RegisterKey
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Nome da chave'}
        )
        
        self.fields['number'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Número'}
        )
        
        self.fields['amount'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Quantidade de cópias'}
        )
        
        self.fields['user'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Portaria'}
        )
        
        
class EPIForm(ModelForm):
    class Meta:
        model = models.RegisterEPI
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Nome da chave'}
        )
        
        self.fields['number'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Número'}
        )
        
        self.fields['amount'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Quantidade de cópias'}
        )
        
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Descrição'}
        )
        
        self.fields['user'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Portaria'}
        )
        
    
        
        
        