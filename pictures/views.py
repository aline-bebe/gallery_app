
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'all_images/index.html',{"images":images,"location":location})


def location(request,location_id):
    photos=Image.objects.filter(location_id=location_id)

    return render(request,'all_images/location.html',{"photos":photos})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_category(search_term)
        
        message = f"{search_term}"
        
        return render(request, 'all_images/search.html',{"message":message,"thecat":searched_categories})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all_images/search.html',{"message":message,"thecat":searched_categories })