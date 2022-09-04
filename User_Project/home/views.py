from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')
    
def loginUser(request):
    if request.method == 'POST':
        # check if users credentials (search : django authentication)
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        print(username_,password_)
        user = authenticate(username=username_, password=password_)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect('/  ')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('/login')