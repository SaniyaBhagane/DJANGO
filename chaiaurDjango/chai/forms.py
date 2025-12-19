from django import forms
from .models import ChaiVariety, Store

class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label='Select Chai Variety')
    # chai_variety= forms.charfield(max_length=100)