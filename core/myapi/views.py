from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import website, linkapi

def login(request):
    return render(request,'app/login.html')


class WebView(ListView):
    template_name = 'app/r-web.html'
    model = website

    def get_queryset(self):
        return website.objects.filter(user=self.request.user)


class ApiView(ListView):
    model = linkapi
    template_name = 'app/r-api.html'

    def get_queryset(self):
        return linkapi.objects.filter(user=self.request.user)  

@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html')


