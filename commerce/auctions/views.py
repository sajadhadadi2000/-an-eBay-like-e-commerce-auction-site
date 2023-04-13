from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, List, Bid, Coments, Watchlist
from .forms import ListForm

def index(request):
    return render(request, "auctions/index.html", {"listing" : List.objects.all()})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def createlist(request):
    # Getting list
    if request.method == 'POST':
        form = ListForm(request.POST)
        
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            start_bid = form.cleaned_data['start_bid']
            url_image = form.cleaned_data['url_image']

            newlist = List(author=user, title=title, description=description, category=category, start_bid=start_bid, url_image=url_image)
            newlist.save()
            
            return HttpResponseRedirect(reverse("index"))
        else:
            form = ListForm()
            return render(request, "auctions/createlist.html", {"form" : form})

    else:
        form = ListForm()
        return render(request, "auctions/createlist.html", {"form" : form})


def listpage(request, id):
    list = List.objects.get(id=id)
    comments = list.comments.all()
    watchlist = Watchlist.objects.filter(list=list, author=request.user)
    
    return render(request, "auctions/listpage.html", {
        "list" : list, 
        "comments": comments,
        "watchlist":watchlist
        })


@login_required(login_url='login')
def comment(request, listid):
    if request.method == "POST":
        # user = request.user
        comment = request.POST["comment"]
        list = List.objects.get(pk=listid)
        newcomment = Coments(coment=comment, list=list)
        newcomment.save()
        return HttpResponseRedirect(reverse('listpage', args=(list.id,)))

@login_required(login_url='login')
def addwatchlist(request, listid):
    list = List.objects.get(id=listid)
    user = request.user
    
    try:
        Watchlist.objects.get(list=list.id, author=user).delete()
    except:
        newwatchlist = Watchlist(author=user, list=list)
        newwatchlist.save()
    return HttpResponseRedirect(reverse('listpage', args=(list.id,)))


@login_required(login_url='login')
def comment(request, listid):
    if request.method == "POST":
        comment = request.POST["comment"]
        list = List.objects.get(pk=listid)
        newcomment = Coments(coment=comment, list=list)
        newcomment.save()
        return HttpResponseRedirect(reverse('listpage', args=(list.id,)))
    


@login_required(login_url='login')
def watchlist(request):
        user = request.user
        watchlist = Watchlist.objects.filter(author=user)
        return render(request, "auctions/watchlist.html", {"lists" : watchlist})

def category(request):
    category = List.categories
    return render(request, "auctions/category.html", {"categories" : category})

"""
    if request.user.is_authenticated:
    # Do something for authenticated users.
    ...
    else:
    # Do something for anonymous users.

    # if user login 
        # can able to bid with condition
        # if user created this list 
            # can close the list
        # if user visit a closed list that owen bid won  
            # show the win
        
    #else: user not login

    
from django.db.models import Max
from myapp.models import MyModel

max_amount = MyModel.objects.aggregate(Max('amount'))['amount__max']

"""