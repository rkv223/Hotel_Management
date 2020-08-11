from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import U_Registration


# Create your views here.
def index(request):
    return render(request, "index.html")


def user_register1(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        password = request.POST['password']

        user = User.objects.create( username=first_name, last_name=last_name, email=email, first_name=first_name)
        user.set_password(password)
        user.save()
        print("user created")
        return redirect('/')

    else:
        return render(request, "user_register.html")


def staff_register(request):
    return render(request, "staff_register.html")
