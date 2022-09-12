from django.shortcuts import render

def show_katalog(request):
    return render(request, "katalog.html")