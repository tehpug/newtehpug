from django.contrib import admin
from django.contrib.auth.models import User

from members.models import Member, SocialSite, SocialLink


class MemberInline(admin.StackedInline):
    model = Member


class UserAdmin(admin.ModelAdmin):
    inlines = (MemberInline,)


admin.site.register(SocialSite)
admin.site.register(SocialLink)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
