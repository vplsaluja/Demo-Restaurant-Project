import json

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


def go_to_cart(request):
    if not request.COOKIES.get('added_dish'):
        print('cookie not found')
    else:
        cookies = json.loads(request.COOKIES.get('added_dish'))
        selected_dish = list()
        bill_amount = 0
        for key, value in cookies.items():
            dish = models.RestMenu.objects.get(dish_id=key)
            selected_dish.append(dish)
            bill_amount = (dish.dish_price * value) + bill_amount
    return render(request, 'cart.html', {'selected_dish': selected_dish, 'bill_amount': bill_amount, })


def order_placed(request):
    return render(request, 'order_placed.html')
