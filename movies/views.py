from django.shortcuts import render

from movies.models import Movie

def movie_list(request):
    movies=Movie.objects.all()
    context={'movies':movies,}
    return render(request,'movies/movie_list.html',context)
