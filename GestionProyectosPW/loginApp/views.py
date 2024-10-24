from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
#from django import http
from .forms import LoginForm 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
                                username=cd['username'], 
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return http.HttpResponse('Authenticated successfully')
                    return redirect('index.html') 
                else:
                    #return http.HttpResponse('Disabled account')
                    return redirect('index.html')
            else:
                #return http.HttpResponse('Invalid login')
                return redirect('index.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
       

def index(request):
    return render(request, "index.html")
