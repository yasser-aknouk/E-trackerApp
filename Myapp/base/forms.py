from django import forms
from .models import product



class AddForm(forms.ModelForm):
    class Meta:
        model = product
        fields={'url_product',}
