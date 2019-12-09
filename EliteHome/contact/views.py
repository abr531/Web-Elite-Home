from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contacto(request):
    Contact_form = ContactForm()

    if request.method == "POST":
        Contact_form = ContactForm(data=request.POST)
        if Contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            number = request.POST.get('number','')
            content = request.POST.get('content','')

            email = EmailMessage(
                "Corredora Elite Home : Nuevo mensaje ",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,number,content),
                "No-reply@inbox.mailtrap.io",
                ["abraham.retamal777@gmail.com"],
                reply_to=[email]

            )

            try:
                email.send()
                
                return redirect(reverse('contacto')+"?ok")
            except:
                
                return redirect(reverse('contacto')+"?fail")
            

    return render(request, 'contact/contacto.html',{'form':Contact_form})
