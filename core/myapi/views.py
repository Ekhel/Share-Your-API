from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import website, linkapi

def login(request):
    return render(request,'app/login.html')


class WebView(ListView):
    model = website
    template_name = 'app/r-web.html'

@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html')


