from django.shortcuts import render

# Create your views here.
from base.models import Contact


def home(request):
    error = ''
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        try:
            Contact.objects.create(name=name, subject=subject, email=email, message=message)
            error = 'no'
        except:
            error = 'yes'
    x = {'error': error}
    return render(request, 'base/main.html', x)