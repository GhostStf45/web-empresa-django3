from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        #Mandar el diccionario por el metodo post del formulario
        contact_form = ContactForm(data=request.POST)
        #Recuperar la información
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                'no contestar@inbox.mailtrap.io',
                ["topguncounter@gmail.com"],
                reply_to=[email]

            )
            try:
                email.send()
                # TodX ha ido bien, redireccionamos a OK
                return redirect(reverse('contact') + '?ok')
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})