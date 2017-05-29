from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        
    def clean_email(self):
        print (self.cleaned_data)
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if extension not in ['edu', 'com']:
            raise forms.ValidationError('Enter a valid email extension')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # Validate name
        return full_name

        
