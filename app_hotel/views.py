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
        bill_amount = 0
        selected_dish = models.RestMenu.objects.filter(pk__in=cookies.keys())
        for dish in selected_dish:
            bill_amount = (dish.dish_price * cookies[str(dish.dish_id)]) + bill_amount
            request.session['bill_amount'] = bill_amount
    return render(request, 'cart.html', {'selected_dish': selected_dish, 'bill_amount': bill_amount, })


def order_placed(request):
    order = models.OrderPlaced.objects.create()
    ordered_item = request.COOKIES.get('added_dish')
    paid_amount = request.session.get('bill_amount')
    order.amount_paid = paid_amount
    order.list_order = ordered_item
    order.save()
    return render(request, 'order_placed.html')


def order_summary(request):
    orders = models.OrderPlaced.objects.all()
    order_dict = dict()
    for order in orders:
        ordered_dishes = json.loads(order.list_order)
        dishes = models.RestMenu.objects.filter(pk__in=ordered_dishes.keys())
        order_dict[order.order_id] = dishes

    data = {'orders': orders, 'order_dict': order_dict, }
    return render(request, 'order_summary.html', data)
