from django.contrib import admin
from pug_sessions.models import Place, PugSession


class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'link_to_map',
        'image', 'created', 'modified'
    )


class PugSessionAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'place',
        'start', 'end', 'created', 'modified'
    )


admin.site.register(Place, PlaceAdmin)
admin.site.register(PugSession, PugSessionAdmin)
