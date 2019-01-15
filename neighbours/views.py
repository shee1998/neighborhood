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

