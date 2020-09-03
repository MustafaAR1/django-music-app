from django.urls import path
from . import views

urlpatterns = [
    #/music/
    path('', views.index, name='index'),


    # /music/1231  ->> index no day raha 
    path('<int:album_id>/',views.details,name="details")


    # path('<int:album_id>',views.details,name="details")
]