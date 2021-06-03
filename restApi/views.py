from django.http import HttpResponse, JsonResponse
from .models import DiscordUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from djangoProject.settings import DISCORD_SECRET
import requests


@csrf_exempt
def get_background(request, userid):
    if request.method == "GET":
        try:
            user = DiscordUser.objects.get(pk=userid)
            return HttpResponse(user.background, content_type='image/png', status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            with open(f'media/default/default.png', mode='rb') as f:
                return HttpResponse(f, content_type='image/png', status=status.HTTP_200_OK)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def update_background(request):
    if request.method == "POST":
        userid = request.POST.get("id")
        background = request.FILES["background"]
        try:
            user = DiscordUser.objects.get(pk=userid)
            user.background = background
            user.save()
            return HttpResponse(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    else:
        HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        userid = request.POST.get("id")
        background = request.FILES["background"]
        u = DiscordUser(id=userid, background=background)
        u.save()
        return HttpResponse(status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def exchange_code(code):
    API_ENDPOINT = 'https://discord.com/api/v8'
    data = {
        'client_id': "849690251575689226",
        'client_secret': DISCORD_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': "http://localhost:4200/"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
    r.raise_for_status()
    return r.json()


@csrf_exempt
def login(request):
    if request.method == "POST":
        code = request.POST.get("auth_code")
        response = exchange_code(code)
        headers = {
            'Authorization': f"Bearer {response['access_token']}"
        }
        r = requests.get("https://discord.com/api/v8/users/@me", headers=headers)
        r.raise_for_status()
        print(r.json())
        return JsonResponse(r.json())