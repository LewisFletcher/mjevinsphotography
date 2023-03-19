from django.shortcuts import render
from django.views.generic import View
from .models import AboutMe

# Create your views here.

class AboutPage(View):
    def get(self, request):
        about = AboutMe.objects.filter().first()
        context = {'about' : about}
        return render(request, 'about.html', context)