from django.contrib import admin
from slideshows.models import Slideshow


class SlideshowAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'link',
        'image', 'created', 'modified'
    )

admin.site.register(Slideshow, SlideshowAdmin)
