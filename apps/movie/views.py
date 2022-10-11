from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def index(request):
    """Returns the homepage for the site"""
    search_term = request.GET.get('search_movie') or ''
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
    ctx = {'search_term': search_term, 'movies': movies}
    return render(request, 'movie/index.html', ctx)


def about(request):
    """Returns the about page for the site"""
    return HttpResponse('<h1>About Us</h1>')


def signup(request):
    """Returns the about page for the site"""
    email = request.GET.get('email') or ''
    ctx = {'email': email}
    return render(request, 'movie/signup.html', ctx)
