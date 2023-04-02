from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files import File
import urllib.request
import os
from django import forms

from .models import User, Listing, Comment


def index(request):
    active_listings = Listing.objects.all()
    return render(request, "auctions/index.html",{
        "active_listings":active_listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        

        # Check if authentication successful
        if user is not None:
            login(request, user)
            
            if "next" in request.POST:
                next = request.POST["next"]
                if next[0:len(next)-1] == "listings/":
                    print("Mpika")
                    return HttpResponseRedirect(reverse(listingPage,args=[next[-1]]))
                elif next[0:len(next)-2] == "listings/":
                    return HttpResponseRedirect(reverse(listingPage,args=[next[-2:]]))
                
                return HttpResponseRedirect(reverse(next))
            else:
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        next = ""
        if "next" in request.GET:
                next = request.GET["next"]
                next = next[1:]
        return render(request, "auctions/login.html",{
            "next" : next
        })


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

@login_required()
def createListing(request):
    if request.method == "POST":
        
        title = request.POST["title"]
        description = request.POST["description"]
        img_url = request.POST["url"]
        price = request.POST["price"]
        category = request.POST["category"]
        user = request.user

            # Store in database
        listing = Listing(title=title,description=description,price=price,category=category,owner=user)
        listing.save()
        if img_url != "":
            basePath = "http://127.0.0.1:8000/media/uploads/"
            result = urllib.request.urlretrieve(basePath+img_url)
            img_name = os.path.basename(img_url)
            index = img_name.rfind(".")
            img_name = str(listing.id) + img_name[index:] 


            listing.photo.save(
                img_name,
                File(open(result[0], 'rb'))
            )
            listing.save()

        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/createlisting.html")

@login_required()
def listingPage(request, id):
    listing = Listing.objects.get(id=id)
    watchlist = request.user.watchlist.all()
    user = request.user
    
    if listing in watchlist:
        add = False
    else:
        add = True

    showClose = False
    if listing.owner == user:
        showClose = True

    notification = ""
    if request.method == "POST":
        if "add" in request.POST:
                user.watchlist.add(listing)
                add = False

        elif "remove" in request.POST:
            user.watchlist.remove(listing)
            add = True
        
        elif "bid" in request.POST:
            bid = float(request.POST["bid_number"])
            if bid < listing.price:
                notification = "The amount must be greater than or equal to the price"
            else:
                listing.price = bid
                listing.bid += 1
                listing.bid_winner = user
        elif "close_bid" in request.POST:
            listing.is_closed = True
        elif "add_comment" in request.POST:
            message = request.POST["message"]
            comment = Comment(user=user,message=message)
            comment.save()
            listing.comments.add(comment)

    listing.save() 
    return render(request, "auctions/listing.html",{
        "listing":listing, "add":add, "notification":notification, "showClose":showClose
    })

@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html")

def categories(request):
    return render(request, "auctions/categories.html")

def category_listings(request,category):
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/category_listings.html",{
        "listings":listings, "category": category
    })
