from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contact_form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'New inquiry from {}'.format(name)
        body = 'Name: {}\nEmail: {}\nMessage: {}'.format(name, email, message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.CONTACT_EMAIL]
        send_mail(subject, body, from_email, to_email, fail_silently=False)
        messages.success(request, 'Thank you for contacting us! We will get back to you shortly.')
    return redirect('contact')
