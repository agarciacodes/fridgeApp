from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Items, Category
from .serializers import ItemSerializer, CategorySerializer

# Create your views here.

@csrf_exempt
def itemAPI(request, id=0):
    if request.method == 'GET':
        items = Items.objects.all()
        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        items_serializer = ItemSerializer(data=item_data)
        if items_serializer.is_valid():
            items_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = Items.objects.get(id=item_data['id'])
        items_serializer = ItemSerializer(item, data=item_data)
        if items_serializer.is_valid():
            items_serializer.save()
            return JsonResponse("Update Successful", safe=False)
        return JsonResponse("Update failed", safe=False)
    elif request.method == 'DELETE':
        item = Items.objects.get(id=id)
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)

def categoryAPI(request, id=0):
    if request.method == 'GET':
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(category_serializer.data, safe=False)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Category.objects.get(id=category_data['id'])
        category_serializer = CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Update Successful", safe=False)
        return JsonResponse("Update failed", safe=False)
    elif request.method == 'DELETE':
        category = Category.objects.get(id=id)
        category.delete()
        return JsonResponse("Deleted successfully", safe=False)






