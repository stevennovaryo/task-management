from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist_movies = MyWatchList.objects.all()
    context = {
        'movie_list' : data_watchlist_movies,
        'name' : 'Uttsada Jason',
        'npm' : '2106629976',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_watchlist_movies = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist_movies), content_type="application/xml")

def show_json(request):
    data_watchlist_movies = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist_movies), content_type="application/json")
