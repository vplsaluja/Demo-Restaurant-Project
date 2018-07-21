from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # url(r'^rest/', views.post_rest, name='post_rest'),
    # url(r'^dish/', views.post_dish, name='post_dish'),
    url(r'^restaurants/', views.list_restaurants, name='list_rest'),
]

# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
