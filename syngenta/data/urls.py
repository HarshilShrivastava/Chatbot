from django.urls import path
from .views import process
from .hindi import process as ph
urlpatterns = [
    path('query/', process),
    path("hindi/",ph),
]