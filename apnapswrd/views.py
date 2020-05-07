from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from apnapswrd.models import contactus, newentry

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    entry = newentry.objects.filter(user=request.user)
    toshow = {'entry': entry}
    return render(request, 'index.html', toshow)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['cname']
        email = request.POST['cemail']
        message = request.POST['cmessage']
        newcontact = contactus(name=name, email=email, message=message)
        newcontact.save()
        messages.success(request, 'Your Message has been sent')
    return render(request, 'contact.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user is not None)
        if user is not None:
            login(request, user)
            #messages.success(request, 'Login Successfully')
            return redirect("/")
        else:
            messages.warning(request, 'Invalid username or password')
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def registerUser(request):
    if request.method=="POST":
        username = request.POST['rusername']
        email = request.POST['remail']
        name = request.POST['rname']
        pass1 = request.POST['rpass1']
        pass2 = request.POST['rpass2']
        userc  = User.objects.get(username=username)

        if len(username) > 30:
            messages.warning(request, 'Username should be less than 30 characters.')
            return redirect("/register")
        if pass1 != pass2:
            messages.warning(request, 'Password should Match')
            return redirect('/register')
        if userc:
            messages.warning(request, 'Username already exists')
            return redirect('/register')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name
        myuser.save()
        messages.success(request, 'Account Registered Successfully')
        return redirect('/login')

    return render(request, 'register.html')

def addnew(request):
    if request.method == "POST":
        entryname = request.POST.get("entryname")
        url = request.POST.get("entryurl")
        username = request.POST.get("entryusername")
        password = request.POST.get("entrypassword")
        user = request.user

        entry = newentry(entryname=entryname, url=url, username=username, password=password, user=user)
        entry.save()
        messages.success(request, 'New Entry Added Successfully')

    return redirect('/')

def search(request):
    query = request.GET['query']
    entryname = newentry.objects.filter(entryname__icontains=query, user=request.user)
    entryurl = newentry.objects.filter(url__icontains=query, user=request.user)
    entry = entryname.union(entryurl)
    if entry.count() == 0:
        messages.warning(request, 'No matching entry')
    toshow = {'entry': entry}
    return render(request, 'search.html', toshow)

def delete(request):
    deletename = request.GET['deletename']
    entry = newentry.objects.filter(entryname=deletename, user=request.user)
    if entry.count() == 0:
        messages.warning(request, 'No matching entry')
    else:
        entry.delete()
        messages.success(request, 'Deleted Successfully')
    return redirect('/')