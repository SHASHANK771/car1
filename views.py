from django.shortcuts import render
from app.models import From1
from app.models import From2
# Create your views here.
def index(request):
  return render(request, 'app/index.html')


def formView(request):
  return render(request, 'app/formpage.html')


def about(request):
  return render(request, 'app/about.html')

def login(request):
  return render(request, 'app/login.html')

def reg(request):
  return render(request, 'app/reg.html')


def services(request):
  return render(request, 'app/services.html')

def ins(request):
  return render(request, 'app/ins.html')


def student(request):
  return render(request,'app/student.html')
def from3(request):
    return render(request,'app/from3.html')   

def from1(request):
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        #last=request.POST.get('last')
        #father_name=request.POST.get('father_name')
        #mother_name=request.POST.get('mather_name')
        email=request.POST.get('email')
        #address=request.POST.get('address')
        #city=request.POST.get('city')
        #number=request.POST.get('number')
        carmodel=request.POST.get('carmodel')
        #Aadhrnumber=request.POST.get('Aadhrnumber')
        f=From1.objects.get_or_create(name=name,number=number,email=email,carmodel=carmodel)[0]
        f.save()
    return render(request,'app/from1.html')

def from2(request):
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        #father_name=request.POST.get('father_name')
        #mother_name=request.POST.get('mather_name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        about=request.POST.get('about')
        comment=request.POST.get('comment')
        
        #Aadhrnumber=request.POST.get('Aadhrnumber')
        f=From2.objects.get_or_create(name=name,number=number, email=email,address=address,city=city,about=about,comment=comment)[0]
        f.save()
    return render(request,'app/from2.html')         

