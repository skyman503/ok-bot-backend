from django.http import HttpResponse
from .models import DiscordUser
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def test(request):
    return HttpResponse("elo")

def get_background(request, userid):
    if request.method == "GET":
        try:
            user = DiscordUser.objects.get(pk=userid)
            return HttpResponse(user.background, content_type='image/png')
        except ObjectDoesNotExist:
            with open(f'media/default/default.png', mode='rb') as f:
                return HttpResponse(f, content_type='image/png')