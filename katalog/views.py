from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_catalog_items = CatalogItem.objects.all()
    context = {
        'item_list' : data_catalog_items,
        'name' : 'Uttsada Jason',
        'npm' : '2106629976',
    }
    return render(request, "katalog.html", context)