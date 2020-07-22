from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('farmbutton', views.farmfun),
    path('cavebutton', views.cavefun),
    path('housebutton', views.housefun),
    path('casinobutton', views.casinofun),
    path('restart', views.restart),	   
]
