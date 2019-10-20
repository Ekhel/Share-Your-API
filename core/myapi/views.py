from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,'app/login.html')


@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html')
    