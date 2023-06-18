from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import Movieform


# Create your views here.
def index(request):
    film = Movie.objects.all()
    context = {
        'filmlist': film
    }
    return render(request, 'index.html', context)


def details(request, filmid):
    film = Movie.objects.get(id=filmid)
    return render(request, "details.html", {'film': film})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    forms = Movieform(request.POST or None, request.FILES, instance=movie)
    if forms.is_valid():
        forms.save()
        return redirect("/")
    return render(request, 'edit.html', {'forms': forms, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
