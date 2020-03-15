from django.shortcuts import render
from .models import Bloodonate
from .models import Bloodonate,President,VicePres,Secretory,Members,All,Bloodimg,Moneyimg,Foodimg

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'About.html')
def team(request):
    return render(request,'department.html')   
def blood(request):
    data = Bloodonate.objects.all()
    return render(request,'blooddonation.html',{'y':data})
def gallery(request):
    monimg = Moneyimg.objects.all()
    allimg = All.objects.all()
    bloodimg = Bloodimg.objects.all()
    foodimg = Foodimg.objects.all()
    return render(request,'gallary.html',{'mimg':monimg,'aimg':allimg,'bimg':bloodimg,'fimg':foodimg})
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
    return render(request,'blooddonation.html')

