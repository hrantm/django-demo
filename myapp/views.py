from django.forms import model_to_dict
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return HttpResponse('Hello World')

def items(request):
    items = TodoItem.objects.all()
    # items = {}
    
    return JsonResponse({'items': [model_to_dict(item)for item in items]})
