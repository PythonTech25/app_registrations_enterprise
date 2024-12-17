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