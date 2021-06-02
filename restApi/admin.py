from django.contrib import admin
from restApi import models

# Register your models here.
@admin.register(models.DiscordUser)
class AuthorAdmin(admin.ModelAdmin):
    pass