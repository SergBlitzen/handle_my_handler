from django.contrib import admin

from index.models import Handler, SocialLink


@admin.register(Handler)
class HandlerAdmin(admin.ModelAdmin):
    ...


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    ...
