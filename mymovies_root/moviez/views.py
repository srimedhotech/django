from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from . models import MovieModel


def index(request):
	movielist = MovieModel.objects.all()
	return render(request, 'moviez/moviez.html', {'movielist' : movielist} )
	#return render(request, 'moviez/movies.html', {'movielist' : movielist} )

def movies(request):
	movielist = MovieModel.objects.all()
	return render(request, 'moviez/movies.html', {'movielist' : movielist} )

"""
mv1 = MovieModel(1, "Spider Man", "Fictious movie", 4)
	mv2 = MovieModel(2, "Gandhi", "Real story", 5)
	mv3 = MovieModel(3, "Avatar", "Graphical magic", 5)
	movielist = [mv1, mv2, mv3]
"""