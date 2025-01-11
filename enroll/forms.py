from django import forms
from .models import user
class student_registration(forms.ModelForm):
    class Meta:
        model = user
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control required'}),
            'email':forms.TextInput(attrs={'class':'form-control required'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control required'}),
            }