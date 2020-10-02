from django.shortcuts import render

# Create your views here.
def review_index(request):
    return render(request, 'review/main.html')