from django.urls import path
from . import views
 

urlpatterns = [
        path('',views.index,name="index"),
        path('<int:year>/<str:month>/',views.index,name="index"),
        path('add_venue/', views.add_venue, name='add-venue'),
        path('registration/', views.registration, name='registration'),
    ]