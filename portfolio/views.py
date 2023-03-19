from django.shortcuts import render
from django.views.generic import View
from .models import Photo, PhotoType, CoverPhoto
from collections import defaultdict
from django.http import JsonResponse

class MainView(View):
    def get(self, request):
        photo_types = CoverPhoto.objects.all().order_by('order')
        context = {
            'photo_types': photo_types
        }
        return render(request, 'main.html', context)

class TypeView(View):
    def get(self, request, pk):
        photo_type = PhotoType.objects.get(pk=pk)
        context= {
            'photo_type' : photo_type
        }
        return render(request, 'type_view.html', context)

def get_photo(request, pk):
    photo = Photo.objects.filter(pk=pk)
    data = {
        'image_url': photo.image.url
    }
    return JsonResponse(data)