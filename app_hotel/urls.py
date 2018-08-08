from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.load_home, name='load_home'),
    url(r'^restaurants/$', views.list_restaurants, name='list_rest'),
    url(r'^restaurants/(?P<pk>[0-9]+)/$', views.restaurant_page, name='rest_page'),
    url(r'^cart/$', views.go_to_cart, name='go_to_cart'),
    url(r'^checkout/$', views.order_placed, name='order_placed'),
]

# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
