from django.urls import re_path as url
from . import views


urlpatterns = [
    url(r'^FridgeApp_items$', views.itemAPI),
    url(r'^FridgeApp_items/([0-9]+)$', views.itemAPI),
    url(r'^FridgeApp_category$', views.categoryAPI),
    url(r'^FridgeApp_category/([0-9])$', views.categoryAPI)
]