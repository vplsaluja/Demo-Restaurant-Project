from django.shortcuts import render

from . import models


def list_restaurants(request):
    rest_list = models.RestModel.objects.all()
    return render(request, 'restaurant_list.html', {"rest_list": rest_list, })


def restaurant_page(request, pk):
    rest_obj = models.RestModel.objects.get(rest_id=pk)
    dish_list = list(models.RestMenu.objects.filter(related_rest=pk))
    if rest_obj is None:
        print('404 not found')
    else:
        print('found')
    return render(request, 'restaurant_page.html', {"rest_obj": rest_obj, "dish_list": dish_list, })


def load_home(request):
    return render(request, 'index.html')
