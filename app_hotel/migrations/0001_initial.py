# Generated by Django 2.0.4 on 2018-07-21 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestMenu',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.CharField(max_length=200)),
                ('dish_logo', models.ImageField(upload_to='static/images/products')),
                ('dish_price', models.FloatField()),
                ('dish_is_veg', models.BooleanField(default=True)),
                ('dish_rating', models.FloatField(default=0)),
                ('dish_desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='RestModel',
            fields=[
                ('rest_id', models.AutoField(primary_key=True, serialize=False)),
                ('rest_name', models.CharField(max_length=140)),
                ('rest_logo', models.ImageField(upload_to='static/images/products')),
                ('rest_food_type', models.CharField(max_length=10)),
                ('rest_rating', models.FloatField(default=0)),
                ('rest_offer', models.CharField(blank=True, max_length=100)),
                ('rest_discount', models.FloatField(default=0)),
                ('rest_expected_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RestReviews',
            fields=[
                ('review_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('review_desc', models.CharField(blank=True, max_length=250)),
                ('rating_given', models.FloatField(max_length=5)),
                ('reviewed_rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_rest', to='app_hotel.RestModel')),
            ],
        ),
        migrations.AddField(
            model_name='restmenu',
            name='related_rest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_rest', to='app_hotel.RestModel'),
        ),
    ]
