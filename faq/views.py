from django.views import generic

from faq.models import FAQ


class FAQListView(generic.ListView):
    model = FAQ
