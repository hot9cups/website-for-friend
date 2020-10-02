from django.shortcuts import render

# Create your views here.
def addcontact(request):
    return render(request, 'contactform/form.html')