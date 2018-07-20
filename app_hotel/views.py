from django.shortcuts import render

from . import forms


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
