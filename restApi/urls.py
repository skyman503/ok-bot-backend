from django.urls import path
from .views import get_background

urlpatterns = [
    path(r"get-background/<userid>", get_background)
]