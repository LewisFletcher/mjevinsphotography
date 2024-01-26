from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='testimonials')

    def __str__(self):
        return self.name