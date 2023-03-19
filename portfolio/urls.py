from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='portfolio'),
    path('type/<int:pk>', views.TypeView.as_view(), name='type_view'),
    path('photo/<int:pk>', views.get_photo, name='photo'),
]