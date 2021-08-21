from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from home.models import DonorRequest

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 150)
    company =forms.CharField(max_length=200)
    email_address = forms.EmailField(max_length = 150)
    phone = forms.CharField(max_length=10)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

        
         
class DonorForm(forms.ModelForm):
    
    class Meta:
        model = DonorRequest
        fields = ['full_name', 'email_id', 'date_of_birth', 'phone', 'city', 'state','pin_code', 'weight', 'blood_group','agree']
        widgets = {
            'full_name': forms.TextInput(attrs = {'class':'form-control'}),
            'city': forms.TextInput(attrs = {'class':'form-control'}),
            'state': forms.TextInput(attrs = {'class':'form-control'}),
            'pin_code': forms.NumberInput(attrs = {'class':'form-control'}),
            'phone': forms.TextInput(attrs = {'class':'form-control'}),
            'date_of_birth': forms.TextInput(attrs = {'label':'Date of birth', 'class':'form-control'}),
            'weight': forms.NumberInput(attrs = {'class':'form-control'}),
            'email_id': forms.EmailInput(attrs = {'class':'form-control'}),
        }