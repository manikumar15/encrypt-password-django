from django.shortcuts import render
from .models import Register
from .forms import regform
from django.http.response import HttpResponse
from passlib.hash import pbkdf2_sha256


# Create your views here.
def home(request):
    return render(request, 'signup.html')

def register(request):
    if request.method == "POST":
        fform=regform(request.POST)
        if fform.is_valid():
            email=request.POST.get('email')
            password=request.POST.get('password')
            enc_password=pbkdf2_sha256.encrypt(password, rounds=12000,salt_size=32)
          
            data=Register(
                email=email,
                password=enc_password
                )
            data.save()
            fform=regform()
            fdata = Register.objects.all()
            return render(request,'signup.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = regform()
        fdata = Register.objects.all()
    return render(request, 'signup.html',{'fform': fform,'fdata': fdata})