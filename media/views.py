from django.views import generic
from django.http import Http404
from django.shortcuts import get_object_or_404

from media.models import Image, Audio, Presentation, Video


class MediaListView(generic.ListView):
    context_object_name = 'media_list'
    template_name = 'media/media_list.html'

    def get_queryset(self):
        media = []
        media.extend(Image.objects.all())
        media.extend(Audio.objects.all())
        media.extend(Presentation.objects.all())
        media.extend(Video.objects.all())

        return sorted(
            media, key=lambda item: item.created, reverse=True  # latest first
        )


class MediaDetailView(generic.ListView):
    template_name = 'media/media_detail.html'
    context_object_name = 'media'

    def get_queryset(self):
        media_types = {
            'image': Image,
            'audio': Audio,
            'presentation': Presentation,
            'video': Video
        }

        if self.kwargs['type'] not in media_types:
            raise Http404('Invalid media type: {}'.format(self.kwargs['type']))

        return get_object_or_404(
            media_types[self.kwargs['type']],
            pk=self.kwargs['pk']
        )
