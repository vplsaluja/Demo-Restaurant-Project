from django.forms import ModelForm
from .models import RestModel, RestMenu


class RestForm(ModelForm):
    class Meta:
        model = RestModel
        fields = ('rest_name', 'rest_food_type', 'rest_rating', 'rest_offer', 'rest_discount', 'rest_expected_price',)


class DishForm(ModelForm):
    class Meta:
        model = RestMenu
        fields = ('related_rest', 'dish_name', 'dish_price', 'dish_is_veg', 'dish_rating', 'dish_desc',)
