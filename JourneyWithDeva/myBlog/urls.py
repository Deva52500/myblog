

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="BlogHome"),
    path("blog/", views.index, name="BlogPage"),
    path("about/", views.about, name="AboutUs"),
    path("addContact", views.addContact, name="ContactUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("sites/<int:myid>", views.siteView, name="SiteView"),
    ]
