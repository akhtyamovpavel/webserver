from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from models import Good

def index(request):
    items = Good.objects.all()
    return render(request, 'index.html', {'goods': items})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return "bad"
        else:
            return render(request, 'login.html', {"message": "Wrong login or password"})
    else:
        return render(request, 'login.html', {})


def show_product(request, product_id):
    item = Good.objects.get(id=product_id)
    return render(request, 'product.html', {'item': item})


def logout_view(request):
    logout(request)
    return redirect('/')