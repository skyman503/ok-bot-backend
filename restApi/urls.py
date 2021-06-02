from django.urls import path
from .views import get_background, create_user, update_background

urlpatterns = [
    path(r"get-background/<userid>", get_background),
    path(r"update-background", update_background),
    path(r"create-user", create_user)
]