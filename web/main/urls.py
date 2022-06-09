from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('registration', views.registration, name='registration'),
    path('about', views.about, name='about'),
    path('video', views.video, name='video'),
    path('school', views.school, name='school'),
    path('news', views.news, name='news'),
    path('create_news', views.create_news, name='create_news')
]
