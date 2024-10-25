from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            error = 'Usuario o contraseña incorrectas.'
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')    

def dashboard(request):
    return render(request, 'dashboard.html')

def logout(request):
    auth_logout(request)
    return redirect('login')