from django import forms
class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=122,required=True)
    email=forms.EmailField(required=True)
    query=forms.CharField(max_length=122,required=True)