from audioop import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404,HttpResponseForbidden
from django.urls import reverse
from django.template.loader import render_to_string

menu = ["About", "Add Article", "Contacts", "Log In"]


class MyClass:

    def __init__(self,a,b):
        self.a = a
        self.b = b


def index(request):
    # t = render_to_string("index.html")
    # return HttpResponse(t)
    data = {
        "title": "Home Page",
        "description": "Hello home page",
        "menu": menu,
        "float": 22.3,
        "int": 22,
        "lst": [7,5,"hello",False],
        "set": {1,2,1,3,2},
        "dd": {"name": "John Smith", "password": "123456789"},
        "cls": MyClass(45,89)
    }
    return render(request,"blog/index.html", data)


def about(request):
    # t = render_to_string("index.html")
    # return HttpResponse(t)
    data = {"title": "About page"}
    return render(request,"blog/about.html", data)


def categories(request):
    return HttpResponse(f"<h1> Categories </h1>")


def categories_by_id(request,cat_id):
    return HttpResponse(f"<h1> Categories </h1><p>ID: {cat_id}</p>")


def categories_by_slug(request, cat_slug=None):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1> Categories </h1> <p> SLUG: {cat_slug} </p>")


def archive(request,year):
    if year > 2024:
        # return redirect("/",permanent=True)
        # return redirect(index,permanent=True)
        # return redirect("index",permanent=True)
        # return redirect("cat_slug","armenia")
        uri = reverse("cat_slug", args="armenia")
        return  redirect(uri, permanent=True)

        # return HttpResponseForbidden()
    return HttpResponse(f"<h1> Archive </h1> <p> ARCHIVE: {year} </p>")


def page_not_found(request,exception):
    return HttpResponseNotFound(f"<h1> Page Not Found 404 {exception}</h1>")
