from .models import *
from django.shortcuts import render, redirect

def index2(request):
    return render(request, "main.html")

def index3(request):
    return render(request, "index.html")

def index4(request):
    return render(request, "index2.html")

def index5(request):
    return render(request, "index3.html")

def create(request):
	if request.method == "POST":
		b = Person()
		b.name = request.POST.get("name")
		b.email = request.POST.get("email")
		b.password = request.POST.get("pass")
		b.save()
	return HttpResponseRedirect("/signup")