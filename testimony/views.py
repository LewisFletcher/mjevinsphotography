from django.views.generic import ListView
from .models import Testimonial

class TestimonialView(ListView):
    template_name = 'testimonials.html'
    model = Testimonial
    context_object_name = 'testimonials'
    ordering = ['-date']
    queryset = Testimonial.objects.all()
