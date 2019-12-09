from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre",required= True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Nombre completo'}
    ))
    email = forms.EmailField(label="Correo electronico",required= True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'ejemplo@dominio.com'}
    ))
    number = forms.CharField(label="Numero de contacto",required= True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'+56 94585127'}
    ),min_length=7, max_length=12)
    content = forms.CharField(label="Mensaje",required= True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 4, 'placeholder':'Escribe tu mensaje'}
    ))

