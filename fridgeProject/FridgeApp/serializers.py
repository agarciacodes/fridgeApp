from rest_framework import serializers
from .models import Items, Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'item_name', 'category_name', 'quantity', 'date')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('categoryName_id', 'category_date')
