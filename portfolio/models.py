from django.db import models

# Create your models here.

class PhotoType(models.Model):
    name= models.CharField(max_length=50)
    desciption= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name= models.CharField(max_length=50)
    photo_type = models.ForeignKey(PhotoType, on_delete=models.CASCADE, related_name='photo_type_set')
    description= models.CharField(max_length=500, null=True, blank=True)
    pictured_persons = models.CharField(max_length=500, null=True, blank=True)
    pictured_place = models.CharField(max_length=500, null=True, blank=True)
    image= models.ImageField(blank=True, upload_to='images/')
    uploaded= models.DateTimeField(auto_now=True)
    landscape = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CoverPhoto(models.Model):
    photo = models.ForeignKey(Photo, related_name='cover_photo', on_delete=models.CASCADE)
    photo_type = models.ForeignKey(PhotoType, related_name='cover_photo_type', on_delete=models.CASCADE)
    order = models.IntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.photo_type.name
    
class PrivatePhotoCategory(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, help_text='Name of the category')
    description = models.CharField(max_length=200, null=True, blank=True, help_text='Description of the category')
    allowed_users = models.ManyToManyField('auth.User', related_name='allowed_users', blank=True, help_text='Users allowed to view this category')
    url_slug = models.SlugField(max_length=50, unique=True, null=True, blank=True, help_text='URL slug for the category (this will be used in the URL to access the category)')

    def __str__(self):
        return "https://mjevinsphoto.com/portfolio/private/" + self.url_slug
    
class PrivatePhoto(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, help_text='Name of the photo')
    image = models.ImageField(blank=True, upload_to='images/', help_text='The photo')
    uploaded = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(PrivatePhotoCategory, related_name='private_photos', on_delete=models.CASCADE)
    landscape = models.BooleanField(default=False)

    def __str__(self):
        return self.name
