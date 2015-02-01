from django.contrib import admin

from media.models import Image, Audio, Presentation, Video

DEFAULT_LIST_DISPLAY = ('title', 'description', 'created', 'modified')


class ImageAdmin(admin.ModelAdmin):
    list_display = DEFAULT_LIST_DISPLAY + ('image',)


class AudioAdmin(admin.ModelAdmin):
    list_display = DEFAULT_LIST_DISPLAY + ('link',)


class PresentationAdmin(admin.ModelAdmin):
    list_display = DEFAULT_LIST_DISPLAY + ('link',)


class VideoAdmin(admin.ModelAdmin):
    list_display = DEFAULT_LIST_DISPLAY + (
        'preview', 'direct_link',
        'youtube_link', 'direct_link'
    )


admin.site.register(Image, ImageAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Video, VideoAdmin)
