from django.forms import ModelForm
from django import forms

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


class OrderForm(ModelForm):
    class Meta:
        model = models.OrderPlaced
        fields = ('list_order', 'amount_paid')


class ReviewForm(ModelForm):
    review_desc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Review Desc'}))
    rating_given = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating'}))

    class Meta:
        model = models.RestReviews
        fields = ('review_desc', 'rating_given')
