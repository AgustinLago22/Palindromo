from django import forms 
from checker_palindromo.models import Words

class PalindromeForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = '__all__'