from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('submitPart1', views.submitPart1, name='submitPart1'),
    path('submitPart2', views.submitPart2, name='submitPart2')
]