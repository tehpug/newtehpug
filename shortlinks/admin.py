from django.contrib import admin
from shortlinks.models import Shortlink


class ShortlinkAdmin(admin.ModelAdmin):
    list_display = ('slug', 'url', 'image', 'created', 'modified')


admin.site.register(Shortlink, ShortlinkAdmin)
