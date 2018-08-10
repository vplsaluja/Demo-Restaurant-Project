# from django.contrib.gis.db import models
from django.db import models


# Create your models here.
class RestModel(models.Model):
    rest_id = models.AutoField(primary_key=True)
    rest_name = models.CharField(max_length=140, blank=False)
    rest_logo = models.ImageField(upload_to='gallery')
    rest_food_type = models.CharField(max_length=10)
    rest_rating = models.FloatField(default=0)
    rest_offer = models.CharField(blank=True, max_length=100)
    rest_discount = models.FloatField(default=0)
    rest_expected_price = models.IntegerField(default=0)


class RestMenu(models.Model):
    related_rest = models.ForeignKey('RestModel', related_name="related_rest", on_delete=models.DO_NOTHING)
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(blank=False, max_length=200)
    dish_logo = models.ImageField(upload_to='gallery', blank=True)
    dish_price = models.FloatField(blank=False)
    dish_is_veg = models.BooleanField(default=True)
    dish_rating = models.FloatField(default=0)
    dish_desc = models.CharField(blank=False, max_length=300)


class RestReviews(models.Model):
    reviewed_rest = models.ForeignKey('RestModel', related_name='reviewed_rest', on_delete=models.CASCADE)
    review_id = models.AutoField(primary_key=True, auto_created=True)
    review_desc = models.CharField(blank=True, max_length=250)
    rating_given = models.FloatField(max_length=5, blank=False)


class OrderPlaced(models.Model):
    order_id = models.AutoField(primary_key=True, auto_created=True)
    list_order = models.TextField(blank=True, default='')
    amount_paid = models.FloatField(blank=True, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
