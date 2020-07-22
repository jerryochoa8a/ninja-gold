from django.shortcuts import render, redirect
import random

def index(request):
    if "gold" not in request.session:
        request.session["gold"]=0
    return render(request, "index.html")

def farmfun(request):
    request.session["temp"] = random.randrange(10, 20)
    request.session["gold"] = request.session["gold"] + request.session["temp"]
    request.session["console"] = "from the farm"
    return redirect('/')


def cavefun(request):
    request.session["temp"] = random.randrange(5, 10)
    request.session["gold"] = request.session["gold"] + request.session["temp"]
    request.session["console"] = "from the cave" 
    return redirect('/')


def housefun(request):
    request.session["temp"] = random.randrange(2, 5)
    request.session["gold"] = request.session["gold"] + request.session["temp"]
    request.session["console"] = "from the house"
    return redirect('/')


def casinofun(request):
    request.session["temp"] = random.randrange(-50, 50)
    request.session["gold"] = request.session["gold"] + request.session["temp"]
    if request.session["temp"] < 0:
        request.session["console"] = "taken from your gold. sorry."
    else:
        request.session["console"] = "from the casino"
    return redirect('/')


def restart(request):
    request.session["gold"] = 0
    return redirect('/')