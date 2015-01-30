from django.contrib import admin
from projects.models import License, Project, Technology


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created', 'modified')


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created', 'modified')


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'link', 'source',
        'license', 'created', 'modified'
    )


admin.site.register(License, LicenseAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
