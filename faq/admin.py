from django.contrib import admin
from faq.models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

admin.site.register(FAQ, FAQAdmin)
