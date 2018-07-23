from django.shortcuts import render

from . import forms
from . import models


# def post_rest(request):
#     rest_form = forms.RestForm(request.POST)
#     if request.method == 'POST':
#         if rest_form.is_valid():
#             rest_form.save()
#         else:
#             print('error not valid')
#
#     context = {'rest_form': rest_form, }
#     return render(request, 'form_rest.html', context)
#
#
# def post_dish(request):
#     dish_form = forms.DishForm(request.POST)
#     if dish_form.is_valid():
#         dish_form.save()
#     else:
#         print('error not valid data')
#     return render(request, 'dish_form.html', {'dish_form': dish_form})

def list_restaurants(request):
    rest_list = models.RestModel.objects.all()
    return render(request, 'restaurant_list.html', {"rest_list": rest_list, })


def restaurant_page(request, pk):
    print('inside method')
    rest_obj = models.RestModel.objects.get(rest_id=pk)
    if rest_obj is None:
        print('404 not found')
    else:
        print('found')
    return render(request, 'restaurant_page.html', {"rest_obj": rest_obj, })
