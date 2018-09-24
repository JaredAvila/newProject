from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def login(request):
    return render(request, 'login/login.html')

def loginValid(request):
    errors = User.objects.validatorLogin(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    loggedIn = User.objects.get(email=request.POST['email'])
    request.session['fName'] = loggedIn.fName
    request.session['id'] = loggedIn.id
    request.session['hId'] = loggedIn.hId
    return redirect('/wish')
def registration(request):
    print('in registration')
    return render(request, 'login/registration.html')

def regValid(request):
    errors = User.objects.validatorReg(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    hashPW = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    hashID = bcrypt.hashpw(request.POST['email'].encode(), bcrypt.gensalt())
    new = User(fName = request.POST['fName'], lName = request.POST['lName'], email = request.POST['email'], password = hashPW, hId = hashID)
    new.save()
    loggedIn = User.objects.get(email=request.POST['email'])
    request.session['fName'] = loggedIn.fName
    request.session['id'] = loggedIn.id
    request.session['hId'] = loggedIn.hId
    return redirect('/wish')

def success(request):
    
    return redirect('/books')
    