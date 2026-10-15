from django.shortcuts import render
from .forms import LoginModelForm
from .models import Customer
def greeting(request):
    data = Customer.objects.all().values(id,email)
    print(data)
    return render(request,'index.html',{'data':data})