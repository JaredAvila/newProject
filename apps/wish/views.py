from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *

def home(request):
    try:
        user = User.objects.get(hId = request.session['hId'])
    except:
        errors = {"error": 'You must be logged in to do that. Tisk tisk!'}
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
        return redirect('/wish/logout')
    return render(request, 'wish/home.html', {"wishes": Wish.objects.filter(userWish=user), "grants": Granted.objects.all()})

def logout(request):
    request.session['hId'] = 'logged out'
    request.session['id'] = ''
    request.session['fName'] = ''
    request.session['myWishesTotal'] = ''
    request.session['myGrantedTotal'] = ''
    request.session['grantedCount'] = ''
    request.session['editWish'] = ''
    request.session['editDesc'] = ''
    request.session['editId'] = ''
    return redirect('/login')

def stats(request, id):
    user = User.objects.get(id=id)
    request.session['myWishesTotal'] = Wish.objects.filter(userWish = user).count()
    request.session['myGrantedTotal'] = Granted.objects.filter(wisher = user.fName).count()
    request.session['grantedCount'] = Granted.objects.all().count()
    return render(request, 'wish/stats.html')

def create(request):
    return render(request, 'wish/create.html')

def edit(request, id):
    try:
        user = User.objects.get(hId = request.session['hId'])
        wish = Wish.objects.get(id=id)
        request.session['editWish'] = wish.wish
        request.session['editDesc'] = wish.desc
        request.session['editId'] = wish.id
    except:
        errors = {"error": 'You must be logged in to do that. Tisk tisk!'}
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
        return redirect('/wish/logout')
    return render(request, 'wish/edit.html')

def editting(request, id):
    errors = Wish.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    wish = Wish.objects.get(id=id)
    wish.wish = request.POST['wish']
    wish.desc = request.POST['desc']
    wish.save()
    return redirect('/wish')

def add(request):
    errors = Wish.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    print(request.POST['wish'])
    user = User.objects.get(hId = request.session['hId'])
    newWish = Wish(wish=request.POST['wish'], desc=request.POST['desc'], userWish = user)
    newWish.save()
    return redirect('/wish')

def delete(request, id):
    delWish = Wish.objects.get(id=id)
    delWish.delete()
    return redirect('/wish')

def granted(request, id):
    wisher = User.objects.get(hId=request.session['hId']).fName
    wish = Wish.objects.get(id=id)
    grant = Granted(granted=wish.wish, grantedDesc=wish.desc, wishCreatedAt=wish.created_at, wisher=wisher, )
    grant.save()
    wish.delete()
    return redirect('/wish')

def like(request, id):
    liked = Granted.objects.get(id=id)
    user = User.objects.get(hId=request.session['hId'])
    liked.grantedLikes.add(user)
    return redirect('/wish')