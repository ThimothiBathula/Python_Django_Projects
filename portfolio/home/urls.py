
from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.home1,name="home1"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('projects/',views.projects,name="projects")
]