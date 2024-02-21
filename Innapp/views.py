from django.shortcuts import render
from .models import Bloodonate
from .models import Bloodonate,President,VicePres,Secretory,Jointsecretory,Members,All,Bloodimg,Moneyimg,Foodimg
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'About.html')
def team(request):
    deptdata = President.objects.all()
    vicepres = VicePres.objects.all()
    secre = Secretory.objects.all()
    jointsecre = Jointsecretory.objects.all()
    members = Members.objects.all()
    return render(request,'department.html',{'dep':deptdata,'vp':vicepres,'secretary':secre,'joint':jointsecre,'members':members})   
def blood(request):
    # data = Bloodonate.objects.all()
    
    return render(request,'blooddonation.html')

def donorlist(request):
    bas = Bloodonate.objects.all()
    blod = request.POST.get("blod")
    addres = request.POST.get("address")
    if blod:
        bas=bas.filter(group=blod)
    if addres:
        bas=bas.filter(address=addres)
    return render(request,'donorslist.html',{'klm':bas})

def donate(request):
    return render(request, 'donate.html')

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

def autodeploy(request):
    import subprocess
    success = True
    try:
        process = subprocess.call('/home/ubuntu/autodeploy.sh')
    except:
        process = ''
        success = False
    return JsonResponse({
        'success' : success,
        'data' : "deployment status:{}".format(process)
        })
