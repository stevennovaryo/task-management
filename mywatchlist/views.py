from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist_movies = MyWatchList.objects.all()
    watched_count, not_watched_count = 0, 0
    for movie in data_watchlist_movies:
        if movie.watched:
            watched_count += 1
        else:
            not_watched_count += 1
    context = {
        'movie_list' : data_watchlist_movies,
        'name' : 'Uttsada Jason',
        'npm' : '2106629976',
        'more_watched' : watched_count >= not_watched_count,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_watchlist_movies = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist_movies), content_type="application/xml")

def show_json(request):
    data_watchlist_movies = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist_movies), content_type="application/json")
