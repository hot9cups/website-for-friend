from django.shortcuts import render
from .models import Contact

# Create your views here.
def showform(request):
    return render(request, 'contactform/form.html')

def addcontact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    extension = request.POST.get('extension')
    mobile_number = request.POST.get('mobile')
    message = request.POST.get('message')
    try:
        contact = Contact.objects.get(email=email)
        contact.mobile_extn = extension
        contact.mobile_number = mobile_number
        contact.message = message
        contact.save()
    except:
        contact = Contact(name=name, email=email, mobile_extn=extension, mobile_number=mobile_number, message=message).save()
    return render(request, 'contactform/form.html')