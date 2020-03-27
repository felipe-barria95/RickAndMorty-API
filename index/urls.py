from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('about/', views.about, name='index'),
    path('episode/<int:id_episode>', views.episode, name='index'),
    path('character/<int:id_character>', views.character, name='index'),
    path('location/<int:id_location>', views.location, name='index'),
    path('search/<str:texto>', views.search, name='index'),
]
