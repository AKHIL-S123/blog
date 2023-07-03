from django.urls import path
from .import views


urlpatterns = [
    
    path('<slug:slug>',views.home.as_view(),name='home'),
    path('about/',views.about.as_view(),name='about'),
    
    path('',views.index.as_view(), name='index' ),
    
]
