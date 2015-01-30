from django.views import generic

from projects.models import Project


class IndexView(generic.ListView):
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.all().order_by('-created')
