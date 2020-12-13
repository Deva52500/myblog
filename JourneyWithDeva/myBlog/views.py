from django.shortcuts import render
from .models import SiteLoc, User
from math import ceil

from django.core.mail import send_mail

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Site.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allPlaces = []
    catplaces = SiteLoc.objects.values('country', 'id')
    cats = {item['country'] for item in catplaces}
    for cat in cats:
        prod = SiteLoc.objects.filter(country=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allPlaces.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allPlaces':allPlaces}
    return render(request, 'blog/index.html', params)

def about(request):
    return render(request, 'blog/about.html')

def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')

def siteView(request, myid):
    # Fetch the product using the id
    site = SiteLoc.objects.filter(id=myid)


    return render(request, 'blog/siteView.html', {'site':site[0]})






def addContact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
    #    print(name)
    #    print(email)
        send_mail('Welcome to JourneyWithDeva',
                  'Thanks for being a part of this exciting journey. We will notify you with recent updates.',
                  'akshayraikar94@gmail.com',
                  [email],
                  fail_silently=False)
        usr = User(user_name=name, user_email=email)
        usr.save()
        return render(request, 'blog/about.html')






