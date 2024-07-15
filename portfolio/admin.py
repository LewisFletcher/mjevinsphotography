from django.contrib import admin
from .models import PhotoType, Photo, CoverPhoto, PrivatePhotoCategory, PrivatePhoto

# Register your models here.

admin.site.register(PhotoType)
admin.site.register(Photo)
admin.site.register(CoverPhoto)
admin.site.register(PrivatePhotoCategory)
admin.site.register(PrivatePhoto)