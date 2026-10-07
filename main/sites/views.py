from django.shortcuts import render

def gallery(request):
    return render(request, 'sites/gallery.html')

def contact(request):
    return render(request, 'sites/contact.html')

# Create your views here.
