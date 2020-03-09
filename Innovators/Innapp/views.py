from django.shortcuts import render
from .models import Bloodonate

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'About.html')
def team(request):
    return render(request,'department.html')   
def blood(request):
    return render(request,'blooddonation.html')
def gallery(request):
    return render(request,'gallary.html')
def money(request):
    return render(request,'Moneydonation1.html')
def payment(request):
    return render(request,'payment.html')
def contact(request):
    return render(request,'contact.html')



def bloodsave(request):
    name = request.POST.get('name')
    group = request.POST.get('group')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    blood = Bloodonate(name=name,group=group,email=email,contact=contact,address=address)
    blood.save()

