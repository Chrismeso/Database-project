from django.shortcuts import render,redirect
from medicioapp.models import Contact
from  medicioapp.models import Branch
from medicioapp.models import Appointment
# Create your views here.

def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')
def about(request):
    return render(request, 'about.html')
def doctors(request):
    return render(request, 'doctors.html')

def departments(request):
    return render(request, 'departments.html')
def home(request):
    return render(request, 'home.html')
def services(request):
    return render(request, 'services.html')
def contacts(request):
    if request.method == 'POST':
        all = Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      message=request.POST['message']
                      )
        all.save()
        return redirect('/contacts')
    else:
        return render(request,'contacts.html')

def branch(request):
    if request.method == 'POST':
        all = Branch(name=request.POST['name'],
                      location=request.POST['location'],
                      manager=request.POST['manager'],
                      email=request.POST['email']
                      )
        all.save()
        return redirect('/branch')
    else:
        return render(request,'branch.html')

def appointment(request):
    if request.method == 'POST':
        myappointment = Appointment(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      date=request.POST['date'],
                      department=request.POST['department'],
                      doctor=request.POST['doctor']
                      )
        myappointment.save()
        return redirect('/appointment')
    else:
        return render(request,'appointment.html')

