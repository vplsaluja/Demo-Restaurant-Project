from django.forms import ModelForm
from . import models


class RestForm(ModelForm):
    class Meta:
        model = models.RestModel
        fields = ('rest_name', 'rest_food_type', 'rest_rating', 'rest_offer', 'rest_discount', 'rest_expected_price',)


class DishForm(ModelForm):
    class Meta:
        model = models.RestMenu
        fields = ('related_rest', 'dish_name', 'dish_price', 'dish_is_veg', 'dish_rating', 'dish_desc',)


class ReviewForm(ModelForm):
    class Meta:
        model = models.RestReviews
        fields = ('reviewed_rest', 'review_desc', 'rating_given')
