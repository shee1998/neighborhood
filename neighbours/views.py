from django.shortcuts import render,redirect
from .forms import RegistrationForm,ProfileForm,BusinessForm
from .models import Occupants,Neighborhood,Business

# Create your views here.
def signup(request):
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form= RegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form})

def profile(request):
    user = request.user
    businesses= Business.objects.filter(owner=user)
    prof = Occupants.objects.get(name__id=user.id)
    return render(request,'profile.html',{'user':user,'prof':prof,'businesses':businesses})

def edit_profile(request):
    user = request.user
       
    if request.method =='POST':
        name= Occupants(name=request.user)
        form = ProfileForm(request.POST,request.FILES,instance=name)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        try:
            form= ProfileForm(instance=user)
        except:
            me = Occupants.objects.get(name__id=user.id) 
        
            form = ProfileForm(instance=me)
            
    return render(request,'edit_profile.html',{'form':form,'user':user})

def create_profile(request):
    user = request.user
    me = Occupants.objects.get(name__id=user.id) 
    if request.method =='POST':
        if form.is_valid():
            form = ProfileForm(request.POST,request.FILES)
            form.save(commit=False)
            form.user = user
            form.save()
            return redirect('profile')
    else:                
        form = ProfileForm(instance=me)
        
    return render(request,'create_profile.html',{'form':form,'user':user})


def neighborhood_details(request):
    user = Occupants.objects.get(name=request.user.id)
    neighborhood= Neighborhood.objects.get(name=user.neighborhood)
    details = Occupants.objects.filter(neighborhood__name=neighborhood)
    # occupants=neighborhood.all
    return render(request,'details.html',{'details':details})

def business(request):
    user = Occupants.objects.get(name=request.user.id)
    business= Business.objects.all().filter(neighborhood=user.neighborhood)
    return render(request,'business.html',{'business':business})

