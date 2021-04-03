from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    return render(request, 'registration/register.html')

def create_new(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    new_user = User.objects.create(
        username=username,
        email=email,
    )
    new_user.set_password(password)
    new_user.save()
    return redirect('/')