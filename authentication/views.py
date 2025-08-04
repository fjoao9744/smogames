from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return render(request, "login.html", {"error": "Credenciais inválidas"})
    
def register_view(request):
    if request.method == "GET":
        return render(request, "register.html")
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Nome de usuário já existe"})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        
        return redirect("login")

def logout_view(request):
    logout(request)
    return redirect("login")