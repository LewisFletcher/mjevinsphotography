from django.shortcuts import render
from django.views.generic import View, ListView
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

class TypeView(ListView):
    model = Photo
    template_name = 'type_view.html'
    context_object_name = 'photos'
    paginate_by = 9

    def get_queryset(self):
        return Photo.objects.filter(photo_type=self.kwargs['pk'])
    
    def get_template_names(self):
        if self.request.htmx:
            return 'photo_loop.html'
        return 'type_view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = self.request.path
        return context

    

def get_photo(request, pk):
    photo = Photo.objects.filter(pk=pk)
    data = {
        'image_url': photo.image.url
    }
    return JsonResponse(data)