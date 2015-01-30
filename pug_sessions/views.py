from django.views import generic

from pug_sessions.models import PugSession, Place


class SessionIndexView(generic.ListView):
    context_object_name = 'session_list'

    def get_queryset(self):
        return PugSession.objects.all().order_by('-created')


class SessionDetailView(generic.DetailView):
    model = PugSession
    context_object_name = 'session'


class PlaceIndexView(generic.ListView):
    context_object_name = 'place_list'

    def get_queryset(self):
        return Place.objects.all().order_by('-created')
